import json

from cloudcafe.identity.v2_0.common.models.base import (
    BaseIdentityModel, BaseIdentityListModel)


class Catalog(BaseIdentityModel):

    ROOT_TAG = 'catalog'

    def __init__(self, catalog=None, links=None):
        super(Catalog, self).__init__()
        self.catalog = catalog
        self.links = links

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls(Catalog._dict_to_obj(json_dict.get("catalog")),
                   Links._dict_to_obj(json_dict.get("links")))

    @classmethod
    def _dict_to_obj(cls, data):
        if data is None:
           return None
        return [Service._dict_to_obj(service) for service in data]


class Links(BaseIdentityModel):

    def __init__(self, self_=None):
        super(Links, self).__init__()
        self.self_ = self_

    @classmethod
    def _dict_to_obj(cls, data):
        if data is None:
            return None
        return Links(self_=data.get("self"))

class Service(BaseIdentityListModel):

    def __init__(self, endpoints=None, type=None):
        super(Service, self).__init__()
        self.endpoints = endpoints
        self.type = type

    @classmethod
    def _dict_to_obj(cls, data):

        if 'type' in data:
            type = data.get("type")

        if Endpoints.ROOT_TAG in data:
            data[Endpoints.ROOT_TAG] = Endpoints._list_to_obj(
                data[Endpoints.ROOT_TAG]).endpoints
        return Service(**data)


class Endpoints(BaseIdentityModel):

    ROOT_TAG = 'endpoints'

    def __init__(self, endpoints=None):
        super(Endpoints, self).__init__()
        self.endpoints = endpoints

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._list_to_obj(json_dict.get(cls.ROOT_TAG))

    @classmethod
    def _list_to_obj(cls, list_):
        ret = {cls.ROOT_TAG: [Endpoint._dict_to_obj(endpoint) for endpoint in list_]}


        return Endpoints(**ret)


class Endpoint(BaseIdentityModel):

    def __init__(self, interface=None, region=None, id=None, url=None):
        super(Endpoint, self).__init__()
        self.interface = interface
        self.region = region
        self.id = id
        self.url = url

    @classmethod
    def _dict_to_obj(cls, data):
        return Endpoint(id=data.get("id"),
                   region=data.get("region"),
                   url=data.get("url"),
                   interface=data.get("interface"))
