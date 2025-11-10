from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, generics
from .models import Doctor, Patient, Result
from .serializers import DoctorSerializer, PatientSerializer, ResultSerializer, RegisterSerializer
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class DoctorView(viewsets.ModelViewSet):
      queryset = Doctor.objects.all()
      serializer_class = DoctorSerializer
      permission_class = [permissions.IsAuthenticatedOrReadOnly]

class PatientView(viewsets.ModelViewSet):
      queryset = Patient.objects.all()
      serializer_class = PatientSerializer
      permission_class = [permissions.IsAuthenticatedOrReadOnly]

class ResultView(viewsets.ModelViewSet):
      queryset = Result.objects.all()
      serializer_class = ResultSerializer
      permission_class = [permissions.IsAuthenticated]

      @action(detail=True,methods=['get'])
      def report(self, request, pk=None):
          test = self.get_object()
          buffer = BytesIO()
          p = canvas.Canvas(buffer)
          p.setFont('Helvetica',12)
          p.drawString(100,800,f'Patient : {test.patient.name}')
          p.drawString(100,780,f'Doctor : {test.patient.doctor.name}')
          p.drawString(100,760,f'Test Name : {test.test_name}')
          p.drawString(100,740,f'Result : {test.result_value}')
          p.drawString(100,720,f'Normal Range : {test.normal_range}')
          p.drawString(100,700,f'Date : {test.date}')
          p.showPage()
          p.save()
          buffer.seek(0)
          return FileResponse(buffer,as_attachment=True,filename=f'{test.patient.name}_report.pdf')

# Create your views here.
