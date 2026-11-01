import pytest
from django.conf import settings
from django.db import IntegrityError
from model_bakery import baker

from creatures.models import Creature


@pytest.mark.django_db
def test_required_apps_are_installed():
    PROPER_APPS = ('creatures', 'shared')

    custom_apps = [app for app in settings.INSTALLED_APPS if not app.startswith('django')]
    for app in PROPER_APPS:
        app_config = f'{app}.apps.{app.title()}Config'
        assert app_config in custom_apps, (
            f'La aplicación <{app}> no está "creada/instalada" en el proyecto.'
        )
    assert len(custom_apps) >= len(PROPER_APPS), (
        'El número de aplicaciones propias definidas en el proyecto no es correcto.'
    )


@pytest.mark.django_db
def test_creature_model_has_proper_fields():
    PROPER_FIELDS = (
        'name',
        'slug',
        'type1',
        'attack',
        'defense',
        'speed',
        'generation',
    )
    for field in PROPER_FIELDS:
        assert getattr(Creature, field) is not None, (
            f'El campo <{field}> no está en el modelo Creature.'
        )


@pytest.mark.django_db(transaction=True)
def test_creature_model_has_proper_unique_constraints(creature: Creature):
    with pytest.raises(IntegrityError):
        baker.make_recipe('tests.creature', name=creature.name)
    with pytest.raises(IntegrityError):
        baker.make_recipe('tests.creature', slug=creature.slug)


@pytest.mark.django_db
def test_creature_model_has_proper_default_values():
    creature = baker.make(Creature)
    assert creature.attack == 0
    assert creature.defense == 0
    assert creature.speed == 0
    assert creature.generation == 1
