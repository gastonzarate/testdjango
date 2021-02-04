"""Loan serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.moni.models import Loan, Gender


class LoanSerializer(serializers.ModelSerializer):
    """Loan model serializer"""
    gender = serializers.SlugRelatedField(queryset=Gender.objects.all(), slug_field='slug_name')
    gender_name = serializers.SerializerMethodField()
    status_name = serializers.SerializerMethodField()

    class Meta:
        """Meta class"""
        model = Loan
        fields = ('id', 'first_name', 'last_name', 'dni', 'gender', 'email',
                  'amount', 'status', 'status_name', 'gender_name')
        read_only_fields = ('status', 'status_name', 'gender_name')

    def get_gender_name(self, obj):
        return obj.gender.name

    def get_status_name(self, obj):
        return obj.get_status_name()

    def validate_dni(self, data):
        """Verify that the dni has a valid length"""
        dni = data
        if len(str(dni)) < 7 or len(str(dni)) > 8:
            raise serializers.ValidationError('El DNI que ingresaste no es válido')
        return data

    def validate_amount(self, data):
        """Verify that the amount is greater than zero"""
        amount = data
        if amount < 1:
            raise serializers.ValidationError('Tengo que prestarte mas que 0')
        if amount > 65000:
            raise serializers.ValidationError('Solo te puedo prestar hasta 65000 pesos')
        return data

    def create(self, data):
        """Create a new Loan and verify that the loan is accepted or not"""
        loan = Loan.objects.create(
            **data
        )
        loan.prescore()

        return loan
