#!/bin/bash
delimit () {
        printf "\n\n\n------------------------------------$SLINGNODE_EXECUTION -- $SLINGNODE_CONSENSUS------------------------------------\n\n\n"
}

export SLINGNODE_EXECUTION=geth SLINGNODE_CONSENSUS=lighthouse SLINGNODE_VALIDATOR=lighthouse

delimit
SLINGNODE_BOX=almalinux/9 molecule test -s expose_ports

export SLINGNODE_EXECUTION=nethermind SLINGNODE_CONSENSUS=prysm SLINGNODE_VALIDATOR=prysm

delimit
molecule test -s expose_ports

export SLINGNODE_EXECUTION=besu SLINGNODE_CONSENSUS=teku SLINGNODE_VALIDATOR=teku

delimit
SLINGNODE_BOX=almalinux/9  molecule test -s expose_ports

export SLINGNODE_EXECUTION=erigon SLINGNODE_CONSENSUS=nimbus SLINGNODE_VALIDATOR=nimbus

delimit
molecule test -s expose_ports

export SLINGNODE_EXECUTION=nethermind SLINGNODE_CONSENSUS=lodestar SLINGNODE_VALIDATOR=lodestar

delimit
molecule test -s expose_ports

unset SLINGNODE_EXECUTION SLINGNODE_CONSENSUS SLINGNODE_VALIDATOR
