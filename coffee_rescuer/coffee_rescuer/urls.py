"""coffee_rescuer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,logout_then_login
from coffee_rescuer.views import mostrar_index,mostrar_nosotros,mostrar_galeria,mostrar_contactanos,predict
urlpatterns = [
    path('admin/', admin.site.urls),
    path('finca/', include('apps.finca.urls', namespace="finca")),
    path('lote/', include('apps.lote.urls', namespace="lote")),
    path('usuario/',include('apps.usuario.urls', namespace="usuario")),
    path('accounts/login/',LoginView.as_view(template_name='usuario/login.html'),name="login"),
    path('logout/',logout_then_login,name="logout"),
    path('', mostrar_index, name="index"),
    path('sobreNosotros/', mostrar_nosotros, name="sobre_nosotros"),
    path('galeria/', mostrar_galeria, name="galeria"),
    path('contactanos/', mostrar_contactanos, name="contactanos"),
    path('predict/', predict, name="predict")
]


