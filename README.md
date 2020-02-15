# api-calculator

This is simple Calculator API endpoint developed with Django Rest_framework and Python 3.6.9 
You can use this API and communicate with you front-end or connect it with some third party app. 
With this API endpoint you can do simple arithmetic operations (+,-, *, /)

This endpoint doesn't include authentication because it is intended for simple calculation.
POST is the only allowed method. This can be GET also.

As part of the API, django admin site is included.

For use of this API you need to perform next steps:

Create virtualenv with Python 3
Clone this repo
Install requirements: pip install -r requirements.txt
The root url is : "http://localhost:{port}/api/calc"
Use Postman or CURL to make requests.
NOTE: Most of the test scenarios are covered with Unit tests. Unit tests are not included for serializer because
validations for my simple fields in this case are handled by rest_framework.

Thank you for considering me as a future coleague of yours.