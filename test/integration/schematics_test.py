from schematics.models import Model
from schematics.types import StringType, URLType

from equals import instance_of


class Person(Model):
    name = StringType(required=True)
    website = URLType()


def test_instance_of_with_attrs():
    any_person = instance_of(Person).with_attrs(
        name="Bob Barker",
    )
    assert any_person == Person({"name": "Bob Barker"})
