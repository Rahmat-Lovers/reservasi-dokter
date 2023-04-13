from django.http import HttpRequest
from django.conf import settings
from django.forms import model_to_dict
from ninja import NinjaAPI
from ninja.security import APIKeyHeader
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import transaction
from main.models import Customer, Doctor, Schedule, Specialist
from ninja.errors import ValidationError as NinjaValidationError
from main.decorators import check_error
from main.schemas import RegisterSchema, LoginSchema, CreateScheduleSchema,\
    EditMeSchema, EditMeDoctorSchema, SpecialistInputSchema
from main.forms import RegisterForm, CreateScheduleForm
from main.eth import contract
import jwt, time

class Auth(APIKeyHeader):
    param_name = 'Authorization'

    def authenticate(self, request: HttpRequest, token: str):
        if not token or not token.startswith('Bearer '):
            return

        try:
            token = token.removeprefix('Bearer').strip()
            data = jwt.decode(token, settings.SECRET_KEY, algorithms = ['HS256'])
            return User.objects.get(id = data['user'])
        except:
            return
        
class CheckAuth(APIKeyHeader):
    param_name = 'Authorization'

    def authenticate(self, request: HttpRequest, token: str):
        if not token or not token.startswith('Bearer '):
            return

        try:
            token = token.removeprefix('Bearer').strip()
            data = jwt.decode(token, settings.SECRET_KEY, algorithms = ['HS256'])
            return data
        except:
            return

api = NinjaAPI(auth = Auth())

@api.get('/me')
def me(request: HttpRequest):
    customer = Customer.objects.filter(user__id = request.auth.id).first()
    doctor = Doctor.objects.filter(customer__id = customer.id).first()

    try:
        photo = customer.photo.url
    except:
        photo = None

    data =  {
        'data': {
            'id': customer.id,
            'user': {
                'id': customer.user.id,
                'username': customer.user.username,
            },
            'name': customer.name,
            'gender': customer.gender,
            'photo': photo,
            'address': customer.address,
            'birthday': customer.birthday,
        }
    }
    
    if doctor:
        data['data']['doctor'] = {
            'id': doctor.id,
            'schedule': doctor.schedule,
            'specialist': list(doctor.specialist.all().values()),
            'experience_since': doctor.experience_since
        }
    
    return data


@api.put('/me')
def editMe(request: HttpRequest, payload: EditMeSchema):
    kwargs = {}
    for k, v in payload.dict().items():
        if not v is None:
            kwargs[k] = v

    if Customer.objects.filter(user__id = request.auth.id).update(**kwargs):
        return {'success':True}
    
    return {'success':False}

@api.put('/me/doctor')
def editDoctorMe(request: HttpRequest, payload: EditMeDoctorSchema):
    kwargs = {}
    for k, v in payload.dict().items():
        if not v is None:
            kwargs[k] = v

    if Doctor.objects.filter(customer__user__id = request.auth.id).update(**kwargs):
        return {'success':True}
    
    return {'success':False}

@api.post('/me/doctor/specialist')
def addDoctorSpecialist(request: HttpRequest, payload: SpecialistInputSchema):
    doctor = Doctor.objects.filter(customer__user__id = request.auth.id).first()
    specialist = Specialist.objects.filter(id = payload.id).first()

    if not doctor or not specialist:
        return {'success':False}
    
    doctor.specialist.add(specialist)
    return {'success':True}

@api.delete('/me/doctor/specialist')
def addDoctorSpecialist(request: HttpRequest, payload: SpecialistInputSchema):
    doctor = Doctor.objects.filter(customer__user__id = request.auth.id).first()
    specialist = Specialist.objects.filter(id = payload.id).first()

    if not doctor or not specialist:
        return {'success':False}
    
    doctor.specialist.remove(specialist)
    return {'success':True}


@api.get('/specialist', auth = None)
def specialist(request: HttpRequest):
    return {
        'data': list(Specialist.objects.all().values())
    }

@api.post('/login', auth = None)
def login(request, payload: LoginSchema):
    user = authenticate(username = payload.username, password = payload.password)
    if not user:
        raise NinjaValidationError([{'login':'username / password salah'}])

    return {
        'data': {
            'token': jwt.encode({'user': user.pk, 'exp': int(time.time()) + 3600 * 24 * 7}, settings.SECRET_KEY, algorithm = 'HS256')
        }
    }

@api.get('/loged', auth = CheckAuth())
def login(request):
    return {'loged':True}


@api.post('/register', auth = None)
@check_error(RegisterForm)
def register(request: HttpRequest, payload: RegisterSchema):
    with transaction.atomic():
        user = User(username = payload.username)
        user.set_password(payload.password)
        user.save()

        customer = Customer(
            user_id = user.id,
            name = payload.name,
            gender = payload.gender,
            birthday = payload.birthday,
            photo = payload.photo
        )
        customer.save()
        return {'success': True}

