from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from calc_api.serializers import CalculatorSerializer


class CalculatorViewSet(viewsets.ViewSet):
    serializer_class = CalculatorSerializer
    permission_classes = [AllowAny,]

    def create(self, request):
        serializer = CalculatorSerializer(data=request.data)

        if serializer.is_valid():
            first_number = serializer.validated_data['first_number']
            second_number = serializer.validated_data['second_number']
            operator = serializer.validated_data['operator']

            if str(operator) not in ['+', '-', '/', '*']:
                raise ValidationError("Invalid operator.")
            if operator == '+':
                result = first_number + second_number
            elif operator == '-':
                result = first_number - second_number
            elif operator == '/':
                try:
                    result = first_number / second_number
                except ZeroDivisionError:
                    result = "You can not divide with 0."
            else:
                result = first_number * second_number

            return Response({"result": result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)