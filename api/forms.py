from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    brand = forms.CharField(max_length=100)
    price = forms.DecimalField()
    manufacturer_id = forms.CharField(max_length=100)
    product_sn = forms.CharField(max_length=100)





