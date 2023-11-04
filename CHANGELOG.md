# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.26.0] - 2023-11-04

### Changed

- Updated Nimbus from 23.9.1 to 23.10.0
- Updated Prysm from 4.0.8 to 4.1.1
- Updated Erigon from 2.52.5 to 2.53.4
- Updated Nethermind from 1.21.0 to 1.21.1
- Updated Geth from 1.13.3 to 1.13.4
- Updated Besu from 23.10.0 to 23.10.1

## [0.25.0] - 2023-10-17

### Changed

- Updated Teku from 23.9.1 to 23.10.0
- Updated Geth from 1.13.2 to 1.13.3
- Updated Besu from 23.7.3 to 23.10.0
- Updated Erigon from 2.49.3 to 2.52.5
- Updated Nethermind from 1.20.4 to 1.21.0

## [0.24.0] - 2023-09-28

### Changed

- Updated Erigon from 2.49.2 to 2.49.3
- Updated Geth from 1.13.1 to 1.13.2

## [0.23.0] - 2023-09-27

### Changed

- Updated Lodestar from 1.11.1 to 1.11.3
- Updated Nethermind from 1.20.3 to 1.20.4
- Updated Besu from 23.7.2 to 23.7.3
- Updated Lighthouse from 4.4.1 to 4.5.0
- Updated Nimbus from 23.9.0 to 23.9.1
- Updated Teku from 23.9.0 to 23.9.1

## [0.22.0] - 2023-09-18

### Changed

- Updated Nimbus from 23.8.0 to 23.9.0
- Updated Erigon from 2.49.0 to 2.49.2
- Updated Geth from 1.12.2 to 1.13.1
- Increased number of retries in verify tasks for expose_ports and multi_tier scenarios to 60

## [0.21.0] - 2023-09-10

### Changed

- Updated Besu from 23.4.4 to 23.7.2
- Updated Lighthouse from 4.3.0 to 4.4.1
- Updated Prysm from 4.0.7 to 4.0.8
- Updated Nimbus from 23.7.0 to 23.8.0
- Updated Lodestar from 1.10.0 to 1.11.1
- Updated Erigon from 2.48.1 to 2.49.0
- Updated Teku from 23.8.0 to 23.9.0
- Updated Nethermind from 1.20.1 to 1.20.3
- Increased number of retries in verify tasks for expose_ports and multi_tier scenarios

## [0.20.0] - 2023-08-19

### Changed

- Updated Geth from 1.12.0 to 1.12.2

## [0.19.0] - 2023-08-04

### Changed

- Updated Lodestar from 1.9.2 to 1.10.0
- Updated Teku from 23.6.2 to 23.8.0

## [0.18.1] - 2023-07-26

### Fixed

- Changed Lodestar image tag from latest to specific version
- Increased number of retries for GET  consensus_client_http_port molecule test

## [0.18.0] - 2023-07-25

### Changed

- Updated Nimbus from 23.6.1 to 23.7.0
- Updated Prysm from 4.0.6 to 4.0.7
- Updated Lighthouse from 4.2.0 to 4.3.0
- Updated Teku from 23.6.1 to 23.6.2
- Updated Erigon from 2.48.0 to 2.48.1
- Updated Nethermind from 1.19.3 to 1.20.1

## [0.17.0] - 2023-07-02

### Fixed

- Fixed added task to update apt cache to avoid cache in Ubuntu

### Changed

- Updated Nethermind image tag from v1.19.2 to v1.19.3
- Updated Erigon image tag from v2.45.2 to v2.48.0
- Updated Teku image tag from 23.6.0 to 23.6.1
- Updated Besu image tag from 23.4.1 to 23.4.4
- Updated Nimbus image tag from v23.5.0 to v23.6.1

## [0.16.0] - 2023-06-23

### Changed

- Renamed validator_keymanager_enabled variable to lodestar_validator_api_enabled


## [0.15.0] - 2023-06-15

### Changed

- Added lodestar consensus and validator clients

## [0.14.0] - 2023-06-15

### Changed

- Updated Nethermind image tag from v1.19.0 to v1.19.2
- Updated Erigon image tag from v2.44.1 to v2.45.2
- Updated Teku image tag from 23.5.0 to 23.6.0
- Updated Prysm image tags from v4.0.5 to v4.0.6

