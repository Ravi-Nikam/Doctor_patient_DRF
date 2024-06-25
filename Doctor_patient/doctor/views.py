from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .serializers import PrescriptionSerializer,PatientSerializer,edit_patient_serializer
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from rest_framework import viewsets
from .models import Patient, Prescription
from .serializers import PatientSerializer, PrescriptionSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .permissions import IsDoctor

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsAuthenticated]

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    # permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsDoctor])
def get_all_patient_info(request):
    queryset = Patient.objects.all()
    serializer = PatientSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def patient_create(request):
    if request.method == "POST":
        patient_info=PatientSerializer(data=request.data)
        try:
            if patient_info.is_valid():
                patient_info.save()
                return Response(patient_info.data,status=status.HTTP_201_CREATED)
            else:
                return Response(patient_info.errors, status=status.HTTP_400_BAD_REQUEST)  # Add this line to handle invalid data
        except Exception as e:
            print("Data validation Error !! ",e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_patient_details(request):
    print("",request.data)
    user_info=Patient.objects.get(Doctor=request.data['Doctor'])
    try:
        user_details=edit_patient_serializer(instance=user_info,data=request.data,partial=True)
        print("=========>>>>>>>>>>",user_details)
        if user_details.is_valid():
            print("Data is valid")
            updated_patient=user_details.save()
            print("----------->",updated_patient.id)
            serialized_data = {
                "id": updated_patient.id,
                "name": updated_patient.name,
                "age": updated_patient.age,
                "medical_history": updated_patient.medical_history,
            }
            
            return Response({"profile_updated": serialized_data, "message": "Patient data updated successfully"}, status=status.HTTP_200_OK)
        else:
            print("Validation errors:", user_details.errors)
            return Response(user_details.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("data fatcing error",e)
        
    return Response({"message": "Patient data not updated"})

