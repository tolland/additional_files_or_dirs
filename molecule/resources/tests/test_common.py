import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')



def test_that_should_fail(host):
    f = host.file('this_file_doesnt_exist')

    assert f.exists
