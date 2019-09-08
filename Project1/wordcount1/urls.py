
from django.urls import path
from.import view

urlpatterns = [
    path('back',view.hello,name="back"),
    path('count',view.count,name="count"),
    path('abt', view.abot, name="about"),

]
