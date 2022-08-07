from django import forms


class AddPost(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
