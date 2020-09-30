from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request,'dento/home.html',{})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        #send an email
        send_mail(
            message_name,#subject
            message,#message
        
            
            message_email,#from email
            ['helloferdous@gmail.com'],#to email
        )

        return render(request,'dento/contact.html',{'message_name':message_name})
    else:
        return render(request,'dento/contact.html',{})
    
def about(request):
    return render(request,'dento/about.html',{})

def blog(request):
    return render(request,'dento/blog.html',{})

def pricing(request):
    return render(request,'dento/pricing.html',{})

def service(request):
    return render(request,'dento/service.html',{})

def blog_detail(request):
    return render(request,'dento/service.html',{})



def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_message = request.POST['your-message']

       
       
        #send an email
        appointment= "Name: "+ your_name + "    >   " + "Phone :" + your_phone +  "     >    " + "Message :" + your_message  + "     >     " +"Schedule :" + your_schedule 
        
        
        

        send_mail(
            'Appointment request',#subject
            appointment,#message
        
            
            your_email,#from email
            ['helloferdous@gmail.com'],#to email
        )

       
        
        return render(request,'dento/appointment.html',{
            
            
            'your_name':your_name,
            'your_phone':your_phone,
            'your_address':your_address,
            'your_schedule':your_schedule,
            'your_message':your_message

            

            
        
        

        })
    else:
        return render(request,'dento/home.html',{})