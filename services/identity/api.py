from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from services.identity.models import Identifier


class IdentifierResource(ModelResource):
    class Meta:
        queryset = Identifier.objects.all()
        resource_name = 'identifier'
        excludes = ['id']
        allowed_methods = ['get', 'post']
        authorization = Authorization()
