from django.urls import path
from contact import views

urlpatterns = [
    path('',views.dashboard,name="home"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('register',views.registerUser,name="register"),
    path('contact/<int:pk>/',views.viewContact,name="viewContact"),
    path('createContact',views.createContact,name="createContact"),
    path('updateContact/<int:pk>/',views.updateContact,name="updateContact"),
    path('deleteContact/<int:pk>/',views.deleteContact,name="deleteContact"),
]
