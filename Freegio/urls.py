from django.urls import path
from . import views
from . views import LaunchesListView


urlpatterns=[
    path('',views.home,name='home'),
    path('list_view',LaunchesListView.as_view(),name='list-view'),
    path('detail_view/<obj_id>',views.detail_view,name='detail_view'),
    path('API-view',views.call,name='Call_API_SPACEX')
]