from django.urls import path 
from.import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('insert/',views.insert,name="insert"),
    path('view/',views.view,name="view"),
    path('detailview/<str:pk>',views.detailview,name="detailview"),
    path('deleted/<str:pk>',views.delete,name="deleted"),
    path('update/<str:pk>',views.update,name="update"),
    path('log/',views.loginn,name="log"),
     path('userlog/',views.userlog,name="user"),
     path('welcome/',views.welcome,name="welcome"),
     path('logout/',views.logout,name="logout"),

]