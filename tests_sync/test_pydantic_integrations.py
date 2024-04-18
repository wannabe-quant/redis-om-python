import abc
import datetime
from collections import namedtuple

import pytest
import pytest

from redis_om import Field, HashModel, Migrator
from tests._compat import EmailStr, ValidationError


today = datetime.date.today()


@pytest.fixture
def m(key_prefix, redis):
    class BaseHashModel(HashModel, abc.ABC):
        class Meta:
            global_key_prefix = key_prefix

    class Member(BaseHashModel):
        first_name: str
        last_name: str
        email: EmailStr = Field(index=True)
        join_date: datetime.date
        age: int

    Migrator().run()

    return namedtuple("Models", ["Member"])(Member)


def test_email_str(m):
    with pytest.raises(ValidationError):
        m.Member(
            first_name="Andrew",
            last_name="Brookins",
            email="not an email!",
            age=38,
            join_date=today,
        )

    with pytest.raises(ValidationError):
        m.Member(
            first_name="Andrew",
            last_name="Brookins",
            email="andrew@bad-domain",
            age=38,
            join_date=today,
        )
