# Microserviço de Perfil
Gerenciamento de perfil

# Getting started

Antes de tudo, você precisa instalar [docker](https://docs.docker.com/install/) e [docker-compose](https://docs.docker.com/compose/install/).

# Rodando a aplicação

Clone o repositório
```bash
$ git clone https://github.com/estudeplus/perfil.git
```

Acesse o diretório principal da aplicação
```bash
$ cd perfil
```
Crie o arquivo .env
```bash
$ touch .env
```

Copie e cole as linhas abaixo no .env
```
POSTGRES_USER=perfilapi
POSTGRES_PASSWORD=perfilapi123
POSTGRES_DB=perfilapi
POSTGRES_HOST=db-perfil
PORT=8000
```

Rode a aplicação

```bash
$ (sudo) docker-compose up
```

And you are good to go! o/
