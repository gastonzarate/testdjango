"""Loan Model"""
# Utils
import requests

# Django
from django.db import models
from django.conf import settings

# Utils
from apps.utils.models import BaseModel


STATUS_WAITING = 0
STATUS_ACCEPTED = 1
STATUS_REJECTED = 2
STATUS_ERROR = 3

STATUS_CHOICES = (
    (STATUS_WAITING, 'En espera'),
    (STATUS_ACCEPTED, 'Aceptado'),
    (STATUS_REJECTED, 'Rechazado'),
    (STATUS_ERROR, 'Error'),
)


class Loan(BaseModel):
    dni = models.IntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    gender = models.ForeignKey(
        'moni.Gender',
        on_delete=models.CASCADE
    )
    email = models.EmailField()
    amount = models.FloatField()
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_WAITING
    )

    def __str__(self):
        return '{} {} DNI {} {} {} ${} {}'.format(
            self.first_name,
            self.last_name,
            self.dni,
            self.gender,
            self.email,
            self.amount,
            self.get_status_name())

    def prescore(self):
        url = '{}{}'.format(settings.MONI_PRESCORE_URL, self.dni)
        header = {
            'credential': settings.MONI_CREDENTIAL
        }
        request = requests.get(url, headers=header)
        response = request.json()
        if response['has_error']:
            self.status = STATUS_ERROR
        elif response['status'] == 'approve':
            self.status = STATUS_ACCEPTED
        else:
            self.status = STATUS_REJECTED
        self.save()

    def get_status_name(self):
        return STATUS_CHOICES[self.status]
