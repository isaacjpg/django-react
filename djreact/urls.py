
from django.contrib import admin
from django.urls import path,include

#static files
from . import settings
from django.conf.urls.static import static
#DRF Simple JWT library
from rest_framework_simplejwt.views import ( TokenObtainPairView, 
TokenRefreshView, TokenVerifyView, )

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    #For REST login
    path('auth/',include('rest_framework.urls'),name='rest_login'),
    path('get-auth-token/', TokenObtainPairView.as_view(), name='get_auth_token'),
    path('refresh-auth-token/', TokenRefreshView.as_view(), name='refresh_auth_token'),
    path('verify-auth-token/', TokenVerifyView.as_view(), name='verify_auth_token'),
    #API for other apps
    path('webapi/accounts/',include('accounts.urls'),name='webapi_accounts'),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
