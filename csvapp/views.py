from django.shortcuts import render
from .forms import CSVUploadForm
from io import TextIOWrapper
import csv
from .models import Student, Program
# Create your views here.
def uploadCSV(request):
    context = {
        'csvupload_form': CSVUploadForm(),
    }
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            #parsing CSV
            csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding='utf-8')
            #Read the CSV file
            reader = csv.DictReader(csv_file)
            for each_row in reader:
                #Create a new Student object for each row
                student = Student(
                    student_id=each_row['student_id'],
                    name=each_row['name'],
                    age=int(each_row['age']),
                    gender=each_row['gender'],
                    program = Program.objects.get_or_create(
                        program_name=each_row['program']
                    )[0],
                    section=each_row['section'],
                )                
                student.save()
                context = {
                    'message': 'CSV file uploaded and processed successfully.',
                    'csvupload_form': CSVUploadForm(),
                }
            else:
                context = {
                    'message': 'Invalid form submission. Please correct the errors.',
                    'csvupload_form': form,
                }

    return render(request, 'csvapp/upload.html', context)