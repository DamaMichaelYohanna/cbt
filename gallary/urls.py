from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as vs
from gallary import views
from django.conf import settings
from django.conf.urls.static import static
#import django.views.static as static

urlpatterns = [
	url('^$',views.Homepage,name = 'home'),
	path("index/",views.index,name = "index"),
	path('index/<int:pk>/',views.Info, name = 'info'),
	path('contact/',views.contact_us,name = 'contact'),
	path('upload/',views.upload,name = 'upload'),
	path('<int:pk>/', views.Details.as_view(), name='detail'),
	path('login/',vs.LoginView.as_view(),name = 'login'),
	path('register/',views.register, name = 'register'),
	path('logout/',vs.LogoutView.as_view(),name = 'logout')


]
