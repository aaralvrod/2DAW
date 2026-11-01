import pytest
from model_bakery import baker

# ==============================================================================
# URL Patterns
# ==============================================================================

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
SIGNUP_URL = '/signup/'

APPOINTMENT_LIST_URL = '/appointments/'
APPOINTMENT_DETAIL_URL = '/appointments/{appointment_pk}/'
APPOINTMENT_ADD_URL = '/appointments/add/'

ADMIN_CHANGE_URL = '/admin/{app_label}/{model_name}/{object_pk}/'

# ==============================================================================
# Helpers
# ==============================================================================


def str_slot(slot):
    return f'{slot.start_at.strftime("%H:%M")} - {slot.end_at.strftime("%H:%M")}'


def str_appointment(appointment):
    return f'{appointment.date} ({str_slot(appointment.slot)})'


def str(item):
    match item.__class__.__name__:
        case 'Slot':
            return str_slot(item)
        case 'Appointment':
            return str_appointment(item)
        case _:
            return str(item)


# ==============================================================================
# Fixtures
# ==============================================================================


@pytest.fixture
def user():
    return baker.make_recipe('tests.user')


@pytest.fixture
def another_user():
    return baker.make_recipe('tests.user')


@pytest.fixture
def slot():
    return baker.make_recipe('tests.slot')


@pytest.fixture
def appointment(slot, user):
    return baker.make_recipe('tests.appointment', slot=slot, user=user)
