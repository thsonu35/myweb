from django import forms

class calculate(forms.Form):
    number1=forms.IntegerField()
    number2=forms.IntegerField()
    number3=forms.IntegerField()

class marks(forms.Form):
    name = forms.CharField(
        label='name',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
    )
    lastname = forms.CharField(
        label='lastame',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
    )
    email = forms.CharField(
        label='email',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
    )
    sub1=forms.IntegerField()
    sub2=forms.IntegerField()
    sub3=forms.IntegerField()
    sub4=forms.IntegerField()
    sub5=forms.IntegerField()
   
