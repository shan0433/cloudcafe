from cloudcafe.identity.v2_0.common.models.base import BaseIdentityModel


class Domain(BaseIdentityModel):

    ROOT_TAG = 'domain'

    def __init__(self, id_=None, name=None):
        super(Domain, self).__init__()
        self.id_ = id_
        self.name = name

    @classmethod
    def _dict_to_obj(cls, data):
        if data is not None:
            return cls(
                id_=data.get('id'),
                name=data.get('name'))
