from cloudcafe.identity.v2_0.common.models.base import (
    BaseIdentityModel, BaseIdentityListModel)


class Roles(BaseIdentityListModel):

    @classmethod
    def _dict_to_obj(cls, data):
        roles = cls()
        for role in data:
            roles.append(Role._dict_to_obj(role))
        return roles

    @classmethod
    def _xml_ele_to_obj(cls, elements):
        return Roles(
            [Role._xml_ele_to_obj(element) for element in elements])


class Role(BaseIdentityModel):

    NS_PREFIX = 'RAX-AUTH'

    def __init__(self, id_=None, name=None, tenant_id=None):
        super(Role, self).__init__()
        self.id_ = id_
        self.name = name
        self.tenant_id = tenant_id

    @classmethod
    def _xml_ele_to_obj(cls, element):
        if element is None:
            return None
        return cls(
            id_=element.attrib.get("id"),
            name=element.attrib.get("name"))

    @classmethod
    def _dict_to_obj(cls, data):
        if data is None:
            return None
        data = cls._remove_prefix(prefix=cls.NS_PREFIX, data_dict=data)
        return cls(
            id_=data.get("id"), name=data.get("name"),
            tenant_id=data.get("tenant_id"))
