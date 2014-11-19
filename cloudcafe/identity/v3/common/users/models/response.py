from cloudcafe.identity.v2_0.common.models.base import BaseIdentityModel
from cloudcafe.identity.v3.common.domains.models.response import Domain


class User(BaseIdentityModel):

    NS_PREFIX = 'RAX-AUTH'

    def __init__(
            self, id_=None, name=None, domain=None,
            default_region=None, default_project_id=None):
        super(User, self).__init__()
        self.id_ = id_
        self.name = name
        self.domain = domain
        self.default_region = default_region
        self.default_project_id = default_project_id

    @classmethod
    def _dict_to_obj(cls, data):
        if data is None:
            return None
        data = cls._remove_prefix(prefix=cls.NS_PREFIX, data_dict=data)
        if 'domain' in data:
            data['domain'] = Domain._dict_to_obj(data.get("domain"))
        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            default_project_id=data.get("default_project_id"),
            default_region=data.get("default_region"),
            domain=data.get("domain"))
