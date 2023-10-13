from django.urls import path
from main.views import show_main
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, get_product_json, add_product_ajax, count_product_json, delete_product_ajax

app_name = 'main'

urlpatterns = [
    # access the imported function that located in views
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    # access the previously imported json function in views
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('count-product/', count_product_json, name='count_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-product-ajax/<int:id>',
         delete_product_ajax, name='delete_product_ajax')

]
