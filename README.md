# Teste Técnico Desenvolvedor(a) Python Júnior [REMOTO]

Este repositório contém uma solução para o problema apresentado no repositório da [Instruct](https://github.com/instruct-br/teste-python-jr-remoto).

## Sobre o problema
A companhia de marketing Vough tem trabalhado cada vez mais para empresas de tecnologia que disponibilizam código aberto.

Com o aumento das demandas surgiu a necessidade de rankear seus atuais e potenciais clientes por um nível de prioridade, de modo a dar preferência a projetos de empresas maiores e mais influentes no meio open source.

## Solução

Para auxiliar a Vough, foi desenvolvida uma API que calcula o valor de prioridade de cada cliente e retorna uma lista de clientes ordenandos por prioridade.

Na API, o valor de prioridade é calculado com base em dados encontrados no Github, através da seguinte fórmula:

`prioridade = <quantidade de membros públicos da organização no Github> + <quantidade de repositórios públicos da organização no Github>`

A API foi desenvolvida de acordo com alguns requisitos técnicos:

- Deve utilizar a [API Rest do Github](https://docs.github.com/pt/free-pro-team@latest/rest) para coletar as informações referentes às organizações.

- Deve possuir um endpoint para consultar uma organização específica através do nome (`login`):

```
GET /api/orgs/<login>/
```

Esse endpoint deverá apresentar os dados no seguinte formato:

```
{
    "login": "string",
    "name": "string",
    "score": int
}
```

Onde o `score` é o nível de prioridade da organização.
Em caso de sucesso, o status `200` deverá ser retornado.
Caso a empresa não seja encontrada, deve retornar o status `404`.

- Deve possuir um endpoint para a listagem de todas as organizações já consultadas através da API:

```
GET /api/orgs/
```

Esse endpoint deverá apresentar os dados no seguinte formato:

```
[
  {
    "login": "string",
    "name": "string",
    "score": int
  },
  {
    "login": "string",
    "name": "string",
    "score": int
  },
  ...
]
```

As organizações listadas aqui devem estar ordenadas pela prioridade (`score`), da maior para a menor.

- Deve possuir um endpoint para a remoção de organizações da listagem:

```
DELETE /api/orgs/<login>/
```

Em caso de sucesso, o status `204` deverá ser retornado.
Caso a empresa não seja encontrada, deve retornar o status `404`.

## Instruções de uso

O projeto foi desenvolvido utilizando o [Pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today) como o gerenciador de dependências. Depois de instalado, siga os seguintes passos:
- Clone o projeto para o seu computados
- Acesse a pasta ```vough_backend``` do projeto, e execute o comando ```pipenv shell```que irá ativar (ou criar, caso não exita) um ambiente virtual para o projeto em específico.
- Com o ambiente ativo, execute ```pipenv install```que todos as dependências informadas no ```Pipfile``` serão instaladas (use python mais recente, ou uma versão superior a 3.7).
- instaladas todas as dependências, aplicar as migrações do Django antes de começar a executar o projeto, para isso, execute ```pipenv run python manage.py migrate``` (as migrations já estão no repositório, por isso, não há necessidade de usar o makemigrations). Por ser um projeto simples, resolvel-se utilizar do sqlite3.
- (Opcional) Caso queira executa os testes automatizados do projeto, basta executar ```pipenv run python manage.py test```.
- Aplicadas todas as migrações, para iniciar o servidor da aplicação, execute ```pipenv run python manage.py runserver``` e os endpoints já estarão acessíveis. 
- A documentação dos endpoints poderá ser consultada através do seguinte endpoint:
```
/docs/
```
ou
```
/raw-docs/
```

A endereço da aplicação com o deploy no heroku pode ser encontrada em:

 - [https://teste-python-jr-anderson.herokuapp.com/](https://teste-python-jr-anderson.herokuapp.com/)

Existe, na raiz do projeto, um arquivo chamado ```tests-open.js``` que contém alguns teste para avaliar a aplicação. 

Você pode executar esses testes com o [k6](https://k6.io/). Para instalar o k6 basta [baixar o binário](https://github.com/loadimpact/k6/releases) para o seu sistema operacional (Windows, Linux ou Mac).

E para rodar os testes abertos, especifique a variável de ambiente "API_BASE" com o endereço base da API testada.

Exemplo de aplicação rodando no localhost na porta 8000:
`k6 run -e API_BASE='http://localhost:8000/' tests-open.js` ou `k6 run -e API_BASE='https://teste-python-jr-anderson.herokuapp.com/' tests-open.js` (no windows, caso ocorra algum erro, tente retirar as aspas do valor de API_BASe, deixo como ```API_BASE=http://localhost:8000/```.

 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
