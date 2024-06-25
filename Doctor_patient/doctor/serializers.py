# serializers.py
from rest_framework import serializers
from .models import Patient
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate

# create patient
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate(self,data):
        return data
    
    def create(self, validated_data):
        user = Patient.objects.create(**validated_data)
        return user
    
# update patient
class edit_patient_serializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        print("CALLAED1")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Serializer fields:", self.fields)
        
    def update(self,instance,validated_data):
        print("CALLAED2")
        try:
            print("Update data:", validated_data)
            print("//////////////////////UPDATE DATA",validated_data)        
            try:
                instance.name = validated_data.get('name',instance.name)
                # print("----------instance phone number------------>>",instance.age)
                # print("----------instance phone number------------>>",validated_data.get('phone_number'))
                instance.medical_history = validated_data.get('medical_history', instance.medical_history)
                instance.age = validated_data.get('age', instance.age) 
                instance.user = validated_data.get('Doctor', instance.Doctor)
            except Exception as e:
                print("error ++++++++++++++++++",e)
            instance.save()
            return instance
        except Exception as e:
            print("Maybe some error instance ",e)




from .models import Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
