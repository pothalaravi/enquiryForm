from django import forms
from multiselectfield import MultiSelectFormField
from django.forms.widgets import SelectDatawidget

class EnquiryForm(forms.Form):
    firstname = forms.CharField(
        label='Enter your firstname',
        widget=forms.TextInput(
            attrs={
                "class": "from-control",
                "placeholder" : "your firstname"
            }
        )
    )

    lastname = forms.CharField(
        label='Enter your lasttname',
        widget=forms.TextInput(
            attrs={
                "class": "from-control",
                "placeholder": "your lasttname"
            }
        )
    )

    email = forms.EmailField(
        label='Enter your email',
        widget=forms.EmailInput(
            attrs={
                "class": "from-control",
                "placeholder": "your email"
            }
        )
    )

    mobile = forms.IntegerField(
        label='Enter your mobile number',
        widget=forms.NumberInput(
            attrs={
                "class": "from-control",
                "placeholder": "your contact number"
            }
        )
    )

    course_choices = [
        ('python', 'python'),
        ('Django', 'Django'),
        ('MySQL', 'MySQL')
    ]

    course = MultiSelectFormField(
        choices=course_choices,
        label = 'select Required courses:'
    )

    location_choices = [
        ('hyderabad', 'hyderabad'),
        ('pune', 'pune'),
        ('mumbai', 'mumbai')
    ]

    location = MultiSelectFormField(
        choices=location_choices,
        label ='select Required Locations :'
    )


    y= range(1980,2030)
    start_date =forms.DateField(
        widget=SelectDatawidget(years=y),
        label ='Enter required Date:'
    )


    gender_choices =(
        ('male','male'),
        ('female','female'),
    )
    gender = forms.ChoiceField(
        choices = gender_choices,
        widget=forms.RadioSelect(),
        label='select your gender:'
    )
