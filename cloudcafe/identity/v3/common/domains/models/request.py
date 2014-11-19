from cloudcafe.identity.v2_0.common.models.base import BaseIdentityModel

class Domain(BaseIdentityModel):

    ROOT_TAG = 'domain'

    def __init__(self, name=None, id_=None):
        super(Domain, self).__init__()
        self.name = name
        self.id_ = id_

    def _obj_to_dict(self):
        ret = {}
        if self.name is not None:
            ret['name'] = self.name
        if self.id_ is not None:
            ret['id'] = self.id_
        return self._remove_empty_values(ret)
