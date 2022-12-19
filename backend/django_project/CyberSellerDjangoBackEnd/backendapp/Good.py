from django import forms

class GoodForm(forms.Form):
	good_id = forms.IntegerField()
	name = forms.CharField(max_length=100)
	price = forms.FloatField()
	seller = forms.CharField(max_length=100)
	marker = forms.CharField(max_length=100)
