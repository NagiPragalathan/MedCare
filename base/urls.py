from django.urls import path
from . import views

urlpatterns : list = [
    
    #home
    path('home', views.home ),
    path('', views.home ),
    
    
    #labtest
    path('cart'   , views.cart ),
    path('labtest', views.labtest ),
    path('payment', views.payment ),
    
    #video con
    path('video_consult', views.videocon ),
    
    #surgeries
    path('surgeries', views.surgeries ),
    
    #login
    path('otp', views.otp ),
    path('facebooklogin', views.facebooklogin ),
    path('login', views.login ),
    path('termsCondition', views.termsCondition ),
    path('otpVerify', views.otpVerify ),
    path('signup', views.signup ),
    
    # about us
    path('aboutus', views.about ),
    
    # find docter
    path('find_docter', views.find_docter ),
    path('docter_profile', views.docter_profile ),
    path('contact_us', views.contact_us ),
    path('vitamin', views.vitamin ),
    path('vitamin2', views.vitamin2 ),
    path('vitamin3', views.vitamin3 ),
    path('vitamin4', views.vitamin4 ),
    path('vitamin5', views.vitamin5 ),
    
    #guiding
    path('guiding', views.guiding ),
        
    #chat
    path('chat', views.lobby),
    path('room/', views.room),
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]