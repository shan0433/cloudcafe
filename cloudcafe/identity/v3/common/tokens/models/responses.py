import json

from cloudcafe.identity.v2_0.common.models.base import BaseIdentityModel

from cloudcafe.identity.v3.common.roles.models.response import Roles
from cloudcafe.identity.v3.common.projects.models.response import Project
from cloudcafe.identity.v3.common.catalog.models.response import Catalog
from cloudcafe.identity.v3.common.users.models.response import User


class AuthResponse(BaseIdentityModel):

    ROOT_TAG = 'token'

    def __init__(
            self, token=None, roles=None, catalog=None, user=None,
            issued_at=None, extras=None, methods=None, project=None,
            expires_at=None, audit_ids=[]):
        super(AuthResponse, self).__init__()

        self.token = token
        self.roles = roles
        self.catalog = catalog
        self.user = user
        self.project = project
        self.issued_at = issued_at
        self.extras = extras
        self.methods = methods
        self.expires_at = expires_at
        self.audit_ids = audit_ids

    @classmethod
    def _dict_to_obj(cls, data):
        if data is None:
            return None

        return cls(
            token=data.get("token"),
            roles=Roles._dict_to_obj(data.get("roles") or []),
            user=User._dict_to_obj(data.get("user")),
            catalog=Catalog._dict_to_obj(data.get("catalog") or []),
            issued_at=data.get("issued_at"),
            extras=data.get("extras"),
            methods=data.get("methods"),
            project=Project._dict_to_obj(data.get("project")),
            expires_at=data.get("expires_at"),
            audit_ids=data.get("audit_ids"))

    @classmethod
    def _json_to_obj(cls, serialized_str):
        data = json.loads(serialized_str)
        return cls._dict_to_obj(data.get("token"))

    def get_service(self, name):
        for service in self.catalog:
            if service.name == name:
                return service
        return None
