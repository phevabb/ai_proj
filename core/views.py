import pandas as pd
import os
import joblib
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import StudentPerformanceForm
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_lin = joblib.load(os.path.join(BASE_DIR, 'final_model_stu_perf_pre_lin_reg_3.joblib'))
model_tree = joblib.load(os.path.join(BASE_DIR, 'final_model_stu_perf_pre_tree_3.joblib'))
model_forest = joblib.load(os.path.join(BASE_DIR, 'final_model_stu_perf_pre_forest_3.joblib'))
model_svr = joblib.load(os.path.join(BASE_DIR, 'final_model_stu_perf_pre_svr_3.joblib'))
# View function
def predict_performance(request):
    prediction = None

    if request.method == 'POST':
        form = StudentPerformanceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            input_data = [[
                data['activities'],
                data['paid'],
                int(data['sex']),
                data['age'],
                data['address'],
                data['Medu'],
                data['Fedu'],
                data['studytime'],
                data['failures'],
                data['higher'],
                data['internet'],
                data['health'],
                data['absences'],
                data['G1'],
                data['G2'],
            ]]

            selected_model = data['model_choice']
            if selected_model == 'linear':
                student_data = pd.DataFrame(input_data, columns=['activities', 'paid','sex','age', 'address',
                                                                 'Medu', 'Fedu', 'studytime', 'failures', 'higher', 'internet',
                                                                 'health', 'absences', 'G1', 'G2'])
                prediction = model_lin.predict(student_data)[0]
                actual_score_20 = prediction
                prediction = (prediction / 20) * 100
                return render(request, 'performance_index.html', {'actual_score_20':actual_score_20, 'p_index':prediction,'model_used': 'linear regression'})

            elif selected_model == 'decision_tree':
                student_data = pd.DataFrame(input_data,
                                            columns=['activities', 'paid', 'sex', 'age', 'address',
                                                     'Medu', 'Fedu', 'studytime', 'failures', 'higher', 'internet',
                                                     'health', 'absences', 'G1', 'G2'])

                prediction = model_tree.predict(student_data)[0]
                actual_score_20 = prediction
                prediction = (prediction / 20) * 100
                return render(request, 'performance_index.html', {'actual_score_20':actual_score_20,'p_index': prediction,'model_used': 'decision tree'})

            elif selected_model == 'random_forest':
                student_data = pd.DataFrame(input_data,
                                            columns=['activities', 'paid', 'sex', 'age', 'address',
                                                     'Medu', 'Fedu', 'studytime', 'failures', 'higher', 'internet',
                                                     'health', 'absences', 'G1', 'G2'])

                prediction = model_forest.predict(student_data)[0]
                actual_score_20 = prediction
                prediction = (prediction / 20) * 100
                return render(request, 'performance_index.html', {'actual_score_20':actual_score_20,'p_index': prediction,'model_used': 'random forest'})

            elif selected_model == 'svm':
                student_data = pd.DataFrame(input_data,
                                            columns=['activities', 'paid', 'sex', 'age', 'address',
                                                     'Medu', 'Fedu', 'studytime', 'failures', 'higher', 'internet',
                                                     'health', 'absences', 'G1', 'G2'])

                prediction = model_svr.predict(student_data)[0]
                actual_score_20 = prediction
                prediction = (prediction / 20) * 100
                return render(request, 'performance_index.html', {'actual_score_20':actual_score_20,'p_index': prediction,'model_used': 'support vector machine'})

            else:
                prediction = "Invalid model selected."
                return render(request, 'performance_index.html', {'p_index': prediction})



    else:
        form = StudentPerformanceForm()

    return render(request, 'index.html', {
        'form': form,
        'prediction': prediction
    })
