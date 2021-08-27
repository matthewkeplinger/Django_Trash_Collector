from django import forms


class InputForm(forms.Form):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    weekly_pickup_day = models.CharField(max_length=10)
