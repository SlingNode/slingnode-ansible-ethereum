# Ansible Role: Ethereum

slingnode.ethereum is an Ansible role that facilitates deployment of Ethereum clients. Its objective is to enable a consistent way of deploying and upgrading the chosen client mix. The role can be used to deploy:

* a single node running execution, consensus and validator layers
* hundreds of nodes running all three layers
* a distributed set up with each layer running on a separate server on a single or hundreds of servers
* change client mix (as seamlessly as this can be done)
* upgrade clients

# Supported Ethereum clients

Execution clients:

* Geth
* Nethermind
* Besu
* Erigon

Consensus clients:

* Lighthouse
* Prysm
* Teku
* Nimbus (checkpoint sync currently not supported)

Validator clients:

* Lighthouse
* Prysm
* Teku
* Nimbus

# Documentation

The README file provides a basic overview only. Full documentation describing the role in details is available at [https://slingnode.gitbook.io/slingnode.ethereum/](https://slingnode.gitbook.io/slingnode.ethereum/).

# Requirements

Ansible Docker module is required on the Ansible controller. It can be installed using the below command:

```
ansible-galaxy collection install community.docker:==3.4.0
```

# Dependencies

The role requires a running docker daemon and docker compose plugin installed on the target server. The role has been tested with "geerlingguy.docker" role. Refer to [examples repository](https://github.com/SlingNode/slingnode-ethereum-examples) for sample Playbooks.

# Role Variables

Role variables are defined in 'defaults'. This means they have the lowest precedence and can be easily overridden. See [Ansible documentation](https://docs.ansible.com/ansible/latest/playbook\_guide/playbooks\_variables.html#understanding-variable-precedence) for details on the precedence.

All client specific variables are defined in their corresponding variable file. All client specific variables have unique names (prefixed with clientname\_) so there's no risk of a clash.

| Variable location              | Purpose                                                          |
| ------------------------------ | ---------------------------------------------------------------- |
| defaults/main/main.yml         | generic variables for the role; common variables for all clients |
| defaults/main/\{{client\}}.yml | variables specific to the client                                 |
| vars/\{{os\_family\}}.yml      | variables specific to the OS                                     |

## Important variables

This section outlines variables that you will most likely want to modify.

**clients**

"clients" variable defines what clients will be deployed. It defaults to geth and lighthouse. Possible values are:

* execution: geth / nethermind / erigon / besu
* consensus and validator: lighthouse, prysm, teku, nimbus

```yaml
clients:
  execution: geth
  consensus: lighthouse
  validator: lighthouse
```

**deploy\_execution / deploy\_consensus / deploy\_validator**

These three variables define which layer of the stack will be deployed. By default all three layers are deployed. Check out [examples](using-the-role.md) to see how they can be used.

```yaml
deploy_execution: true
deploy_consensus: true
deploy_validator: true
```

**enable\_firewall**

By default set to true, the role will make sure the firewall package is installed and will configure rules for the client that is being deployed.

```yaml
enable_firewall: true
```

This is meant to be a safe default for anyone who uses the role to deploy on a server that is directly exposed to the internet (for example an OVH bare metal server). It is expected that for more enterprise type of deployments this would be set to false. Refer to [Host firewall](https://slingnode.gitbook.io/slingnode.ethereum/architecture/security#host-firewall) section for details and notes on SSH port.

**network**

Specifies Ethereum network to connect to.

```yaml
network: goerli
```

**consensus\_checkpoint\_sync\_enabled**

Enable/disable consensus client checkpoint sync feature. Defaults to "true" (sync from checkpoint).

```yaml
consensus_checkpoint_sync_enabled: true
```

Refer to [Checkpoint sync](https://slingnode.gitbook.io/slingnode.ethereum/checkpoint-sync) section for details.

**consensus\_checkpoint\_sync\_url**

Beacon endpoint to sync from. This needs to match the network you are deploying on. Defaults to Goerli.

```yaml
consensus_checkpoint_sync_url: https://sync-goerli.beaconcha.in
```

Refer to [Checkpoint sync](https://slingnode.gitbook.io/slingnode.ethereum/checkpoint-sync) section for details.

**suggested\_fee\_recipient**

A priority fee recipient address on your validator client instance and consensus node.

```yaml
suggested_fee_recipient: "0xa10214731A6D9eC03d36d1437796D1cEe6a061f7" 
```

**graffiti**

```yaml
graffiti: SlingNode.com
```

# Example playbook

The best place to start is to check the examples project. There are multiple example playbooks ranging from a simple single node deployment to a distributed deployment of a large number of nodes. The examples project includes sample playbooks, inventories and group vars that you can adapt to your needs. The examples project is available here [https://github.com/SlingNode/slingnode-ethereum-examples](https://github.com/SlingNode/slingnode-ethereum-examples)

Sample Playbook:

```yaml
---
- name: Deploy ehtereum stack - whole stack per node - default clients (geth & lighthouse)
  hosts: all
  become: true

  vars:
    suggested_fee_recipient: "0xa10214731A6D9eC03d36d1437796D1cEe6a061f7"
    graffiti: SlingNode.com

  roles:
    - geerlingguy.docker
    - slingnode.ethereum
```

# License

MIT

# Author Information

This role was created in 2023 by [pgjavier](https://github.com/pgjavier) and [karolpivo](https://github.com/karolpivo).
