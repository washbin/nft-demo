import time

import pytest
from brownie import network

from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpers import LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    # Act
    advanced_collectible, _ = deploy_and_create()
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
