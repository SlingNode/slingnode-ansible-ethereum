#!/bin/bash
delimit () {
        printf "\n\n\n------------------------------------$SLINGNODE_EXECUTION -- $SLINGNODE_CONSENSUS------------------------------------\n\n\n"
}

export SLINGNODE_EXECUTION=geth SLINGNODE_CONSENSUS=lighthouse SLINGNODE_VALIDATOR=lighthouse

delimit
molecule test -s multi_tier

export SLINGNODE_EXECUTION=nethermind SLINGNODE_CONSENSUS=prysm SLINGNODE_VALIDATOR=prysm

delimit
SLINGNODE_BOX=almalinux/9 molecule test -s multi_tier

export SLINGNODE_EXECUTION=besu SLINGNODE_CONSENSUS=teku SLINGNODE_VALIDATOR=teku

delimit
molecule test -s multi_tier

export SLINGNODE_EXECUTION=erigon SLINGNODE_CONSENSUS=nimbus SLINGNODE_VALIDATOR=nimbus

delimit
SLINGNODE_BOX=almalinux/9 molecule test -s multi_tier

delimit
molecule test -s multi_tier

export SLINGNODE_EXECUTION=besu SLINGNODE_CONSENSUS=lodestar SLINGNODE_VALIDATOR=lodestar


unset SLINGNODE_EXECUTION SLINGNODE_CONSENSUS SLINGNODE_VALIDATOR
