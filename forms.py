from django import forms
from websites.models import *


class WebsiteInlineForm(forms.ModelForm):
    class Meta:
        model = Crawl.websites.through
        fields = '__all__'

    industry = forms.ModelChoiceField(queryset=Industry.objects.all())
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    age = forms.ModelChoiceField(queryset=Age.objects.all())
    gender = forms.ModelChoiceField(queryset=Gender.objects.all())
    income = forms.ModelChoiceField(queryset=Income.objects.all())
    relationship = forms.ModelChoiceField(queryset=Relationship.objects.all())
    children = forms.ModelChoiceField(queryset=Children.objects.all())

    def __init__(self, *args, **kwargs):
        super(WebsiteInlineForm, self).__init__(*args, **kwargs)
        if kwargs.get('instance'):
            web = Website.objects.get(id=self.instance.id)
            self.fields['industry'].initial = web.industry
            self.fields['industry'].label = 'Industry'
            self.fields['location'].initial = web.location
            self.fields['age'].initial = web.age
            self.fields['gender'].initial = web.gender
            self.fields['income'].initial = web.income
            self.fields['relationship'].initial = web.relationship
            self.fields['children'].initial = web.children

    def save(self, commit=True):
        instance = super(WebsiteInlineForm, self).save(commit=False)
        web = Website.objects.get(id=instance.id)
        web.industry = self.cleaned_data['industry']
        web.location = self.cleaned_data['location']
        web.age = self.cleaned_data['age']
        web.gender = self.cleaned_data['gender']
        web.income = self.cleaned_data['income']
        web.relationship = self.cleaned_data['relationship']
        web.children = self.cleaned_data['children']
        web.save()

        if commit:
            instance.save()
        return instance
