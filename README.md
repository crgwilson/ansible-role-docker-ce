# Ansible role: Docker-CE

![Molecule Test](https://github.com/crgwilson/ansible-role-docker-ce/workflows/Molecule%20Test/badge.svg)

Install and manage [docker community edition](https://www.docker.com/products/container-runtime)


## Variables

All variables are really straight forward, there's no real reason to need to change any of them.


## TODO

* Manage daemon config
* Manage storage driver config
* Manage network driver config
* Support for installing an arbitrary number of containers


## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
