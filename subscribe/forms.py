from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = "__all__"  # can be added as list if not all are required ["first_name", "email"]. Also using exclude=("first_name") which will put all fields, excluding listed
        labels = {
            "first_name": _("Enter First Name: "),
            "last_name": _("Enter Last Name: "),
            "email": _("Enter Email: "),
        }
        help_text = {"first_name": _("Enter Characters Only")}
        error_messages = {
            "first_name": {"required": _("You cannot move forward without first name")}
        }

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
