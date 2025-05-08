from django import forms

class StudentPerformanceForm(forms.Form):
    MODEL_CHOICES = [
        ('linear', 'Linear Regression'),
        ('svm', 'Support Vector Machine'),
        ('random_forest', 'Random Forest'),
        ('decision_tree', 'Decision Tree'),
    ]

    model_choice = forms.ChoiceField(label="Choose Model", choices=MODEL_CHOICES)

    YES_NO_CHOICES = [(1, 'Yes'), (0, 'No')]

    activities = forms.ChoiceField(
        label="Extracurricular Activities",
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text="Does the student participate in extracurricular activities?"
    )

    paid = forms.ChoiceField(
        label="Paid Extra Classes",
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text="Did the student take paid extra classes?"
    )

    # Gender with clear labels
    GENDER_CHOICES = [(1, 'Male'), (0, 'Female')]

    sex = forms.ChoiceField(
        label="Gender",
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="Age",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. 17'
        })
    )

    # Address with clear labels
    ADDRESS_CHOICES = [(1, 'Urban'), (0, 'Rural')]

    address = forms.ChoiceField(
        label="Address Type",
        choices=ADDRESS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Education levels (shared between mother and father)
    EDUCATION_CHOICES = [
        (0, "None"),
        (1, "Primary education (4th grade)"),
        (2, "5th to 9th grade"),
        (3, "Secondary education"),
        (4, "Higher education"),
    ]

    Medu = forms.ChoiceField(
        choices=EDUCATION_CHOICES,
        label="Mother's Education Level",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    Fedu = forms.ChoiceField(
        choices=EDUCATION_CHOICES,
        label="Father's Education Level",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Study time with clear options
    STUDYTIME_CHOICES = [
        (1, "<2 hours"),
        (2, "2 to 5 hours"),
        (3, "5 to 10 hours"),
        (4, ">10 hours"),
    ]

    studytime = forms.ChoiceField(
        choices=STUDYTIME_CHOICES,
        label="Weekly Study Time",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    failures = forms.IntegerField(
        min_value=0,
        max_value=4,
        label="Past Class Failures",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        help_text="Number of times the student has failed a class (0-4)"
    )

    higher = forms.ChoiceField(
        label="Wants Higher Education",
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    internet = forms.ChoiceField(
        label="Has Internet Access",
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Health scale
    HEALTH_CHOICES = [
        (1, "Very bad"),
        (2, "Bad"),
        (3, "Average"),
        (4, "Good"),
        (5, "Very good"),
    ]

    health = forms.ChoiceField(
        choices=HEALTH_CHOICES,
        label="Current Health Status",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    absences = forms.IntegerField(
        min_value=0,
        max_value=93,
        label="School Absences",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        help_text="Number of school absences (0-93)"
    )

    G1 = forms.IntegerField(
        min_value=0,
        max_value=20,
        label="First Period Grade (0-20)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    G2 = forms.IntegerField(
        min_value=0,
        max_value=20,
        label="Second Period Grade (0-20)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )