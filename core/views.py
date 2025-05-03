import os
import joblib
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import StudentPerformanceForm
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_lin = joblib.load(os.path.join(BASE_DIR, 'final_model_stu_perf_pre_lin_reg.joblib'))
model_tree = joblib.load(os.path.join(BASE_DIR, 'final_model_stu_perf_pre_tree.joblib'))
model_forest = joblib.load(os.path.join(BASE_DIR, 'final_model_stu_perf_pre_forest.joblib'))
model_svr = joblib.load(os.path.join(BASE_DIR, 'final_model_stu_perf_pre_svr.joblib'))
# View function
def predict_performance(request):
    prediction = None

    if request.method == 'POST':
        form = StudentPerformanceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(f"dataaaaaaaaaaaaa: {data}")
            input_data = [[
                data['hours_studied'],
                data['previous_scores'],
                int(data['extracurricular_activities']),
                data['sleep_hours'],
                data['sample_question_papers_practiced']
            ]]

            selected_model = data['model_choice']
            if selected_model == 'linear':
                prediction = model_lin.predict(input_data)[0]
                return render(request, 'performance_index.html', {'p_index':prediction,'model_used': 'linear regression'})
            elif selected_model == 'decision_tree':
                prediction = model_tree.predict(input_data)[0]
                return render(request, 'performance_index.html', {'p_index': prediction,'model_used': 'decision tree'})

            elif selected_model == 'random_forest':
                prediction = model_forest.predict(input_data)[0]
                return render(request, 'performance_index.html', {'p_index': prediction,'model_used': 'random forest'})

            elif selected_model == 'svm':
                prediction = model_svr.predict(input_data)[0]
                return render(request, 'performance_index.html', {'p_index': prediction,'model_used': 'support vector machine'})

            else:
                prediction = "Invalid model selected."
                return render(request, 'performance_index.html', {'p_index': prediction})



    else:
        form = StudentPerformanceForm()

    return render(request, 'index.html', {
        'form': form,
        'prediction': prediction
    })
