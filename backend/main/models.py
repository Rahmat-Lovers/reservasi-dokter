from django.db import models

class Customer(models.Model):
    class GenderChoices(models.IntegerChoices):
        MALE = 1, "Laki-laki"
        FEMALE = 2, "Perempuan"

    user = models.OneToOneField('auth.User', on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    gender = models.PositiveSmallIntegerField(choices = GenderChoices.choices)
    birthday = models.DateField(null = True, blank = True)
    photo = models.ImageField(null = True, blank = True)
    address = models.CharField(max_length = 255, null = True, blank = True)
    followed = models.ManyToManyField('main.Doctor', related_name = '+')


class Doctor(models.Model):
    customer = models.OneToOneField('main.Customer', on_delete = models.CASCADE)
    specialist = models.ManyToManyField('main.specialist')
    bio = models.TextField()
    schedule = models.JSONField()
    experience_since = models.DateField()


class Specialist(models.Model):
    name = models.CharField(max_length = 255)


class Schedule(models.Model):
    class StatusChoices(models.IntegerChoices):
        NOT_YET_PAID = 1, 'Belum Dibayar'
        PAID = 2, 'Dibayar'
        PROCCESS = 3, 'Proses'
        COMPLETE = 4, 'Berhasil'
        CANCEL = 5, 'Dibatalkan'   

    doctor = models.ForeignKey('main.Doctor', on_delete = models.CASCADE, related_name = 'a+')
    patient = models.ForeignKey('main.Customer', on_delete = models.CASCADE, related_name = 'a+')
    status = models.PositiveSmallIntegerField(choices = StatusChoices.choices, default = StatusChoices.NOT_YET_PAID)

