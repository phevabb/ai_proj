from django import forms

class StudentPerformanceForm(forms.Form):
    MODEL_CHOICES = [
        ('linear', 'Linear Regression'),
        ('svm', 'Support Vector Machine'),
        ('random_forest', 'Random Forest'),
        ('decision_tree', 'Decision Tree'),
    ]

    model_choice = forms.ChoiceField(label="Choose Model", choices=MODEL_CHOICES)

    hours_studied = forms.FloatField(label="Hours Studied", min_value=0, max_value=24)
    previous_scores = forms.FloatField(label="Previous Scores", min_value=0, max_value=100)
    extracurricular_activities = forms.ChoiceField(
        label="Extracurricular Activities",
        choices=[(1, 'Yes'), (0, 'No')],
        widget=forms.Select()
    )
    sleep_hours = forms.FloatField(label="Sleep Hours", min_value=0, max_value=12)
    sample_question_papers_practiced = forms.IntegerField(label="Sample Question Papers Practiced", min_value=0, max_value=20)
