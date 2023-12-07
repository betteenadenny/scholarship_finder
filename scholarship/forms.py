from django import forms
from .models import Scholarship

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ScholarshipForm, self).__init__(*args, **kwargs)
        self.fields.pop('verified')

class AdminScholarshipForm(ScholarshipForm):
    class Meta(ScholarshipForm.Meta):
        exclude = ['verified']

class UpdateScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['type', 'category', 'description', 'application_start_date', 'application_end_date', 'degree_types', 'major', 'application_link']

    def __init__(self, *args, **kwargs):
        super(UpdateScholarshipForm, self).__init__(*args, **kwargs)

        # Specify the fields that can be updated
        editable_fields = ['description', 'application_start_date', 'application_end_date', 'degree_types', 'major', 'application_link']

        for field_name, field in self.fields.items():
            if field_name in editable_fields:
                field.widget.attrs.pop('readonly', None)
    