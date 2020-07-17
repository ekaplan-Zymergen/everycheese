from django.urls import path
from . import views


app_name="cheeses"

urlpatterns = [
    # URL Pattern for the CheeseListView
    path(
        route='',
        view=views.CheeseListView.as_view(),
        name='list'
    ),    
    # URL Pattern for the CheeseCreateView
    path(
        route='add/',
        view=views.CheeseCreateView.as_view(),
        name='add'
    ),
    # URL Pattern for the CheeseUpdateView
    path(
        route='<slug:slug>/update/',
        view=views.CheeseUpdateView.as_view(),
        name='update'
    ),
    # URL Pattern for the CheeseDetailView
    path(
        route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail'
    )
]