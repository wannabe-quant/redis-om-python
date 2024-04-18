from redis_om._compat import PYDANTIC_V2


if PYDANTIC_V2:
    from pydantic.v1 import EmailStr, ValidationError
else:
    from pydantic import EmailStr, ValidationError
