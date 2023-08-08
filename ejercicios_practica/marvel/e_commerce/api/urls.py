from django.urls import path
from e_commerce.api.vista import *
from e_commerce.api.marvel_api_views import *

urlpatterns = [
    path('hello-world/',hello_world),
    path('request-data/',return_request_data),
    path('ejemplo-get/',ejemplo_get),
    path('ejemplo-post/',ejemplo_post),
    path('ejemplo-post-2/',ejemplo_post_dos),
    path('get-comics/',get_comics),
    path('purchased-item/',purchased_item),
]
 