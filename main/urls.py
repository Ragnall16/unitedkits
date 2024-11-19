from django.urls import path
from main.views import show_main, create_order, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_order, delete_order
from main.views import your_order, products, images
from main.views import add_order_ajax, get_form_fields
from main.views import create_order_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-order', create_order, name='create_order'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-order/<uuid:id>', edit_order, name='edit_order'),
    path('delete/<uuid:id>', delete_order, name='delete_order'),
    path('your-order/', your_order, name='your_order'),
    path('products/', products, name='products'),
    path('images/', images, name='images'),
    path('create-order-ajax', add_order_ajax, name='add_order_ajax'),
    path('get-form-fields/', get_form_fields, name='get_form_fields'),
    path('create-flutter/', create_order_flutter, name='create_order_flutter'),
]