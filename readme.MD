# ErnieApp Testing project
## 1. Dependencies
  - Django
  - Django REST Framework
  - PyTest
  - flake8
  - Postgres
  - Docker
  - Docker Compose

## 2. Project structure
  - There are 4 Django apps
    * account
      Includes custom user model that allows user can input firstname, lastname, email, company, and password
      Has a CREATE API endpoint
    * company
      Includes a simple model that has name field
      Has a CREATE API endpoint
    * menu
      Includes a base menu model, category model, and 2 menu models(food, alcohol) that are inherited from base menu model
      Be able to edit on Django admin panel
      There is no API endpoint regarding the menus.
    * order
      Includes order model
      Has 2 API endpoints that customer can CREATE/EDIT orders
      Customer can create only 1 order per day, per table
      Customer can edit order, but only if they created it to begin with

## 3. Project Installation
  - Prerequiresites 
    * Python
    * docker
    * docker-compose
  - How to run
    * docker compose build
    * docker up app
    * docker run app python manage.py makemigrations
    * docker run app python manage.py createsuperuser
## 4. Endpoints
  - account
    http://localhost:8000/users
  - company
    * Create new company
      http://localhost:8000/company/new
  - order
    http://localhost:8000/order/order
