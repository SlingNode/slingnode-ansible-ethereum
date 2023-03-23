#!/bin/bash
delimit () {
        printf "\n\n\n------------------------------------$SLINGNODE_EXECUTION -- $SLINGNODE_CONSENSUS------------------------------------\n\n\n"
}

export SLINGNODE_EXECUTION=geth SLINGNODE_CONSENSUS=lighthouse SLINGNODE_VALIDATOR=lighthouse

delimit
molecule test -s default_docker

export SLINGNODE_EXECUTION=nethermind SLINGNODE_CONSENSUS=prysm SLINGNODE_VALIDATOR=prysm

delimit
molecule test -s default_docker

export SLINGNODE_EXECUTION=besu SLINGNODE_CONSENSUS=teku SLINGNODE_VALIDATOR=teku

delimit
molecule test -s default_docker

export SLINGNODE_EXECUTION=erigon SLINGNODE_CONSENSUS=nimbus SLINGNODE_VALIDATOR=nimbus

delimit
molecule test -s default_docker

unset SLINGNODE_EXECUTION SLINGNODE_CONSENSUS SLINGNODE_VALIDATOR
