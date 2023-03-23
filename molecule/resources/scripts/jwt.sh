#!/bin/bash
delimit () {
        printf "\n\n\n------------------------------------$SLINGNODE_EXECUTION -- $SLINGNODE_CONSENSUS------------------------------------\n\n\n"
}

export SLINGNODE_EXECUTION=geth SLINGNODE_CONSENSUS=lighthouse SLINGNODE_VALIDATOR=lighthouse

delimit
molecule test -s jwt

export SLINGNODE_EXECUTION=nethermind SLINGNODE_CONSENSUS=prysm SLINGNODE_VALIDATOR=prysm

delimit
SLINGNODE_BOX=almalinux/9 molecule test -s jwt

unset SLINGNODE_EXECUTION SLINGNODE_CONSENSUS SLINGNODE_VALIDATOR
