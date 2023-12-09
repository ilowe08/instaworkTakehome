from django import forms
from .models import TeamMember


class TeamMemberForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "1112223333"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "example@example.com"}))

    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'is_admin']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[str(field)].label = ""

        self.fields['is_admin'].label = "Role"

