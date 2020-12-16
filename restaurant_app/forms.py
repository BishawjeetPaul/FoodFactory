from django import forms
from restaurant_app.models import RestaurantModel

class RestaurantForm(forms.ModelForm):
	resto_password = forms.CharField(max_length=30, widget=forms.PasswordInput)
	class Meta:
		model = RestaurantModel
		fields = "__all__"
		excluce	= ('resto_id', 'resto_otp', 'resto_status')

class RestroLoginForm(forms.Form):
	contactno = forms.IntegerField()
	password = forms.CharField(max_length=30,widget=forms.PasswordInput)