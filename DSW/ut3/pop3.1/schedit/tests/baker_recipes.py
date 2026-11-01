import datetime

from faker import Faker
from model_bakery.recipe import Recipe, seq

fake = Faker()


user = Recipe(
    'auth.User',
    username=fake.user_name,
    first_name=fake.first_name,
    last_name=fake.last_name,
    email=fake.email,
    _fill_optional=True,
)

another_user = Recipe(
    'auth.User',
    username=fake.user_name,
    first_name=fake.first_name,
    last_name=fake.last_name,
    email=fake.email,
    _fill_optional=True,
)

slot = Recipe(
    'slots.Slot',
    start_at=seq(datetime.time(8, 0), datetime.timedelta(hours=1)),
    end_at=seq(datetime.time(9, 0), datetime.timedelta(hours=1)),
    _fill_optional=True,
)

appointment = Recipe(
    'appointments.Appointment',
    date=seq(fake.date_between(start_date='+1d', end_date='+2M'), datetime.timedelta(days=1)),
    _fill_optional=True,
)
