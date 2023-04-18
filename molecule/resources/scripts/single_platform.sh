#!/bin/bash
delimit () {
        printf "\n\n\n------------------------------------$1 ------------------------------------\n\n\n"
        molecule test -s $1
}

delimit expose_ports

delimit jwt

delimit multi_tier
