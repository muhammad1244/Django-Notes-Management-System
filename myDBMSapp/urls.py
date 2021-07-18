from django.contrib import admin
from django.urls import path
from . import views


# Web-Directory/ urls patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name="welcome"),

    path('home/', views.home ,name="home"),

    path('login/', views.login ,name="login"),
    path('logout/', views.logout ,name="logout"),
    path('register/', views.register ,name="register"),

    path('about/', views.about ,name="about"),
    path('contact/<str:pk>/', views.contact ,name="contact"),

    path('adminSite/<str:pk>/', views.adminSite ,name="adminSite"),
    path('userProfile/<str:pk>/', views.userProfile ,name="userProfile"),
    path('userProfileEdit/<str:pk>/', views.userProfileEdit ,name="userProfileEdit"),
    path('userProfileEditAdmin/<str:pk>/', views.userProfileEditAdmin ,name="userProfileEditAdmin"),

    path('delete/<str:pk>/', views.delete ,name="delete"),
    path('deleteUser/<str:pk>/', views.deleteUser ,name="deleteUser"),

    path('updateUserData/<str:pk>/', views.updateUserData ,name="updateUserData"),
    path('updateUserDataAdmin/<str:pk>/', views.updateUserDataAdmin ,name="updateUserDataAdmin"),

    path('contribute/<str:pk>/', views.contribute ,name="contribute"),
    path('makeContribution/<str:pk>/', views.makeContribution ,name="makeContribution"),

    # courses
    path('started/', views.started ,name="started"),
    path('courses/<str:pk>/', views.courses ,name="courses"),

    # subjects
    path('calculus/<str:pk>/', views.calculus ,name="calculus"),
    path('emt/<str:pk>/', views.emt ,name="emt"),
    path('itc/<str:pk>/', views.itc ,name="itc"),
    path('statistics/<str:pk>/', views.statistics ,name="statistics"),
    path('ww/<str:pk>/', views.ww ,name="ww"),

]


