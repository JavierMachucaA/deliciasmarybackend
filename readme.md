Proyect structure
### Application Structure

```
app/
├── requirements.txt
├── __init__.py
├── extensions
│   └── __init__.py
└── modules
    ├── __init__.py
    ├── api
    │   └── __init__.py
    ├── auth
    │   ├── __init__.py
    │   ├── models.py
    │   ├── parameters.py
    │   └── views.py
    ├── users
    │   ├── __init__.py
    │   ├── models.py
    │   ├── parameters.py
    │   ├── permissions.py
    │   ├── resources.py
    │   └── schemas.py
    └── teams
        ├── __init__.py
        ├── models.py
        ├── parameters.py
        ├── resources.py
        └── schemas.py
```

#  DEPENDENCIES
pip install flask
pip install Flask-PyMongo
pip install flask-bcrypt
pip install pyjwt
pip install flask-blueprint
# pip install Flask-Script # not for now

# FOR MORE DETAIL OF DEPENDENCIES READ ´all-dependencies.txt´

´Set up´
pip install virtualenv
py -m venv venv
# if windows
venv\Scripts\activate.bat
# else venv\Scripts\activate
# change file to test NOTE: only "$env:" for powershell if use linux replace for "set " and "export " un cmd
$env:FLASK_APP = "app.py"
# optional
$env:FLASK_ENV="development"
# debug mode
$env:FLASK_DEBUG=1
py -m flask run -p 8080

