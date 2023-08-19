# Color-Palettes-Project
## Features
 1. Browse and search color palettes and colors through API endpoints.
 2. Use the Django admin panel to manage color palettes and colors.
 3. Only authenticated user can post or put color palettes.
## Installation
1. Clone or download zip file
```
$ https://github.com/AlSaimun/Color-Palettes-Project.git
```
```
2.  pip install -r requirements.txt
```
```
3.  py manage.py makemigrations
```
```
4.  py manage.py migrate
```
5. Create SuperUser
```
 py manage.py createsuperuser
```
```
6.  py manage.py runserver
```
## API Endpoints
* list of Color palettes ``` http://127.0.0.1:8000/palettes/" ```
* list of Color palettes by user (must be a user) ``` http://127.0.0.1:8000/favorites/ ```
* Search  by name ``` http://127.0.0.1:8000/palettes/?search=name ```

## How to create color palettes in admin site
1. select user
2. Enter name
3. In dominant/accent colors field, enter json format data.

