from django.urls import path
from Questions import views

app_name="Questions"

urlpatterns=[
    path("q1/",views.quest1,name="quest1"),
    path('q2/',views.quest2,name='quest2'),
]