from django.shortcuts import render, redirect
from .forms import PersonForm 
from .models import Person


def user_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            # Save the data to the database
            person = Person(
                first_name=first_name,
                last_name=last_name,
                email=email,
                age=age
            )
            person.save()
            # Pass data to success page
            return render(request, 'formbuilderapp/success.html', {
                'form': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'age': age
                }
            })
        else:
            error = 'Please correct the errors below.'
    else:
        form = PersonForm()
        error = None
    return render(request, 'formbuilderapp/form.html', {'form': form, 'error': error})
