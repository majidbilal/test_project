from django.contrib import admin
from django.urls import path

from custompermissions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view1/', views.View1.as_view(), name='view1'),
    path('view2/', views.View2.as_view(), name='view2'),
]
