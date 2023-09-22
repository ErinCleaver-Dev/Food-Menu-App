from django.contrib import admin
from django.urls import path
import food_app.views

app_name="food_app"
urlpatterns = [
    path('', food_app.views.index, name="home" ),
    # path for details basd on id
    path('details/<int:item_id>', food_app.views.details, name="details"),
    # path for edit based on id
    path('edit/<int:item_id>', food_app.views.edit, name="edit")
]