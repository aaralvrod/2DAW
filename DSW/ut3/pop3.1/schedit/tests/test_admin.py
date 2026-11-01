import pytest
from django.contrib import admin

from appointments.models import Appointment
from slots.models import Slot


@pytest.mark.parametrize(
    'model',
    [Appointment, Slot],
)
@pytest.mark.django_db
def test_models_are_registered_in_admin(model):
    assert model in admin.site._registry, (
        f'El modelo "{model.__name__}" no está registrado en el admin'
    )
