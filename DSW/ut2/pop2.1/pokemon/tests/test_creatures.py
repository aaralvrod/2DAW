import conftest
import pytest
from django.test import Client
from model_bakery import baker
from pytest_django.asserts import assertContains

from creatures.models import Creature

# ==============================================================================
# CREATURE MODEL
# ==============================================================================


@pytest.mark.django_db
def test_creature_representation(creature):
    assert str(creature) == creature.name


# ==============================================================================
# CREATURE LIST
# ==============================================================================


@pytest.mark.django_db
def test_creature_list_page_contains_title(client: Client):
    response = client.get(conftest.CREATURE_LIST_URL)
    assert response.status_code == 200
    assertContains(response, 'Pokemon')
    assertContains(response, 'Creature list')


@pytest.mark.django_db
def test_creature_list_page_contains_creature_names(client: Client):
    creatures = baker.make_recipe('tests.creature', _quantity=10)
    response = client.get(conftest.CREATURE_LIST_URL)
    assert response.status_code == 200
    for creature in creatures:
        assertContains(response, creature.name)


@pytest.mark.django_db
def test_creature_list_page_contains_proper_creature_order(client: Client):
    creatures = baker.make_recipe('tests.creature', _quantity=10)
    response = client.get(conftest.CREATURE_LIST_URL)
    assert response.status_code == 200
    content = response.content.decode('utf-8')
    sorted_creatures = sorted(creatures, key=lambda c: c.name, reverse=True)
    last_index = -1
    for creature in sorted_creatures:
        current_index = content.index(creature.name)
        assert current_index > last_index
        last_index = current_index


@pytest.mark.django_db
def test_creature_list_page_contains_detail_links(client: Client):
    creatures = baker.make_recipe('tests.creature', _quantity=10)
    response = client.get(conftest.CREATURE_LIST_URL)
    assert response.status_code == 200
    for creature in creatures:
        detail_url = conftest.CREATURE_DETAIL_URL.format(creature_slug=creature.slug)
        assertContains(response, detail_url)


@pytest.mark.django_db
def test_creature_list_page_no_creatures_message(client: Client):
    response = client.get(conftest.CREATURE_LIST_URL)
    assert response.status_code == 200
    assertContains(response, 'No creatures yet on database')


@pytest.mark.django_db
def test_creature_list_page_creature_count(client: Client):
    creatures = baker.make_recipe('tests.creature', _quantity=10)
    response = client.get(conftest.CREATURE_LIST_URL)
    assert response.status_code == 200
    assertContains(response, f'Total creatures: {len(creatures)}')


# ==============================================================================
# CREATURE DETAIL
# ==============================================================================


@pytest.mark.django_db
def test_creature_detail_page_contains_title(client: Client, creature: Creature):
    url = conftest.CREATURE_DETAIL_URL.format(creature_slug=creature.slug)
    response = client.get(url)
    assert response.status_code == 200
    assertContains(response, 'Pokemon')
    assertContains(response, 'Creature detail')


@pytest.mark.django_db
def test_creature_detail_page_contains_required_creature_info(client: Client, creature: Creature):
    url = conftest.CREATURE_DETAIL_URL.format(creature_slug=creature.slug)
    response = client.get(url)
    assert response.status_code == 200
    assertContains(response, creature.name)
    assertContains(response, creature.type1)
    assertContains(response, creature.attack)
    assertContains(response, creature.defense)
    assertContains(response, creature.speed)
    assertContains(response, creature.generation)


@pytest.mark.django_db
def test_creature_detail_page_contains_back_link(client: Client, creature: Creature):
    url = conftest.CREATURE_DETAIL_URL.format(creature_slug=creature.slug)
    response = client.get(url)
    assert response.status_code == 200
    assertContains(response, conftest.CREATURE_LIST_URL)
    assertContains(response, 'Back')
