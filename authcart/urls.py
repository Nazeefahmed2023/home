from django.urls import path
from authcart import views
urlpatterns = [
    path('signup/',views.signup,name ='signup'),
    path('login/',views.handlelogin,name ='login'),
    path('logout/',views.handlelogout,name ='handlelogout'),
    path('home/', views.home, name='home'),
    path('activate/<uid64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]