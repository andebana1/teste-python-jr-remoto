import os
import requests
import json
from .. import models

class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "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")

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        headers = {
            "Authorization": "Token {}".format(self.GITHUB_TOKEN)
        }

        url = f'{self.API_URL}/orgs/{login}'

        repo = requests.get(url, headers=headers).json()
        if repo.get('message', None) is not None and repo['message'] == 'Not Found':
            return None
        pub_org_members = requests.get(url + '/public_members', headers=headers).json()
        
        login = repo['login']
        name = repo['name']
        score = len(pub_org_members) + repo['public_repos']

        # t = models.Organization(login, name, score)

        # t.save()

        return {
            "login": login,
            "name": name,
            "score": score
        }

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        return 0
