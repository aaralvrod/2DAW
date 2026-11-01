import datetime

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from model_bakery import baker

from appointments.models import Appointment
from slots.models import Slot

User = get_user_model()


@pytest.mark.django_db
def test_required_apps_are_installed():
    REQUIRED_APPS = ('accounts', 'slots', 'appointments')

    custom_apps = [app for app in settings.INSTALLED_APPS if not app.startswith('django')]
    for app in REQUIRED_APPS:
        app_config = f'{app}.apps.{app.title()}Config'
        assert app_config in custom_apps, (
            f'La aplicación <{app}> no está "creada/instalada" en el proyecto.'
        )
    assert len(custom_apps) >= len(REQUIRED_APPS), (
        'El número de aplicaciones propias definidas en el proyecto no es correcto.'
    )


# ==============================================================================
# SLOT
# ==============================================================================


@pytest.mark.django_db
def test_slot_model_is_correctly_configured():
    # start_at field
    assert (start_at := Slot._meta.get_field('start_at')), 'Slot.start_at no se ha definido'
    assert start_at.get_internal_type() == 'TimeField', 'Slot.start_at no es del tipo esperado'
    assert not start_at.unique, 'Slot.start_at no debe ser un campo único (por sí solo)'

    # end_at field
    assert (end_at := Slot._meta.get_field('end_at')), 'Slot.end_at no se ha definido'
    assert end_at.get_internal_type() == 'TimeField', 'Slot.end_at no es del tipo esperado'
    assert not end_at.unique, 'Slot.end_at no debe ser un campo único (por sí solo)'

    # Meta options
    assert Slot._meta.unique_together == (('start_at', 'end_at'),), (
        'La configuración de claves únicas juntas del modelo Slot no es correcta.'
    )
    assert Slot._meta.ordering == ['start_at', 'end_at'], (
        'La configuración de ordenación del modelo Slot no es correcta.'
    )


@pytest.mark.django_db
def test_str_representation_of_slot():
    slot = baker.make_recipe(
        'tests.slot', start_at=datetime.time(9, 0), end_at=datetime.time(10, 0)
    )
    assert str(slot) == '09:00 - 10:00', (
        'La representación en cadena de texto del modelo Slot no es correcta.'
    )


# ==============================================================================
# APPOINTMENT
# ==============================================================================


@pytest.mark.django_db
def test_appointment_model_is_correctly_configured():
    # date field
    assert (date := Appointment._meta.get_field('date')), 'Appointment.date no se ha definido'
    assert date.get_internal_type() == 'DateField', 'Appointment.date no es del tipo esperado.'
    assert not date.unique, 'Appointment.date no debe ser un campo único (por sí solo).'

    # user field
    assert (user := Appointment._meta.get_field('user')), 'Appointment.user no se ha definido.'
    assert user.get_internal_type() == 'ForeignKey', 'Appointment.user no es del tipo esperado.'
    assert user.remote_field.model == User, 'Appointment.user no referencia al modelo esperado'
    assert user.remote_field.on_delete.__name__ == 'CASCADE', (
        'Appointment.user no tiene el método de borrado esperado'
    )
    assert user.remote_field.related_name == 'appointments', (
        'Appointment.user no tiene el related_name esperado.'
    )

    # slot field
    assert (slot := Appointment._meta.get_field('slot')), 'Appointment.slot no se ha definido.'
    assert slot.get_internal_type() == 'ForeignKey', 'Appointment.slot no es del tipo esperado.'
    assert slot.remote_field.model == Slot, 'Appointment.slot no referencia al modelo esperado.'
    assert slot.remote_field.on_delete.__name__ == 'CASCADE', (
        'Appointment.slot no tiene el método de borrado esperado.'
    )
    assert slot.remote_field.related_name == 'appointments', (
        'Appointment.slot no tiene el related_name esperado.'
    )
    assert not slot.unique, 'Appointment.slot no debe ser un campo único (por sí solo).'

    # Meta options
    assert Appointment._meta.unique_together == (('date', 'slot'),), (
        'La configuración de claves únicas juntas del modelo Appointment no es correcta.'
    )
    assert Appointment._meta.ordering == ['date', 'slot'], (
        'La configuración de ordenación del modelo Appointment no es correcta.'
    )


@pytest.mark.django_db
def test_str_representation_of_appointment():
    slot = baker.make_recipe(
        'tests.slot', start_at=datetime.time(9, 0), end_at=datetime.time(10, 0)
    )
    appointment = baker.make_recipe('tests.appointment', date=datetime.date(2024, 1, 1), slot=slot)
    assert str(appointment) == '2024-01-01 (09:00 - 10:00)', (
        'La representación en cadena de texto del modelo Appointment no es correcta.'
    )
