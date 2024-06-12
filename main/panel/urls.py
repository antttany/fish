from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('error.html', views.error),
    path('code.html', views.code),
    path('code1.html', views.code1),
    path('PayU.html', views.payu),
    path('process-data/', views.process_data, name='process_data'),
    path('process-data1/', views.process_data1, name='process_data1'),
]
