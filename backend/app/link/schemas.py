from re import fullmatch
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, validator


class UrlIn(BaseModel):
    url: HttpUrl
    slug: Optional[str] = Field(min_length=5, max_length=64)

    @validator('slug')
    def is_correct_slug(cls, value):
        if fullmatch(r"[a-z0-9]+(?:[-_]?[a-z0-9]+)*", value) is not None:
            return value
        raise ValueError('This is not correct slug')
