# pyenv

Master: [![Build Status](https://travis-ci.org/sansible/pyenv.svg?branch=master)](https://travis-ci.org/sansible/pyenv)  
Develop: [![Build Status](https://travis-ci.org/sansible/pyenv.svg?branch=develop)](https://travis-ci.org/sansible/pyenv)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Arguments](#Arguments)
* [Examples](#examples)
* [Development & Testing](#development---testing)

This role configures pyenv, compiles Python versions from source, and installs Python modules for the latter.

It can be run muliple times for multiple Python versions and users.

**Note:** Module installation will be skipped if `sansible_pyenv_python_version` is "system"; use the ansible `pip` module for this task instead.


## Installation and Dependencies

To install this role run `ansible-galaxy install sansible.pyenv`
or add this to your `roles.yml`

```YAML
- name: sansible.pyenv
  version: v2.1.x
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs pyenv and a Python version (via `pyenv global <version>`)
* `configure` - Does nothing at this stage

## Arguments

Argument | Required | Default | Description
---------|----------|---------|------------
sansible_pyenv_user | no | root | User for which pyenv, Python, and Python modules will be installed
sansible_pyenv_activate | no | no | Whether or not to activate the Python version
sansible_pyenv_python_version | yes |  | Version of Python to install
sansible_pyenv_python_modules | no | [] | List of Python modules to install (skipped if `sansible_pyenv_python_version` is "system")


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
      sansible_pyenv_activate: yes
      sansible_pyenv_python_modules:
        - ansible
        - ansible-lint
        - six
      sansible_pyenv_user: jenkins
      sansible_pyenv_python_version: 2.7.14
```

Install Pyenv globally for all users:

```YAML
- name: Install pyenv globally
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
      sansible_pyenv_global_install: yes
      sansible_pyenv_installation_dir: /usr/local/bin/pyenv
      sansible_pyenv_python_modules:
        - ansible
        - ansible-lint
        - six
      sansible_pyenv_python_version: 3.6.7
```

When installing globally the installation directory should be overridden (the 
default is to use the root users home directory) in this instance 
/usr/local/bin is used. When installed globally a global profile file is put 
in place, defaulting to /etc/profile.d/pyenv.sh (can be overidden via the 
sansible_pyenv_global_profile_file var)

## Development & Testing

If you want to work on this role, please start with running
`make watch`. This will re-provision docker images on any file changes.
