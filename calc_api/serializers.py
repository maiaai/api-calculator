from rest_framework import serializers

OPERATION_CHOICES = [
    ('+', 'Add'),
    ('-', 'Minus'),
    ('*', 'Multiple'),
    ('/', "Divide")
]


class CalculatorSerializer(serializers.Serializer):
    """
    Serializer for performing arithmetic calculations.
    """
    first_number = serializers.IntegerField(required=True, help_text="First number for the operation.")
    second_number = serializers.IntegerField(required=True, help_text="Second number for the operation.")
    operator = serializers.ChoiceField(choices=OPERATION_CHOICES, help_text="Operator for the operation.")
    result = serializers.IntegerField(read_only=True, help_text="Result of the operation.")

    def validate(self, data):
        """
        Additional validation to ensure that division operation doesn't result in division by zero.
        """
        if data['operator'] == '/' and data['second_number'] == 0:
            raise serializers.ValidationError("Cannot divide by zero.")
        return data
