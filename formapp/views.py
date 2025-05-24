from django.shortcuts import render,redirect
from .form import ChatForm
# Create your views here.


#3 pages a home page, contact page and success page
# home page
def home_view(request):
    return render(request, "formapp/home.html")

def contact_view(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect("success")#this on submit redirects to the success page
    else:
        form = ChatForm()
    context = {"form" : form}
    return render(request, "formapp/contact.html", context)

def contact_sucess(request):
    return render(request, "formapp/success.html")