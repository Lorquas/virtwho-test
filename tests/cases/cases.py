'''

'''

import pytest
from virt_who import logger


@pytest.fixture()
def hypervisor_data():
    hypervisor = {
        "hypervisor_uuid": "hypervisor_uuid is ok",
        "hypervisor_hwuuid": "hypervisor_hwuuid is ok",
        "hypervisor_hostname": "hypervisor_hostname is ok"
    }
    return hypervisor


@pytest.fixture()
def register_data():
    register = {
        "server_org": ""
    }
    return register


class TestVirtWhoPackage:

    @pytest.mark.tier1
    def test_check_hypervisor_hostname(self, hypervisor_data):
        assert hypervisor_data['hypervisor_hostname'] is not None
        logger.info(hypervisor_data['hypervisor_hostname'])

    @pytest.mark.tier1
    def test_check_satellite_org(self, register_data):
        assert register_data['server_org'] is ''
        logger.info('Failed to get server_org')

    @pytest.mark.tier2
    @pytest.mark.satelliteOnly
    def test_only_satellite(self):
        assert 1 == 1
        logger.info('Only for satellite case')

    @pytest.mark.tier2
    @pytest.mark.rhsmOnly
    def test_only_rhsm(self):
        assert 1 == 1
        logger.info('Only for rhsm case')