## [0.13.0] - 2023-06-05

### Changed

- Updated Nethermind image tag from v1.18.2 to v1.19.0
- Updated Erigon image tag from v2.43.1 to v2.44.0

## [0.12.0] - 2023-05-27

### Changed

- Updated Nethermind image tag from v1.18.0 to v1.18.2
- Updated Prysm image tag from v4.0.4 to v4.0.5
- Updated Lighthouse image tag from v4.0.1-modern to v4.2.0-modern
- Updated Geth image tag from v1.11.6 to v1.12.0
- Updated Besu image tag from 23.4.0 to 23.4.1

## [0.11.0] - 2023-05-20

### Changed

- Updated Nimbus image tag from v23.5.0 to v23.5.1
- Updated Erigon image tag from v2.43.0 to v2.43.1


## [0.10.0] - 2023-05-17

### Changed

- Updated Prysm image tag from v4.0.3-hotfix to v4.0.4

## [0.9.0] - 2023-05-13
### Changed

- Hotfix Prysm image tag from v4.0.3 to v4.0.3-hotfix - https://github.com/prysmaticlabs/prysm/releases/tag/v4.0.3-hotfix
- Updated Teku image tag from 23.4.0 to 23.5.0
- Fixed community.docker version in README

## [0.8.0] - 2023-05-09

### Changed

- Updated Ansible community.docker from 3.4.0 to 3.4.5
- Updated Nethermind image tag from 1.17.4 to 1.18.0
- Updated Besu image tag from 23.1.2 to 23.4.0
- Removed Besu flag `besu_xbonsai_use_snapshots` - https://github.com/hyperledger/besu/pull/5337

## [0.7.0] - 2023-04-26

### Changed

- Updated Nimbus image tag from v23.3.2 to v23.4.0
- Updated Teku image tag from 23.3.1 to 23.4.0
- Updated Erigon image tag from v2.42.0 to v2.43.0
- Removed Erigon flag --externalcl


## [0.6.0] - 2023-04-20

### Changed

- Updated Nethermind image tag from 1.17.3 to 1.17.4
- Updated Lighthouse image tag from v4.0.1-modern to v4.1.0-modern
- Updated Prysm image tag from v4.0.2 to v4.0.3
- Updated Geth image tag from v1.11.5 to v1.11.6


## [0.5.0] - 2023-04-17

### Changed

- Updated Erigon image tag from v2.41.0 to v2.42.0
- Updated Besu image tag from 23.1.2 to 23.1.3
- Updated Prysm image tag from v3.2.2to v4.0.2

## [0.4.1] - 2023-04-10

### Fixed

- Removed spaces from teku metrics endpoint variable

## [0.4.0] - 2023-04-06

### Changed

- Replaced hardcoded /keystore path with a variable  (container_keystore_dir)
- Replaced hardcoded /keystore with container_keystore_dir in Teku validator Docker compose template
- Changed prysm_wallet_file_name from fixed path to a variable
- Changed location of prysm_wallet_file from /keystore dir to the data dir
- Change teku_validator_keys variable from fixed path to variables (no change on location)

### Fixed

- Moved --metrics-publish-endpoint from Teku consensus client to validator client
- Added task to reset file permissions on SSL keystore for Teku validator client

## [0.3.0] - 2023-03-28

### Changed

- Updated Erigon image tag from v2.40.1 to v2.41.0
- Updated Lighthouse image tag from v3.5.1-modern to v4.0.1-modern
- Molecule multi_tier scenario to test the "clients variable" case fixed in this release
- Removed wait_for module from Molecule tests and replaced with "until" in URI module

### Fixed

- Role failing on the last task when "clients" variable did not contain consensus or execution keys

## [0.2.0] - 2023-03-24

### Added

- Added supported OSes section in README

### Changed

- Updated Nethermind image tag from 1.17.2 to 1.17.3
- Updated Teku image tag from 23.3.0 to 23.3.1
- Updated Besu image tag from 23.1.1 to 23.1.2

### Fixed

 - Molecule converge playbooks used the pre-release role name, fixed them to use the correct name
 - Bug in a verify playbook for multi_tier scenario

## [0.1.0] - 2023-03-23

### Added

- initial release
