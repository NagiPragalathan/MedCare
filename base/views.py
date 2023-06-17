from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt


#home
def home(request) -> HTTPResponse:
    """     Home Page     """
    return render(request, "home/home.html")

#labtest
def cart(request) -> HTTPResponse:
    return render(request, "labtest/cart.html")

def labtest(request) -> HTTPResponse:
    return render(request, "labtest/labtest.html")

def payment(request) -> HTTPResponse:
    return render(request, "labtest/payment.html")



#video consult
def videocon(request) -> HTTPResponse:
    return render(request, "videocon/videocon.html")


#surgeries
def surgeries(request) -> HTTPResponse:
    return render(request, "surgeries/surgeries.html")


#login or signup
def login(request) -> HTTPResponse:
    return render(request, "login/login.html")

def signup(request) -> HTTPResponse:
    return render(request, "login/signup.html")

def otp(request) -> HTTPResponse:
    return render(request, "login/otp.html")

def otpVerify(request) -> HTTPResponse:
    return render(request, "login/otpVerify.html")

def termsCondition(request) -> HTTPResponse:
    return render(request, "login/termsCondition.html")

def facebooklogin(request) -> HTTPResponse:
    return render(request, "login/facebooklogin.html")



# video or text chat
def lobby(request) -> HTTPResponse:
    return render(request, 'base/lobby.html')

def room(request) -> HTTPResponse:
    return render(request, 'base/room.html')

def getToken(request) -> HTTPResponse:
    appId = "6c195af2970e48579689b47d0debf9ca"
    appCertificate = "acb5f43b05c74985aec64f691cf4311c"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)

@csrf_exempt
def createMember(request) -> HTTPResponse:
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)

def getMember(request) -> HTTPResponse:
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request) -> HTTPResponse:
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)


# AboutUs

def about(request) -> HTTPResponse:
    return render(request, "AboutUs/AboutUs.html")


# find docter

def find_docter(request) -> HTTPResponse:
    return render(request, "find_docter/finddoctor.html")

def docter_profile(request) -> HTTPResponse:
    return render(request, "find_docter/doctor_profile.html")

def contact_us(request) -> HTTPResponse:
    return render(request, "find_docter/contact_us.html")

def vitamin(request) -> HTTPResponse:
    return render(request, "find_docter/vitamin.html")

def vitamin2(request) -> HTTPResponse:
    return render(request, "find_docter/vitamin2.html")

def vitamin3(request) -> HTTPResponse:
    return render(request, "find_docter/vitamin3.html")

def vitamin4(request) -> HTTPResponse:
    return render(request, "find_docter/vitamin4.html")

def vitamin5(request) -> HTTPResponse:
    return render(request, "find_docter/vitamin5.html")


# guiding
def guiding(request) -> HTTPResponse:
    return render(request, "guiding/guiding.html")