@api.get('/doctors')
def doctors(request: HttpRequest, query: str = None, specialist: int = None):
    queryset = Doctor.objects.all()
    logedCustomer = Customer.objects.get(user__id = request.auth.id)

    if specialist:
        queryset = queryset.filter(specialist__id = specialist)

    if not query:
        queryset = queryset.order_by('?')[:10]
    else:
        queryset = queryset.filter(
            Q(customer__name__contains = query) |
            Q(bio__contains = query) |
            Q(specialist__name__contains = query)
        )

    rv = []
    for x in queryset:
        keren = model_to_dict(x)

        customer = x.customer
        try:
            photo = customer.photo.url
        except:
            photo = None
    
        keren['customer'] = {
            'name': customer.name,
            'photo': photo,
            'gender': customer.gender,
            'birthday': customer.birthday,
        }

        keren['specialist'] = list(x.specialist.values())
        keren['followed'] = x.id in [y.id for y in logedCustomer.followed.all()]

        rv.append(keren)

    return {
        'data': rv
    }

@api.get('/doctor/{doctor_id}')
def doctor(request: HttpRequest, doctor_id: int):
    doctor = Doctor.objects.filter(id = doctor_id).first()
    logedCustomer = Customer.objects.get(user__id = request.auth.id)
    if not doctor:
        raise NinjaValidationError([{'doctor_id':'not found'}])

    keren = model_to_dict(doctor)
    
    customer = doctor.customer
    try:
        photo = customer.photo.url
    except:
        photo = None
    
    keren['customer'] = {
        'name': customer.name,
        'photo': photo,
        'gender': customer.gender,
        'birthday': customer.birthday,
    }

    keren['specialist'] = list(doctor.specialist.values())

    keren['followed'] = doctor.id in [y.id for y in logedCustomer.followed.all()]
    return keren

@api.post('/follow/{doctor_id}')
def doctor(request: HttpRequest, doctor_id: int):
    doctor = Doctor.objects.filter(id = doctor_id).first()
    if not doctor:
        raise NinjaValidationError([{'doctor_id':'not found'}])
    
    customer = Customer.objects.filter(user__id = request.auth.id).first()
    if customer:
        customer.followed.add(doctor)
        return {'success':True}
    
@api.delete('/follow/{doctor_id}')
def doctor(request: HttpRequest, doctor_id: int):
    doctor = Doctor.objects.filter(id = doctor_id).first()
    if not doctor:
        raise NinjaValidationError([{'doctor_id':'not found'}])
    
    customer = Customer.objects.filter(user__id = request.auth.id).first()
    if customer:
        customer.followed.remove(doctor)
        return {'success':True}

@api.post('/schedule')
@check_error(CreateScheduleForm)
def createSchedule(request: HttpRequest, payload: CreateScheduleSchema):
    schedule = Schedule(
        patient_id = request.auth.id,
        doctor_id = payload.doctor_id
    )
    schedule.save()

    return {
        'data': model_to_dict(schedule)
    }

@api.get('/schedule')
def getAllSchedule(request: HttpRequest, doctor: bool = False):
    kwargs = {'patient__id':request.auth.id}
    if doctor:
        kwargs = {'doctor__id':request.auth.id}

    schedules = list(Schedule.objects.filter(**kwargs).values())
    return {
        'data': schedules
    }

@api.get('/schedule/{schedule_id}')
def getSchedule(request: HttpRequest, schedule_id: int, doctor: bool = False):
    kwargs = {'patient__id':request.auth.id}
    if doctor:
        kwargs = {'doctor__id':request.auth.id}

    kwargs['id'] = schedule_id

    schedule = Schedule.objects.filter(**kwargs).first()
    if not schedule:
        raise NinjaValidationError([{'schedule_id':'not found'}])

    return {
        'data': model_to_dict(schedule)
    }

@api.post('/schedule/{schedule_id}/pay')
def paySchedule(request: HttpRequest, schedule_id: int):
    schedule = Schedule.objects.filter(patient__id = request.auth.id, id = schedule_id).\
        filter(status = Schedule.StatusChoices.NOT_YET_PAID).first()
    if not schedule:
        raise NinjaValidationError([{'schedule_id':'not found'}])
    
    transaction = contract.functions.getTransaction(str(schedule_id)).call()
    if transaction[-1] == 'payed':
        schedule.status = Schedule.StatusChoices.PAID
        schedule.save()
        return {'success':True}
    
    return {'success':False}

@api.post('/schedule/{schedule_id}/confirm')
def confirmSchedule(request: HttpRequest, schedule_id: int):
    schedule = Schedule.objects.filter(patient__id = request.auth.id, id = schedule_id).\
        filter(status = Schedule.StatusChoices.PAID).first()
    if not schedule:
        raise NinjaValidationError([{'schedule_id':'not found'}])
    
    transaction = contract.functions.getTransaction(str(schedule_id)).call()
    if transaction[-1] == 'sent_to_seller':
        schedule.status = Schedule.StatusChoices.COMPLETE
        schedule.save()
        return {'success':True}
    
    return {'success':False}

@api.post('/schedule/{schedule_id}/cancel')
def cancelSchedule(request: HttpRequest, schedule_id: int):
    schedule = Schedule.objects.filter(doctor__id = request.auth.id, id = schedule_id).\
        filter(
            Q(status = Schedule.StatusChoices.PAID) |
            Q(status = Schedule.StatusChoices.COMPLETE)
        ).first()
    if not schedule:
        raise NinjaValidationError([{'schedule_id':'not found'}])
    
    transaction = contract.functions.getTransaction(str(schedule_id)).call()
    if transaction[-1] == 'sent_to_buyer':
        schedule.status = Schedule.StatusChoices.CANCEL
        schedule.save()
        return {'success':True}
    
    return {'success':False}

