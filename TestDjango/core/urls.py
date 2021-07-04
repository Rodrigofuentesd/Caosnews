from django.urls import path
from .views import home
from .views import home_usuario
from .views import home_editor_user
from .views import home_editor_editor
from .views import create_user
from .views import new_1
from .views import new_1_editor
from .views import new_template


urlpatterns = [
    path('', home, name="index-invitado"),
    path('home_user', home_usuario, name="index-usuario"),
    path('home_editor_user', home_editor_user, name="index-editor-user"),
    path('home_editor_editor', home_editor_editor, name="index-editor-editor"),
    path('create_user', create_user, name="create_user"),
    path('new_1', new_1, name="new-1"),
    path('new_1_editor', new_1_editor, name="new-1-editor"),
    path('new_template', new_template, name="new-template"),
 
    
]