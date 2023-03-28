# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
