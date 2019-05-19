import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

@pytest.mark.parametrize('name, version', [
    ('rethinkdb', '2.3.6')
])
def test_rethinkdb_installed(host, name, version):
    pkg = host.package(name)

    assert pkg.is_installed
    assert pkg.version.startswith(version)

def test_check_folders(host):
    folder = host.file('/var/lib/rethinkdb/default')

    assert folder.exists
    assert folder.is_directory
    assert folder.user == "rethinkdb"
    assert folder.group == "rethinkdb"


def test_check_user(host):
    user = host.user("rethinkdb")

    assert user.name == "rethinkdb"
    assert user.group == "rethinkdb"

def test_check_group(host):
    group = host.group("rethinkdb")

    assert group.name == "rethinkdb"
    assert group.exists

def test_database_is_up(host):
    assert host.socket("tcp://127.0.0.1:8080").is_listening
    assert host.socket("tcp://127.0.0.1:28015").is_listening
    assert host.socket("tcp://127.0.0.1:29015").is_listening