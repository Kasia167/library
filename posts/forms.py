from django import forms


class add_post(forms.Form):
    title = forms.CharField()
    content = forms.Textarea()
