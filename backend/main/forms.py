from django import forms as _forms
from django.core.validators import RegexValidator as _RegexValidator
from django.core.exceptions import ValidationError as _ValidationError
from django.contrib.auth.models import User as _User
from main.models import Customer as _Customer, Doctor as _Doctor

class RegisterForm(_forms.Form):
    username = _forms.CharField(max_length = 15, min_length = 3, validators = [
        _RegexValidator(r'^[a-zA-Z0-9]+$')
    ])
    password = _forms.CharField(max_length = 255, min_length = 6)
    gender = _forms.IntegerField()
    name = _forms.CharField(max_length = 50, min_length = 3, validators = [
        _RegexValidator(r"^[a-zA-Z ]+$")
    ])
    photo = _forms.ImageField(required = False)

    def clean_username(self):
        if _User.objects.filter(username = self.data['username']).exists():
            raise _ValidationError('username sudah terdaftar')

        return self.data['username']

    def clean_gender(self):
        gender = self.data['gender']

        if not gender in [_Customer.GenderChoices.MALE, _Customer.GenderChoices.FEMALE]:
            raise _ValidationError('Jenis kelamin tidak valid')

        return gender

class CreateScheduleForm(_forms.Form):
    doctor_id = _forms.IntegerField()

    def clean_doctor_id(self):
        doctor_id = self.data['doctor_id']
        doctor = _Doctor.objects.filter(id = doctor_id).first()
        if not doctor:
            raise _ValidationError('Doctor tidak ditemukan')

        return doctor_id