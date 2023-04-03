from ninja import Schema
from ninja.files import UploadedFile
from datetime import date
from typing import Optional, Union

class RegisterSchema(Schema):
    username: str
    password: str
    name: str
    gender: int
    birthday: date
    photo: Optional[UploadedFile]

class LoginSchema(Schema):
    username: str
    password: str

class CreateScheduleSchema(Schema):
    # patient_id: int
    doctor_id: int

class EditMeSchema(Schema):
    name: Optional[str]
    gender: Optional[int]
    birthday: Optional[date]
    photo: Optional[UploadedFile]
    address: Optional[str]

class EditMeDoctorSchema(Schema):
    bio: Optional[str]
    schedule: Optional[str]
    experience_since: Optional[date]

class SpecialistInputSchema(Schema):
    id: int