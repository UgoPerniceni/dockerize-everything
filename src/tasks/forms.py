from django import forms


from .models import Task

class TaskModelForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'expected_end_date',
            'color'
        ]

# COLOR_CHOICES = (
#     ('1', 'White'),
#     ('2', 'Blue'),
#     ('3', 'Red'),
#     ('4', 'Yellow')
# )

# class TaskModelForm(forms.Form):

#     title           = forms.CharField(label='Title')
#     expected_end_date = forms.DateField(initial=datetime.date.today)
#     description     = forms.CharField(widget=forms.Textarea)
#     color           = forms.ChoiceField(choices=COLOR_CHOICES)
