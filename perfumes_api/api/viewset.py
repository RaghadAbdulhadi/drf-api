from rest_framework import generics
from .serializers import PerfumeSerializer
from perfumes_api.models import Perfume

class PerfumeAPIList(generics.ListAPIView):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer

class PerfumeAPIRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer

class PerfumeAPICreate(generics.ListCreateAPIView):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer
