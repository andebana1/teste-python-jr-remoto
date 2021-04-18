from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from operator import itemgetter
from api import models
from api import serializers
from api.integrations import github
# Create your tests here.

client = Client()


class OrgsTests(github.GithubApi, TestCase):

    def setUp(self):
        result = self.get_ramdom_orgs()
        for i in result[:10]:
            client.get(reverse('orgs-detail', kwargs={'login': i['login']}))
        pass

    def test_get_all_orgs(self):
        # Get API Response
        response = client.get(reverse('orgs-list'))
        # Get data from DB
        orgs = models.Organization.objects.all().order_by('-score')
        serializer = serializers.OrganizationSerializer(orgs, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(
            response.data,
            sorted(response.data, key=itemgetter('score'), reverse=True))

    def test_get_org(self):
        orgs = models.Organization.objects.filter(login="instruct-br")
        self.assertFalse(orgs)  # garante que a org não está no cache
        response = client.get(
            reverse('orgs-detail', kwargs={'login': 'instruct-br'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        orgs = models.Organization.objects.filter(login="instruct-br")
        self.assertTrue(orgs)  # checa se a org foi para o cache após o get

    def test_delete_org(self):
        response = client.delete(
            reverse('orgs-detail', kwargs={'login': 'tensorflow'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_get = client.get(
            reverse('orgs-detail', kwargs={'login': 'tensorflow'}))
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        response_del = client.delete(
            reverse('orgs-detail', kwargs={'login': 'tensorflow'}))
        self.assertEqual(response_del.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_method(self):
        reponse = client.post(reverse('orgs-list'), {})

        self.assertEqual(
            reponse.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED)
