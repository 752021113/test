# import the standard Django Forms
# from built-in library
from django import forms
from .models import GeeksModel
   
# creating a form 
class InputForm(forms.Form):
   
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())\

from django import forms


# # create a ModelForm
# class GeeksForm(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = GeeksModel
#         fields = "__all__"


from django import forms
  
# create a form
# class GeeksForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()




# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = GeeksModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]