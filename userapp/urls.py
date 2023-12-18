from django.urls import path
from userapp import views

urlpatterns=[
    path('homepage_fn/', views.homepage_fn, name='homepage_fn'),
    path('registration_fn/',views.registration_fn,name='registration_fn'),
    path('saveregistrationdata/',views.saveregistrationdata,name='saveregistrationdata'),
     path('signup_fn/',views.signup_fn,name='signup_fn'),
     path('userlogout/',views.userlogout,name='userlogout'),
    path('contactpage/',views.contactpage,name='contactpage'),
    path('hotelbooking/',views.hotelbooking,name='hotelbooking'),
    path('destination_page/',views.destination_page,name='destination_page'),
    path('singledest_fn/<int:dataid>',views.singledest_fn,name='singledest_fn'),


    path('booking_fn/',views.booking_fn,name='booking_fn'),
    path('savebooking/',views.savebooking,name='savebooking'),
    path('displaybook_fn/',views.displaybook_fn,name='displaybook_fn'),
    path('deletebooking/<int:dataid>/',views.deletebooking,name='deletebooking'),
    path('feedback_fn/',views.feedback_fn,name='feedback_fn'),
    path('savefeedback/',views.savefeedback,name='savefeedback'),
    path('contact_fn/',views.contact_fn,name='contact_fn'),
    path('history_fn/',views.history_fn,name='history_fn'),




]

