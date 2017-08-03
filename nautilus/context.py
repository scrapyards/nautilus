from oslo_context import context


class RequestContext(context.RequestContext):

    def __init__(self, project_id=None, client_id=None, overwrite=True,
                 auth_token=None, user=None, tenant=None,
                 domain=None, user_domain=None, project_domain=None,
                 is_admin=False, read_only=False, show_deleted=False,
                 request_id=None, instance_uuid=None, roles=None, **kwargs):

        super(RequestContext, self).__init__(auth_token=auth_token,
                                             user=user, tenant=tenant,
                                             domain=domain,
                                             user_domain=user_domain,
                                             project_domain=project_domain,
                                             is_admin=is_admin,
                                             read_only=read_only,
                                             show_deleted=show_deleted,
                                             request_id=request_id,
                                             roles=roles)

        self.project_id = project_id
        self.client_id = client_id

        if overwrite or not hasattr(context._request_store, 'context'):
            self.update_store

    def update_store(self):
        context._request_store.context = self

    def to_dict(self):
        ctx = super(RequestContext, self).to_dict()
        ctx.update({
            'project_id': self.project_id,
            'client_id': self.client_id
        })
        return ctx
