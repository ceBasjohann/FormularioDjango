from django.contrib import admin
from django.urls import path
from form.views import home , form, create #Importa as views home , form e create


urlpatterns = [#Definição de url 
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
]
