import pytest


@pytest.fixture
def always_pass():
    assert True
