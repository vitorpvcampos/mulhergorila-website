# Mulher Gorila Website
## Projeto para o site da Mulher Gorila desenvolvido em Python e Django.

[![Build Status](https://travis-ci.org/tiagocordeiro/mulhergorila-website.svg?branch=master)](https://travis-ci.org/tiagocordeiro/mulhergorila-website)
[![Updates](https://pyup.io/repos/github/tiagocordeiro/mulhergorila-website/shield.svg)](https://pyup.io/repos/github/tiagocordeiro/mulhergorila-website/)
[![Python 3](https://pyup.io/repos/github/tiagocordeiro/mulhergorila-website/python-3-shield.svg)](https://pyup.io/repos/github/tiagocordeiro/mulhergorila-website/)
[![codecov](https://codecov.io/gh/tiagocordeiro/mulhergorila-website/branch/master/graph/badge.svg)](https://codecov.io/gh/tiagocordeiro/mulhergorila-website)
[![Python 3.8.1](https://img.shields.io/badge/python-3.8.1-blue.svg)](https://www.python.org/downloads/release/python-381/)
[![Django 2.2.9](https://img.shields.io/badge/django-2.2.9-blue.svg)](https://www.djangoproject.com/download/)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/tiagocordeiro/mulhergorila-website/blob/master/LICENSE)


### Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/tiagocordeiro/mulhergorila-website.git
cd mulhergorila-website
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

### Testes

##### Rode os testes
```
python manage.py test -v 2
```
ou
```
coverage run manage.py test -v 2
coverage hmtl
```
para relatório de cobertura de testes.

#### Code style and PEP8 Tests
```
pycodestyle .
flake8 .
```