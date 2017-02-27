from django.conf.urls import url
from TrucksandLoads import views

urlpatterns=[
url(r'^trucks/$',views.truck_list,name="list"),
url(r'^loads/$',views.load_list,name="list"),
        ]