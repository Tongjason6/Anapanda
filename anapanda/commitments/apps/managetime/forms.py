from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Circle, Role, Task, Kummitment, Project

#class CreateTask(forms.ModelForm):
#    helper = FormHelper()
#    helper.form_show_labels = False
#
#    def __init__(self, *args, **kwargs):
#        super(createTask, self)__init__(*args, **kwargs)
#        self.helper = FormHelper()
#        self.helper.form_id = 'id-personal-data-form'
#        self.helper.form_method = 'post'
#        self.helper.form_action = reverse('submit_form')
#        self.helper.add_input(Submit('submit', 'Submit'))
