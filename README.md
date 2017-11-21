# pyenv

Master: [![Build Status](https://travis-ci.org/sansible/pyenv.svg?branch=master)](https://travis-ci.org/sansible/pyenv)  
Develop: [![Build Status](https://travis-ci.org/sansible/pyenv.svg?branch=develop)](https://travis-ci.org/sansible/pyenv)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Arguments](#Arguments)
* [Examples](#examples)
* [Development & Testing](#development---testing)

This role configures pyenv, compiles Python versions from source, and installs Python modules for the latter.

It can be run muliple times for multiple Python versions and users.

**Note:** Module installation will be skipped if `python_version` is "system"; use the ansible `pip` module for this task instead.


## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```


## Installation and Dependencies

To install this role run `ansible-galaxy install sansible.pyenv`
or add this to your `roles.yml`

```YAML
- name: sansible.pyenv
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs pyenv and a Python version (via `pyenv global <version>`)
* `configure` - Does nothing at this stage

## Arguments

Argument | Required | Default | Description
---------|----------|---------|------------
user | no | root | User for which pyenv, Python, and Python modules will be installed
activate | no | no | Whether or not to activate the Python version
python_version | yes |  | Version of Python to install
python_modules | no | [ ] | List of Python modules to install (skipped if `python_version` is "system")


## Examples

Install Python 2.7.14, Python modules ansible, ansible-lint, six, and activate the former for user jenkins:

```YAML
- name: Install pyenv
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.pyenv
      sansible_pyenv:
        user: jenkins
        activate: yes
        python_version: 2.7.14
        python_modules:
          - ansible
          - ansible-lint
          - six
```


## Development & Testing

If you want to work on this role, please start with running
`make watch`. This will re-provision vagrant box on any file changes.
