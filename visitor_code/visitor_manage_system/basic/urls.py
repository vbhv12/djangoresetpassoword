from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),

    path('host/',views.host,name='host'),
    path('host/<str:pk>',views.hostdynamic,name='hostdynamic'),
    path('create_host/',views.createhost,name='createhost'),
    path('update_host/<str:pk>',views.updateHost,name='updatehost'),
    path('delete_host/<str:pk>',views.deleteHost,name='deletehost'),


    path('visitor/',views.visitor,name='visitor'),
    path('create_visitor/',views.createvisitor,name='createvisitor'),
    path('update_visitor/<str:pk>',views.updatevisitor,name='updatevisitor'),
    path('delete_visitor/<str:pk>',views.deletevisitor,name='deletevisitor'),


    path('visitentry/',views.visitdetails,name='visitdetails'),

    path('eventvisitor/',views.eventvisitor,name='eventvisitor'),
    path('events/',views.events,name= 'events'),

    

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="basic/reset_password.html"),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="basic/password_reset_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="basic/password_reset_form.html"),name="password_reset_confirm"),
    
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="basic/password_reset_done.html"),name="password_reset_complete")
   

]