from rest_framework import viewsets, status
from rest_framework.views import Response

from api import models, serializers
from api.integrations.github import GithubApi

# TODOS:
# 1 - Buscar organização pelo login através da API do Github
# 2 - Armazenar os dados atualizados da organização no banco
# 3 - Retornar corretamente os dados da organização
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API


class OrganizationViewSet(GithubApi, viewsets.ModelViewSet):

    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    lookup_field = "login"

    def notfound_status(self):
        return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, login=None):
        result = self.get_organization(login)
        if result is None:
            return self.notfound_status()
        serializer = self.get_serializer(data=result, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def create(self, request, *args, **kwars):
        return self.notfound_status()
    
    def update(self, request, *args, **kwars):
        return self.notfound_status()

    def partial_update(self, request, *args, **kwars):
        return self.notfound_status()