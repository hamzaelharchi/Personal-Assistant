from django import forms
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		fields = ("first_name", "last_name", "email", "password")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user