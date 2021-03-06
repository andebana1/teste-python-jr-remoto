from rest_framework import viewsets, mixins, status
from rest_framework.views import Response

from api import models, serializers, filters
from api.integrations.github import GithubApi

# TODOS:
# 1 - Buscar organização pelo login através da API do Github
# 2 - Armazenar os dados atualizados da organização no banco
# 3 - Retornar corretamente os dados da organização
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API


class OrganizationViewSet(
        GithubApi,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):

    queryset = models.Organization.objects.all().order_by('-score')
    serializer_class = serializers.OrganizationSerializer
    filter_class = filters.OrganizationFilter
    lookup_field = "login"

    def notfound_status(self):
        return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, login=None):
        """
            Busca os dados de uma org através do login informado
        """
        result = self.get_organization(login)
        if result is None:
            return self.notfound_status()
        pub_org_members = self.get_organization_public_members(login)
        obj = {
            "login": result['login'],
            "name": result.get('name', None),
            "score": pub_org_members + result.get('public_repos', 0)
        }
        serializer = self.get_serializer(data=obj, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """
            Listagem de todas as organizações que estão no cache
        """
        return super(OrganizationViewSet, self).list(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        """
            Remove uma organização da listagem
        """
        return super(OrganizationViewSet, self).destroy(request, args, kwargs)
