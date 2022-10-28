from django.urls import path

from . import views
urlpatterns = [
                path('registration',views.registration,name="registration"),
                path('login',views.login,name="login"),

                path('login/new_form/', views.new_form, name="new_form"),
                path('logout',views.logout,name="logout"),
               # path('login/new_form/msgAlert', views.msgAlert, name="msgAlert"),

]