from django.shortcuts import render,redirect
from .forms import ContactModelForm
from .models import Services,SliderOne,SliderTwo


# Create your views here.
def landing(request):
    if request.method == 'GET':
        form=SliderOne.objects.all()
        forms=SliderTwo.objects.all()
    return render(request, "index.html", {'form': form,'forms':forms})




def service(request):
    if request.method == 'GET':
        form=Services.objects.all()
    return render(request,'service.html',{'form': form})



def serviceDetails(request,pk):
    if request.method == 'GET':
        form=Services.objects.get(pk=pk)
    return render(request,'serviceDetails.html',{'form': form})




def contact(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    else:
        form = ContactModelForm()
    return render(request, "contact.html", {"form": form})



def about(request):
    return render(request, 'about.html') 


def moreabout(request):
    return render(request, 'moreabout.html')




