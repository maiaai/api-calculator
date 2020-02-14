from rest_framework import serializers

OPERATION_CHOICES = [
    ('+', 'Add'),
    ('-', 'Minus'),
    ('*', 'Multiple'),
    ('/', "Divide")
]


class CalculatorSerializer(serializers.Serializer):
    first_number = serializers.IntegerField(required=True)
    second_number = serializers.IntegerField(required=True)
    operator = serializers.ChoiceField(choices=OPERATION_CHOICES)
    result = serializers.IntegerField(read_only=True)
