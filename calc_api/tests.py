from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestCalculatorViewSet(APITestCase):

    @staticmethod
    def list_url():
        return reverse('calc-list')

    # SUM
    def test_calculate_sum_of_two_positive_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 2,
            "second_number": 3,
            "operator": '+'
        }
        expected_data = {
            'result': 5
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_sum_of_two_negative_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": -2,
            "second_number": -3,
            "operator": '+'
        }
        expected_data = {
            'result': -5
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_calculate_sum_of_integer_and_0(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 2,
            "second_number": 0,
            "operator": '+'
        }
        expected_data = {
            'result': 2
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_calculate_sum_of_negative_integer_and_0(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": -2,
            "second_number": 0,
            "operator": '+'
        }
        expected_data = {
            'result': -2
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_calculate_sum_of_positive_negative_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 2,
            "second_number": -3,
            "operator": '+'
        }
        expected_data = {
            'result': -1
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    # MINUS
    def test_calculate_minus_of_two_possitive_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 2,
            "second_number": 3,
            "operator": '-'
        }
        expected_data = {
            'result': -1
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_calculate_minus_of_two_negative_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": -2,
            "second_number": -3,
            "operator": '-'
        }
        expected_data = {
            'result': 1
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_calculate_minus_of_positive_and_negative_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": -2,
            "second_number": 3,
            "operator": '-'
        }
        expected_data = {
            'result': -5
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

        data = {
            "first_number": -12,
            "second_number": 3,
            "operator": '-'
        }
        expected_data = {
            'result': -15
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_calculate_minus_of_zero_and_integer(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 0,
            "second_number": 3,
            "operator": '-'
        }
        expected_data = {
            'result': -3
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

        data = {
            "first_number": 0,
            "second_number": -3,
            "operator": '-'
        }
        expected_data = {
            'result': 3
        }
        response = self.client.post(self.list_url(), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    # MULTIPLE
    def test_calculate_multiple_of_two_positive_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 2,
            "second_number": 3,
            "operator": '*'
        }
        expected_data = {
            'result': 6
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_multiple_of_two_negative_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": -2,
            "second_number": -3,
            "operator": '*'
        }
        expected_data = {
            'result': 6
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_multiple_of_positive_and_negative_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": -2,
            "second_number": 3,
            "operator": '*'
        }
        expected_data = {
            'result': -6
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_multiple_of_zero_and_negative_integer(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 0,
            "second_number": -3,
            "operator": '*'
        }
        expected_data = {
            'result': 0
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_multiple_of_zero_and_positive_integer(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 0,
            "second_number": 3,
            "operator": '*'
        }
        expected_data = {
            'result': 0
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_multiple_of_1_and_negative_integer(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 1,
            "second_number": -3,
            "operator": '*'
        }
        expected_data = {
            'result': -3
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    # DIVIDE
    def test_calculate_divide_of_zero_and_integer(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 0,
            "second_number": -3,
            "operator": '/'
        }
        expected_data = {
            'result': 0
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_divide_with_zero(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 10,
            "second_number": 0,
            "operator": '/'
        }
        expected_data = {
            'result': 'You can not divide with 0.'
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_divide_same_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": 10,
            "second_number": 10,
            "operator": '/'
        }
        expected_data = {
            'result': 1
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_divide_negative_integers(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": -10,
            "second_number": -3,
            "operator": '/'
        }
        expected_data = {
            'result': 3.3333333333333335
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)

    def test_calculate_divide_with_1(self):
        response = self.client.post(self.list_url())
        data = {
            "first_number": -10,
            "second_number": 1,
            "operator": '/'
        }
        expected_data = {
            'result': -10
        }
        response = self.client.post(self.list_url(), data=data)
        actual_data = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, actual_data)
