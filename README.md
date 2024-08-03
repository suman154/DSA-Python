# JWT Authentication with Django REST Framework


This repository demonstrates how to implement JWT (JSON Web Token) authentication in a Django REST Framework application. JWT authentication is a popular method for securing APIs, providing a robust and stateless way to manage user authentication.



# Installation

* Clone the repository:
```sh
git clone https://github.com/your-username/jwt-auth-django.git
cd JWT
```


* Create a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

* Install dependencies:
```sh
pip install -r requirements.txt
```

* Run database makemigrations & migrate:
```sh
python manage.py makemigrations
python manage.py migrate
```


* Create a superuser:
```sh
python manage.py createsuperuser
```

* Start the development server:
```sh
python manage.py runserver
```
