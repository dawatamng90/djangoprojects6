from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def studentinput_view(request):
    submitted = False
    form = StudentForm()
    name = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("Form validation success and I want to print the data.")
            print('Roll No:',form.cleaned_data['rollno'] )
            print('Name:',form.cleaned_data['name'] )
            print('Marks:',form.cleaned_data['marks'] )
            name = form.cleaned_data['name']
            submitted = True
    return render(request,'testapp/input.html',{'form':form,'submitted':submitted,'name':name})