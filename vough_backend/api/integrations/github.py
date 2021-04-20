import os
import requests


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get(
        "GITHUB_TOKEN",
        "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")

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        headers = {
            "Authorization": "Token {}".format(self.GITHUB_TOKEN)
        }

        url = f'{self.API_URL}/orgs/{login}'

        try:
            repo = requests.get(url, headers=headers)

            if repo.status_code == 404:
                return None
            else:
                repo = repo.json()

            return repo
        except requests.exceptions.ConnectionError:
            return None

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        headers = {
            "Authorization": "Token {}".format(self.GITHUB_TOKEN)
        }
        params = {
            "per_page": 100,
            "page": 0
        }
        pub_org_members = 0

        url = f'{self.API_URL}/orgs/{login}/public_members'

        condition = True
        while condition:

            try:
                params['page'] += 1
                response = requests.get(url, headers=headers, params=params)
                array_len = len(response.json())
                if array_len == 0:
                    condition = False
                    break
                pub_org_members += array_len
            except requests.exceptions.ConnectionError:
                params['page'] -= 1  # Repete a requisição que falhou
            except requests.ConnectionAbortedError:
                params['page'] -= 1

        return pub_org_members

    def get_ramdom_orgs(self):  # for tests
        """
            Retorna algumas orgs aleatórias para que sejam feitos os tests
        """
        headers = {
            "Authorization": "Token {}".format(self.GITHUB_TOKEN)
        }

        try:
            url = f'{self.API_URL}/organizations'
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                return None

            return response.json()
        except requests.exceptions.ConnectionError:
            return None
