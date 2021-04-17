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

        repo = requests.get(url, headers=headers)
        if repo.status_code == 404:
            return None
        else:
            repo = repo.json()
        # pub_org_members = requests.get(url + '/public_members', headers=headers).json()
        
        login = repo['login']
        name = repo['name']
        # score = len(pub_org_members) + repo['public_repos']
        
        return repo

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        headers = {
            "Authorization": "Token {}".format(self.GITHUB_TOKEN)
        }

        url = f'{self.API_URL}/orgs/{login}/public_members'

        pub_org_members = requests.get(url, headers=headers)

        return 0 if pub_org_members.status_code != 200 else len(pub_org_members.json())
