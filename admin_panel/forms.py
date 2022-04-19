from django import forms
from doctor import models as doctor_model
from patient import models as patient_model

class DoctorForm(forms.ModelForm):  #This class is used for doctor table to create form#
    class Meta:
        model = doctor_model.Doctor
        fields = "__all__"


class PatientForm(forms.ModelForm): #This class is used for patient table to create form#
    class Meta:
        model = patient_model.Patient
        fields = "__all__"
