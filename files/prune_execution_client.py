#!/usr/bin/python3
'''
Author: SlingNode
License: MIT

This script is used to trigger pruning of the execution client. The script can trigger pruning every time
it is run (--always_prune) or it can trigger if the remaining percentage of the free disk space is
less than the specified value (--min_free_disk_percentage).

It makes API call to the execution client to verify that the sync is complete before starting to prune.

The script does the following:

    1. Check if sync is complete
    2. Retrieve disk space info
    3. If --min_free_disk_percentage > free disk space OR --always_prune is set - trigger pruning

Client specific notes:

Geth - only supports offline pruning. The script uses Docker SDK to stop the running container
    and start a temporary pruning container. When pruning has completed, it restarts the original
    Geth container.

Nethermind - supports online pruning. The script triggers the pruning using the API call to Nethermind.

'''

import logging
from logging.handlers import RotatingFileHandler
import shutil
import argparse
import sys
from typing import List, Dict

import docker
import requests

from docker.types import LogConfig
from docker.models import containers


SUPPORTED_CLIENTS: List[str] = [
    'geth',
    'nethermind'
]

EXECUTION_CLIENT_CONTAINER_NAME = "blockchain_dc_execution_1"


def is_sync_in_progress(endpoint) -> bool:

    json_data = {"jsonrpc": "2.0", "method": "eth_syncing", "params": [], "id": 1}
    response = requests.post(endpoint, json=json_data)

    logging.info(f"is_sync_in_progress response -> {response.json()}")

    return response.json()['result']


def setup_logger(log_path='/var/log/prune_execution_client.log', level=logging.DEBUG) -> logging.Logger:

    logger = logging.getLogger("prune_execution_client")
    logger.setLevel(level=level)
    handler = RotatingFileHandler(log_path, maxBytes=1000000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def get_disk_space_info() -> Dict[str, float]:

    gb = 2**30
    total, used, free = shutil.disk_usage('/')

    return {
        'total': total / gb,
        'used': used / gb,
        'free': free / gb,
        'used_percentage': used / total * 100,
        'free_percentage': free / total * 100
    }


def execution_client_is_supported(supported_clients_list: List[str], exec_client: str) -> bool:

    return exec_client in supported_clients_list


def setup_docker_log_format() -> LogConfig:

    return LogConfig(
        type=LogConfig.types.JSON,
        config={
            'max-size': '10m',
            'max-file': '1',
            'tag': 'blockchain|pruning|geth|{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}'
        }
    )


def correct_execution_client_is_running(execution_client_name: str, execution_client_container) -> bool:

    return execution_client_name == execution_client_container.labels.get('com.slingnode.client')


def prune_geth() -> None:

    client = docker.from_env()

    execution_client_container: containers.Container = client.containers.get(EXECUTION_CLIENT_CONTAINER_NAME)

    logger.info(f"Acquired execution client container -> {execution_client_container.short_id}, {execution_client_container.image}")

    if not correct_execution_client_is_running("geth", execution_client_container):

        logger.error(f"Running client is not Geth. Detected client is {execution_client_container.labels.get('com.slingnode.client')}")
        sys.exit(1)

    execution_client_container.stop()
    logger.info("Stopped geth container")
    logger.info("Starting pruning")

    docker_log_config: LogConfig = setup_docker_log_format()

    execution_clients = {

        'geth': {
            'image': 'ethereum/client-go',
            'name': 'prune_geth',
            'volumes': [
                '/opt/blockchain/execution:/gethdata:rw',
                '/etc/localtime:/etc/localtime:ro'
                ],
            'command': ['--datadir', '/gethdata', '--log.json', '--verbosity', '3', 'snapshot', 'prune-state']
        }
    }

    client.containers.run(
        execution_clients['geth']['image'],
        name=execution_clients['geth']['name'],
        command=execution_clients['geth']['command'],
        volumes=execution_clients['geth']['volumes'],
        remove=True,
        detach=False,
        log_config=docker_log_config
    )

    logger.info('Pruning complete.')
    logger.info('Restarting execution client container')

    execution_client_container.start()

    logger.info('Execution client container started')


def prune_nethermind(endpoint) -> None:

    client = docker.from_env()

    execution_client_container: containers.Container = client.containers.get(EXECUTION_CLIENT_CONTAINER_NAME)

    if not correct_execution_client_is_running("nethermind", execution_client_container):

        logger.error(f"Running client is not nethermind. Detected client is {execution_client_container.labels.get('com.slingnode.client')}")
        sys.exit(1)

    json_data = {"method": "admin_prune", "params": [], "id": 1, "jsonrpc": "2.0"}
    response = requests.post(endpoint, json=json_data)

    logging.info(f"admin_prune response -> {response.json()}")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='Prune execution client utility',
        description='Script used to prune Ethereum execution clients',
        epilog='')

    parser.add_argument('--always_prune', dest='always_prune', action='store_true',
                        help='When enabled the script will always trigger pruning ignoring disk space criteria')
    parser.add_argument('--min_free_disk_percentage', dest='min_free_disk_percentage', action='store', type=float,
                        help='Triggers prunning when percentage of free disk space is less than specified value')
    parser.add_argument('--execution_client_to_prune', dest='execution_client_to_prune', action='store', type=str,
                        choices=SUPPORTED_CLIENTS, help='Client to prune. Must be in the SUPPORTED_CLIENTS list')
    parser.add_argument('--execution_client_endpoint', dest='execution_client_endpoint', action='store', type=str,
                        help='JSON RPC endpoint. Default: http://localhost:8545')

    logger = setup_logger()

    logger.info("pruning script started")

    args = parser.parse_args()

    execution_client_to_prune: str = args.execution_client_to_prune

    execution_client_endpoint = ''

    if args.execution_client_endpoint:
        execution_client_endpoint = args.execution_client_endpoint
    else:
        execution_client_endpoint = 'http://localhost:8545'

    if not (args.always_prune or args.min_free_disk_percentage):
        print("One of --always_prune or --min_free_disk_space_percentage must be set. Exiting...")
        logger.error("Incorrect flags set. Exiting.")
        sys.exit(1)

    if is_sync_in_progress(execution_client_endpoint):

        logger.error("Sync in progress. Exiting.")
        sys.exit(1)

    else:

        if execution_client_to_prune == 'geth':

            if args.always_prune:
                logger.debug("args.always_prune condition met")

                prune_geth()

            else:

                disk_usage: Dict = get_disk_space_info()
                logger.info(f"disk_usage -> {disk_usage}")

                if args.min_free_disk_percentage > disk_usage['free_percentage']:

                    logger.debug("args.min_free_disk_percentage < disk_usage['free_percentage'] condition met")
                    prune_geth()

        elif execution_client_to_prune == 'nethermind':

            if args.always_prune:

                prune_nethermind(execution_client_endpoint)

            else:

                disk_usage: Dict = get_disk_space_info()

                if args.min_free_disk_percentage > disk_usage['free_percentage']:

                    prune_nethermind(execution_client_endpoint)
