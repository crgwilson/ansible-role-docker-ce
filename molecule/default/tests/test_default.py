import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package', [
    ('docker-ce'),
    ('docker-ce-cli'),
    ('containerd.io')
])
def test_default_packages(host, package):
    p = host.package(package)
    assert p.is_installed


def test_default_service(host):
    s = host.service('docker')
    assert s.is_running
    assert s.is_enabled
