from cloudcafe.identity.v2_0.common.models.base import BaseIdentityModel
from cloudcafe.identity.v3.common.domains.models.response import Domain


class Project(BaseIdentityModel):

    def __init__(self, id_=None, name=None, domain=None):
        super(Project, self).__init__()
        self.id = id_
        self.name = name
        self.domain = domain

    @classmethod
    def _dict_to_obj(cls, data):
        if data is None:
            return None
        if 'domain' in data:
            data['domain'] = Domain._dict_to_obj(data.get("domain"))

        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            domain=data.get("domain"))
