# swapidjango



Projeto SwApi em Django

Instalando o projeto:

1) Estabeleça um ambiente virtual dentro do diretório do projeto

```
virtualenv -p python3 venv
```

2) Ative o ambiente virtual

```
source venv/bin/activate
```
3) Instale o projeto

```
pip install -r requirements.txt
```

4) Aplique o modelo de Dados com os comandos abaixo:

```
python3 manage.py makemigrations
```
```
python3 manage.py migrate 
```

5) Inicie a aplicação

```
python3 manage.py runserver 5000
```

6) Rode o init para carregar o banco de dados. Neste momento irá 
acessar a url https://swapi.dev/api para carregar as informações 
e salvar no banco de dados 

```
curl -0 http://localhost:5000/init 
```
OBS: Este projeto necessita que o data--config-server e o secret do django esteja ativado para capturar as configurações.
     Para isto inicie o springboot config server, crie um arquivo chamado ".env" con o conteúdo abaixo:
     
```

SECRET_KEY = django-insecure-9^iuh9#ni^0n!6svqjsh=dk5x6&m9vxzl2gq=v2sm_ew%ls=c^
CONFIG_SERVER_URL = http://localhost:8888/config
NODE_PROFILES_ACTIVE = dev
```
