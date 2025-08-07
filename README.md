# Site-de-cadastro-e-login-TCC

Estrutura para execução

- Instalando Framework DJANGO na maquina -
no terminal digite: pip install django.

- Instalando driver do MySQL -
no terminal digite: pip install mysqlclient

- Criando banco no MySQL -
Crie uma tabela usando o seguinte comando: 
CREATE DATABASE cadastro_usuarios CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

- Rodando o servidor -
Execute no terminal o comando: python manage.py runserver

- IMPORTANTE -
Modificação na estrutura do bando de dados executar os seguintes códigos
python manage.py makemigrations
python manage.py migrate