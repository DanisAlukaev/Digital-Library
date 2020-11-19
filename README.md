# Setup the environment
### Backend
- Install Django REST framework:
```
pip install djangorestframework
```
-------------------
- Add Django REST framework to the INSTALLED_APPS array:
```
INSTALLED_APPS = [
    ...
    # Django REST framework 
    'rest_framework',
]
```
----------
- Install CORS for a Rest Api Resource:
```
pip install django-cors-headers
```
----------------
- Add configuration of CORS to the INSTALLED_APPS array:
```
INSTALLED_APPS = [
    ...
    # CORS
    'corsheaders',
]
```
-------------
- Add a middleware class to listen in on responses (CorsMiddleware should be placed as high as possible):
```
MIDDLEWARE = [
    ...
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
```
----------------
- For simplicity, authorize all origins to make cross-site HTTP requests:
```
CORS_ORIGIN_ALLOW_ALL = True
```
------
- Install necessary packages:
```
pip install requirements.txt
```
### Frontend
- Install NodeJS.

-------------
- Install all required libraries:
```
npm install
```
----------
- Install Vue:
```
npm install -g @vue/cli
```
----
- In case you create new Vue project, do not forget to install ```axios```:
```
npm install axios
```
- Import the axios library:
 ```
 import axios from 'axios'
 ```
----------------
- Run a local server for web application (source code in  folder ```frontend```):
```
npm run serve
```
------
[OPTIONAL] : Install Postman to simplify API development.