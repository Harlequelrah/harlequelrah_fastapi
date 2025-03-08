from elrahapi.authorization.meta_model import (
    MetaAuthorization,
    MetaAuthorizationBaseModel,
    MetaAuthorizationPydanticModel,
)
from pydantic import BaseModel, Field
from typing import List, Optional

from elrahapi.authorization.privilege_model import PrivilegeCreateModel


class RoleModel(MetaAuthorization):
    pass


class RoleBaseModel(BaseModel):
    name: str = Field(example="Admin")
    description: str = Field(example="allow to manage all the system")


class RoleCreateModel(RoleBaseModel):
    is_active: Optional[bool] = Field(example=True, default=True)


class RoleUpdateModel(RoleBaseModel):
    is_active: bool = Field(example=True)

class RolePatchModel(BaseModel):
    name: Optional[str] = Field(example="Admin", default=None)
    is_active: Optional[bool] = Field(example=True, default=None)
    description: Optional[str] = Field(example="allow to manage all the system", default=None)


class RolePydanticModel(MetaAuthorizationPydanticModel):
    role_privileges: List["MetaAuthorizationBaseModel"] = []

    class Config:
        from_attributes = True
