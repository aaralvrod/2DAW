from functools import partial

from faker import Faker
from model_bakery.recipe import Recipe

fake = Faker()

rint1 = partial(fake.random_int, min=1, max=100)
rint2 = partial(fake.random_int, min=1, max=8)

creature = Recipe(
    'creatures.Creature',
    name=fake.unique.first_name,
    slug=fake.unique.slug,
    type1=fake.word,
    attack=rint1,
    defense=rint1,
    speed=rint1,
    generation=rint2,
)
