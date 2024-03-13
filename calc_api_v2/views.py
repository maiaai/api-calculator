from abc import ABC, abstractmethod
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from calc_api.serializers import CalculatorSerializer


class CalculatorOperation(ABC):
    @abstractmethod
    def execute(self, first_number, second_number):
        pass


class AdditionOperation(CalculatorOperation):
    def execute(self, first_number, second_number):
        return first_number + second_number


class SubtractionOperation(CalculatorOperation):
    def execute(self, first_number, second_number):
        return first_number - second_number


class DivisionOperation(CalculatorOperation):
    def execute(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("You cannot divide by 0.")
        return first_number / second_number


class MultiplicationOperation(CalculatorOperation):
    def execute(self, first_number, second_number):
        return first_number * second_number


class OperatorFactory:
    @staticmethod
    def create_operator(operator):
        if operator == '+':
            return AdditionOperation()
        elif operator == '-':
            return SubtractionOperation()
        elif operator == '/':
            return DivisionOperation()
        elif operator == '*':
            return MultiplicationOperation()
        else:
            raise ValidationError("Invalid operator.")


class Calculator:
    @classmethod
    def calculate(cls, first_number, second_number, operator):
        operation = OperatorFactory.create_operator(operator)
        return operation.execute(first_number, second_number)


class CalculatorAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        message = "Welcome to the Calculator API. Use POST method to perform calculations."
        return Response({"message": message}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CalculatorSerializer(data=request.data)
        if serializer.is_valid():
            try:
                first_number = serializer.validated_data['first_number']
                second_number = serializer.validated_data['second_number']
                operator = serializer.validated_data['operator']
                result = Calculator.calculate(first_number, second_number, operator)
                return Response({"result": result}, status=status.HTTP_200_OK)
            except Exception as e:
                import pdb;pdb.set_trace()
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
