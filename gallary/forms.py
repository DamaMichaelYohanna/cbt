from django import forms
from gallary.models import Post,Comments
from django.contrib.auth.models import User

class Image_upload_form(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('post','img',)

class MessageForm(forms.Form):
	"""form class for sending messages."""
	name = forms.CharField(max_length=30)
	email = forms.EmailField()
	date = forms.DateTimeField(required = False)
	body = forms.CharField(widget = forms.Textarea,max_length = 1000)

class CommentForm(forms.ModelForm):
	"""docstring forCommentForm."""
	class Meta:
		model = Comments
		fields = ('name','body')

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password',
		widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password',
		widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'first_name','last_name', 'email')
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']
