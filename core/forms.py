from django import forms

class StudentPerformanceForm(forms.Form):
    MODEL_CHOICES = [
        ('linear', 'Linear Regression'),
        ('svm', 'Support Vector Machine'),
        ('random_forest', 'Random Forest'),
        ('decision_tree', 'Decision Tree'),
    ]

    model_choice = forms.ChoiceField(label="Choose Model", choices=MODEL_CHOICES)


    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="Age",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. 17'
        })
    )


    absences = forms.IntegerField(
        min_value=0,
        max_value=93,
        label="School Absences",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        help_text="Number of school absences (0-93)"
    )


    G2 = forms.IntegerField(
        min_value=0,
        max_value=20,
        label="Second Test Grade (0-20)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )