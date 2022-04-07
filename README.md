## Instruções de Criação do Projeto
- instalar VirtualEnv no Linux Ubuntu Server:

    `sudo apt install python3-virtualenv`

- instalar VirtualEnv no Windows Desenvolvimento:

    `pip install virtualenv`

## Entrando no ambiente VirtualEnv
    - Criar a pasta com as configurações do virtualenv:

        `virtualenv venv`

    - Entrar no ambiente do virtualenv:

        No Windows: `venv\Scripts\activate.bat`
        No Linux: `source venv/bin/activate`

    - Sair do ambiente Python VirtualEnv:
        
        `deactivate`

    - Apos instalado o recurso de separação de ambientes Python com o VirtualEnd.  Podemos verficar quais recusos instalados para o ambiente:
        
        `pip freeze > requiriments.txt`

## Criando a aplicação Django dentro do VirtualEnv:

    - Instalar o Django:

        `pip install django`
    
    - Criar com o `django-admin` a aplicação:
        
        `django-admin startproject api_django_py_v1`
    
    - Inicializar a aplicação com o `django-admin` (entrar na pasta anterior[api_django_py_v1] antes de executar esse comando):

        `django-admin startapp api`

    - Instalando a biblioteca para APIs Rests:

        `pip install djangorestframework`

    - Comando para criar as migrações default do Django ou migrações personalizadas do arquivo '':
         
        Linux: `python3 manage.py makemigrations`
        Windows Dev: `py manage.py makemigrations`
    
    - Efetuar a migração para criar as tabelas no banco:

        Linux: `python3 manage.py migrate`
        Windows: `py [ou pyth\on] manage.py migrate`
    
    - Criar um super usuario para entrar no painel do Django Adm:

        Linux:  `python3 manage.py createsuperuser`
        Windows:  `py manage.py createsuperuser`
    
    - Rodar em carater de desenvolvimento o servidor interno da aplicação:

        Linux:  `python3 manage.py runserver [IP_SERVICO]:[PORTA]` (exemplo: python3 manage.py runserver localhost:9091)
        Windows:  `py manage.py runserver [IP_SERVICO]:[PORTA]`