
from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request,'index.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        dob = request.POST.get('dob')

        # Validate age as a positive integer
        try:
            age = int(age)
            if age <= 0:
                raise ValueError
        except ValueError:
            return render(request,'error.html', {'message': 'Invalid age! Age must be a positive integer.'})

        # Validate email format
        if '@' not in email or '.' not in email:
            return render(request, 'error.html', {'message': 'Invalid email address!'})

        # Save user data to the database
        User.objects.create(name=name, email=email, age=age, dob=dob)
        return redirect('view_data')
    return render(request,'index.html')

def view_data(request):
    users = User.objects.all()
    return render(request,'view.html', {'users': users})
