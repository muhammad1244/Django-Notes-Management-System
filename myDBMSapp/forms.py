
from django import forms 
from .models import *

class profilePic(forms.ModelForm): 

	class Meta: 
		model = Register 
		fields = ['profile_pic', ] 

class contributionFile(forms.ModelForm): 

	class Meta: 
		model = Contributions 
		fields = ['contribution_file', ] 
