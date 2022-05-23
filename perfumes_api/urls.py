from django.urls import path
from perfumes_api.api.viewset import PerfumeAPIList, PerfumeAPIRetrieve


urlpatterns = [
    path('api/v1/perfume-list', PerfumeAPIList.as_view(), name="perfumes_list"),
    path('api/v1/<int:pk>', PerfumeAPIRetrieve.as_view(), name='perfumes_detail'),
]