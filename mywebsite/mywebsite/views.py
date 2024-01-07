from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from service.models import service


def evenoff(request):
    
    fun = int(forms.IntegerField())
    ans=0
    input_data={'enenoddd':fun}
    try:
        if request.method =="POST":
            val1 = eval(request.POST.get('fun'))
            evenodd = 0
            if fun % 2 == 0:
                evenodd = 'even'
            else:
                evenodd = 'odd'
            input_data = {
                'enenoddd': fun,
               
                'ans1': evenodd
            }

    except ValueError as e:
        pass

    return render(request, 'evenoff.html', input_data)
           

            

def calculator(request):
    fun = calculate()
    ans = 0
    ans2 = 0
    
    input_data = {'calc': fun}
    try:
        if request.method == "POST":
            val1 = eval(request.POST.get('number1'))
            val2 = eval(request.POST.get('number2'))
            val3 = eval(request.POST.get('number3'))
            no2 = (request.POST.get('no1'))
            opra = request.POST.get('opera')
            
            if val3 % 2==0:
                ans2='enen'
            else:
                ans2='odd'
            
            
            if opra == '+':
                ans = val1 + val2
            elif opra == '-':
                ans = val1 - val2
            elif opra == '*':
                ans = val1 * val2
            elif opra == '%':
                ans = val1 % val2
            elif opra == '/':
                ans = val1 / val2
            
            input_data = {
                'calc': fun,
                'ans': ans,
                'ans2': ans2
            }

    except ValueError as e:
        pass

    return render(request, 'calculator.html', input_data)
           
# def evenoddprog(request):
#     fn=evenorodd()
#     data={'evod':fn}
#     try:
        
#     except ValueError as e:
#         pass
#     return render(request, 'calculator.html', data)


def marksheet(request):

    serviceDATA=service.objects.all()
    data = {
        'serviceData':serviceDATA
    }

    # for a in serviceDATA:
    #     print(a.name,a.lastname,a.email)
    #     print(service)
    fn = marks()  # Replace "Student Name" with the actual name or method to get the name
    total_subjects = 5  # Assuming there are 5 subjects

    data = {
        'avg': 0,
        'percent': 0,
        'fn': fn,
    }

    try:
        if request.method == 'POST':
            sb1 = eval(request.POST.get('sub1'))
            sb2 = eval(request.POST.get('sub2'))
            sb3 = eval(request.POST.get('sub3'))
            sb4 = eval(request.POST.get('sub4'))
            sb5 = eval(request.POST.get('sub5'))

            total_marks = sb1 + sb2 + sb3 + sb4 + sb5
            avg = total_marks / total_subjects
            percent = (total_marks / (total_subjects * 100)) * 100

            data = {
                'total_marks': total_marks,
                'percent': percent,
                'fn': fn
            }

    except ValueError as e:
        data['error'] = "Invalid input. Please enter numerical values for all subjects."

    return render(request, 'marksheet.html', data)


    



def form(request):
    fn=userForm()
    data = {'form':fn}

    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            psw = request.POST.get('pass1')
            psw2 = request.POST.get('pass2')

            # Process the data or perform any other logic here
            data = {
                'form':fn
            }
            url = "/login/?output={}".format('51')

            # Redirect to another URL after processing the form
            return HttpResponseRedirect(url)

    except ValueError as e:
     pass
        

    return render(request, 'form.html', data)

def login(request):
    if request.method == "GET":
        Output = request.GET.get('output')
     

    return render(request, "login.html", {"output": Output})


# def form(request):
#     data={}
#     finalans=0;
#     pass1=0;

#     try:
#          if request.method=="POST":
#             #   var1=int(request.get['no1'])
#             #   var2=int(request.get['no2'])
#             var1=int(request.POST.get('no1'))
#             var2=int(request.POST.get('no2'))
#             pass1=int(request.POST.get('pass'))
         
           
#     except:
#         pass
#     return render(request,'form.html',{"output":finalans},{"pass":pass1})

    # try:
    #       if request.method=="POST":
    #         #    var1=request.GET['Email']
    #         #    var2=request.GET['Name']
    #         #    var3=request.GET['Password']
    #         #    print(var1 ,var2 , var3);
    #            var1=request.POST.get('Email')
    #            var2=request.POST.get('Name')
    #            data={
    #                 'n1':var1,
    #                 'n2':var2,
    #            }
    #         #    return HttpResponse("successfull")
    # except:
    #  pass
    return render(request,'form.html',{"output":finalans})
    # try:
    #     if request.method=="POST":
    #          return HttpResponse("<h1>successfull</h1>")
    # except:
    #      pass    
     

# def contact(request):
#        finalans=0
       

#        try:
#            if request.method=="POST":
#                 n1=int(request.POST.get['name1']),
#                 n2=int(request.POST.get['password1'])
#                 data={
#                      'n1':n1,
#                      'n2':n2,
#                      'output':finalans
#                 }
#                 url="/about-us/?output={}",format(finalans)
#                 return HttpResponseRedirect(url)
#                 finalans=n1+n2
                
           
    #    except:
    #        pass
    #    return render(request,"form.html")

def home(request):
    # data = { 
    #     'title':"rishab",
    #     'bdata':"hello world",
    #     'lists':['php','java','python','django'],
    #     'dictdata':[
    #         {'name':'sohan','class':'5th'},
    #         {'name':'sonu','class':'8th'}
    #     ],
    #     'k':[1,2,3,4,5,6,7,8,9,10]
    #      }
    return render(request,"index.html")

def success(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            psw = request.POST.get('pass1')
            psw2 = request.POST.get('pass2')

            # Process the data or perform any other logic here
            data = {
                "NAME": name,
                "EMAIL": email,
                "PASSW1": psw,
                "PASSW2": psw2
            }
            

            # Redirect to another URL after processing the form
            return HttpResponse(data)

    except ValueError as e:
     pass
        

    # return render(request, 'form.html', data)



def login(request):
    return render(request,"login.html")

def register(request):
    
       return render(request,"register.html")

