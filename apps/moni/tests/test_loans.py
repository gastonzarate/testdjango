"""Loans tests."""

# Django
from django.test import TestCase
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from apps.moni.models import Loan, Gender
from apps.users.models import User
from rest_framework.authtoken.models import Token


class LoansTestCase(TestCase):
    """Loans test case."""
    fixtures = ["genders.json"]

    def setUp(self):
        """Test case setup."""
        self.loan = Loan.objects.create(
            first_name="Agustina",
            last_name="Nekop",
            dni=41000000,
            gender=Gender.objects.get(slug_name="F"),
            email="agustina.n195@gmail.com",
            amount=25000,
        )

    def test_prescore(self):
        """I test state change when preescore is called."""
        self.loan.prescore()
        self.assertGreater(self.loan.status, 0)


class LoansAPITestCase(APITestCase):
    """Loans API test case."""
    fixtures = ["genders.json"]

    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create(
            first_name='Gonzalo',
            last_name='Zarate',
            email='gonzalo.z195@gmail.com',
            username='gonzalo.z195@gmail.com',
            password='admin123'
        )

        self.loan = Loan.objects.create(
            first_name="Agustina",
            last_name="Nekop",
            dni=41000000,
            gender=Gender.objects.get(slug_name="F"),
            email="agustina.n195@gmail.com",
            amount=25000,
        )

        # Auth
        self.token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))

        # URLs
        self.url = reverse('moni:loans-list')
        self.url_detail = reverse('moni:loans-detail', kwargs={'pk': self.loan.id})

    def test_response_success(self):
        """Verify request succeed."""
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_loan_creation(self):
        """Verify loans are generated if none exist previously."""
        # Loans in DB must be 1
        self.assertEqual(Loan.objects.count(), 1)

        # Call loan create URL
        request = self.client.post(self.url, data={
            "first_name": "Fulano",
            "last_name": "Detal",
            "dni": 30900000,
            "gender": "M",
            "email": "fulano.detal@gmail.com",
            "amount": 20000
        })
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        # Loans in DB must be 2
        self.assertEqual(Loan.objects.count(), 2)

    def test_loan_update(self):
        """Verify loans are updated."""
        # Call loan update URL
        first_name = "Mengano"
        last_name = "Decualquier"
        dni = 29000000
        gender = "M"
        email = "mengano.decualquier@gmail.com"
        amount = 30000
        request = self.client.put(self.url_detail, data={
            "first_name": first_name,
            "last_name": last_name,
            "dni": dni,
            "gender": gender,
            "email": email,
            "amount": amount
        })
        response = request.data
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response['first_name'], first_name)
        self.assertEqual(response['last_name'], last_name)
        self.assertEqual(response['dni'], dni)
        self.assertEqual(response['gender'], gender)
        self.assertEqual(response['email'], email)
        self.assertEqual(response['amount'], amount)

    def test_loan_delete(self):
        """Verify loans are deleted."""
        count_loans = Loan.objects.count()
        request = self.client.delete(self.url_detail)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(count_loans-1, Loan.objects.count())
