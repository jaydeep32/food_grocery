from django import forms


class Chceckout(forms.Form):
        first_name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
        last_name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
        Address = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Permanent address', 'rows': 5}))
        town_City = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Town name or city'}))
        District = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'district'}))
        zipcode = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area zip code'}))
        Phone = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}))
        email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
        card_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0000-0000-0000-0000'}))
        cvv = forms.CharField(max_length=3, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '***'}))
        exp_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': '2021-12-01'}))


