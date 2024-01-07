from django import forms

class userForm(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    psw1=forms.CharField()
    psw2=forms.CharField()

class calculate(forms.Form):
    number1=forms.IntegerField()
    number2=forms.IntegerField()
    number3=forms.IntegerField()

class marks(forms.Form):
    sub1=forms.IntegerField()
    sub2=forms.IntegerField()
    sub3=forms.IntegerField()
    sub4=forms.IntegerField()
    sub5=forms.IntegerField()
   
