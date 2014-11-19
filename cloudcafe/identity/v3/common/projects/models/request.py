from cloudcafe.identity.v2_0.common.models.base import BaseIdentityModel
from cloudcafe.identity.v3.common.domains.models.request import Domain


class Project(BaseIdentityModel):

    def __init__(self, id_=None, name=None, project_domain_name=None,
                 project_domain_id=None,):
        super(Project, self).__init__()

        self.id_ = id_
        self.name = name
        self.project_domain_id = project_domain_id
        self.project_domain_name = project_domain_name
        self.domain = Domain(name=self.project_domain_name,
                             id_=self.project_domain_id)._obj_to_dict()

    def _obj_to_dict(self):
        ret = {}
        if self.id_ is not None:
            ret['id'] = self.id_
        if self.name is not None:
            ret['name'] = self.name
        if self.project_domain_id is not None:
            ret['domain'] = dict(self.domain)
        if self.project_domain_name is not None:
            ret['domain'] = dict(self.domain)
        return self._remove_empty_values(ret)
