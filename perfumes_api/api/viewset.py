from rest_framework import generics
from .serializers import PerfumeSerializer
from perfumes_api.models import Perfume

class PerfumeAPIList(generics.ListAPIView):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer

class PerfumeAPIRetrieve(generics.RetrieveAPIView):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer

