# api-calculator

This is simple Calculator API endpoint developed with `Django Rest_Framework` and `Python 3.6.9` 
You can use this API and communicate with your front-end or connect it with some third party app. 
With this API endpoint you can do simple arithmetic operations like `+,-, *, /`.

This endpoint doesn't include authentication because it is intended for simple calculations and 
could be used by anyone.

`POST` is the only allowed method for making requests. Even-though I don't use models, because I don't need anything
stored in the database, I still choose to use `POST` method (taken into consideration future possible extension).
`GET` method could be aslo used.


For use of this API you need to perform next steps:

1. `Create virtualenv with Python 3`
2. `Clone this repo`
3. `Install requirements: pip install -r requirements.txt`

The root url is : `http://localhost:{port}/api/calc`
Use Postman or CURL to make requests.
CURL request: `curl -X POST --data "first_number=2&second_number=3&operator=-" localhost:8000/api/calc/`

NOTE: Most of the test scenarios are covered with Unit tests. Unit tests are not included for serializer because
validations for my simple fields in this case are handled by rest_framework.

Thank you for considering me as a future coleague of yours.