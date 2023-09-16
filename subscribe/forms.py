from django import forms
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields="__all__" # can be added as list if not all are required ["first_name", "email"]
    



    # def validate_comma(value):
    #     if "," in value:
    #         raise forms.ValidationError("Invalid Last Name")
    #     return value
    # 
    # first_name = forms.CharField(
    #     max_length=100,
    #     required=False,
    #     label="Enter First Name",
    #     help_text="Enter characters only",
    # )
    # last_name = forms.CharField(
    #     max_length=100,
    #     disabled=False,
    #     validators=[validate_comma],
    #     label="Enter Last Name"
    # )
    # email = forms.EmailField(
    #     max_length=100,
    #     label="Enter Email"
    # )

