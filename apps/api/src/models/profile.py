from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Profile(BaseModel):
    id: UUID
    tier_id: UUID
    created_at: datetime
    display_name: str
    stripe_customer_id: str | None
    funding: int


class ProfileInsertRequest(BaseModel):
    # user id needs to be passed since its created from some "auth" table in the db
    id: UUID
    tier_id: UUID
    display_name: str
    stripe_customer_id: str | None = None


class ProfileUpdateRequest(BaseModel):
    tier_id: UUID | None = None
    display_name: str | None = None
    stripe_customer_id: str | None = None


class ProfileGetRequest(BaseModel):
    tier_id: UUID | None = None
    display_name: str | None = None
    stripe_customer_id: str | None = None
