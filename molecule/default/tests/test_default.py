import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pip_packages(host):
    pip_packages = host.pip_package.get_packages(
        '/root/.pyenv/versions/2.7.14/bin/pip'
    )
    assert 'ansible' in pip_packages
    assert 'pytest' in pip_packages


def test_python_version(host):
    python_version = host.run('/root/.pyenv/bin/pyenv global')
    assert python_version.stdout == '2.7.14'
