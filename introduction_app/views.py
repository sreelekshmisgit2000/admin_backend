from rest_framework import viewsets
from .models import *
from .serializers import *

class IntroductionViewSet(viewsets.ModelViewSet):
    queryset = Introduction.objects.filter(is_active=True)
    serializer_class = IntroductionSerializer

class SymptomsViewSet(viewsets.ModelViewSet):
    queryset = Symptoms.objects.filter(is_active=True)
    serializer_class = SymptomsSerializer

class RiskFactorsViewSet(viewsets.ModelViewSet):
    queryset = RiskFactors.objects.filter(is_active=True)
    serializer_class = RiskFactorsSerializer

class PreparationOfSurgeryViewSet(viewsets.ModelViewSet):
    queryset = PreparationOfSurgery.objects.filter(is_active=True)
    serializer_class = PreparationOfSurgerySerializer

class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.filter(is_active=True)
    serializer_class = ProcedureSerializer

class PostProcedureViewSet(viewsets.ModelViewSet):
    queryset = PostProcedure.objects.filter(is_active=True)
    serializer_class = PostProcedureSerializer

class SuccessRateViewSet(viewsets.ModelViewSet):
    queryset = SuccessRate.objects.filter(is_active=True)
    serializer_class = SuccessRateSerializer

class FAQsViewSet(viewsets.ModelViewSet):
    queryset = FAQs.objects.filter(is_active=True).order_by('order')
    serializer_class = FAQsSerializer

class TopDoctorsViewSet(viewsets.ModelViewSet):
    queryset = TopDoctors.objects.filter(is_active=True)
    serializer_class = TopDoctorsSerializer

class TopHospitalsViewSet(viewsets.ModelViewSet):
    queryset = TopHospitals.objects.filter(is_active=True)
    serializer_class = TopHospitalsSerializer
