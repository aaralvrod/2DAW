import pytest
from model_bakery import baker

CREATURE_LIST_URL = '/creatures/'
CREATURE_DETAIL_URL = '/creatures/{creature_slug}/'


@pytest.fixture
def creature():
    return baker.make_recipe('tests.creature')
