from django.shortcuts import render,redirect
from instamojo_wrapper import Instamojo
from .models import Coffee
from django.http import HttpResponse,HttpResponseRedirect

api = Instamojo(api_key="your api key", auth_token="your token key"  )





# Create your views here.
def home(request):
    if request.method=="POST":
        fn1 = request.POST.get("fname1")
        fn2 = request.POST.get("fname2")
        emails = request.POST.get("email1")
        phone_no = request.POST.get("phone1")
        price_sel = (request.POST.get("price1"))
        quantity_c = int(request.POST.get("q1"))
        final=int(price_sel)*(quantity_c)
        print(final,"hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        response = api.payment_request_create(
                    amount=final,
                    buyer_name = fn1,
                    purpose='Patna Comedy Carnival',
                    send_email=True,
                    email=emails,
                    phone=phone_no ,
                    redirect_url="https://patnacomedycarnival.com/success"

                    )
        print(response)
        coffee = Coffee(fname = fn1 ,sname = fn2, email=emails , phone=phone_no  , quantity=quantity_c  ,  amount= price_sel,payment_id = response['payment_request']['id']   )
          #Coffee.Amount = response['payment_request']['id']
        
        coffee.save()
        return render(request,'pay.html' , context={'payment_url': response['payment_request']['longurl'],'names1':fn1 , 'namefs':fn2,"namess":fn2 , "emailss":emails , "phn":phone_no , "ttotal":final }  )

    return render(request,'base.html')

def success(request):
    try:
        payment_request_id = request.GET.get('payment_request_id')
        coffee = Coffee.objects.get(payment_id = payment_request_id)
        coffee.Paid = True   
    
        print(coffee,"hiiiiiii")
        coffee.save()
        
    except Exception as e:
        print(e,"Exception")

    return render(request,'success.html' )


def pri(request):

    return render (request, 'privacy.html')

def ref(request):
    return render (request, 'refund.html')
def tnc(request):
    return render (request, 'tnd.html')
def contact(request):
    return render (request, 'contact.html')


def r1(request):
    return redirect("https://www.facebook.com/shudhdesicomic/")
def r2(request):
    return redirect("https://www.facebook.com/shudhdesicomic/")
def r3(request):
    return redirect("https://www.linkedin.com/in/raviguptacomedy/?originalSubdomain=in")
def r4(request):
    return redirect("https://www.facebook.com/itsgurleenpannu/")
def r5(request):
    return redirect("https://www.linkedin.com/in/gurleen-pannu-6a1b13193/?originalSubdomain=in")
def r6(request):
    return redirect("https://www.instagram.com/gurleen_pannu/?hl=en")
def r7(request):
    return redirect("https://instagram.com/patnacomedycarnival?igshid=NDk5N2NlZjQ=p")
def r8(request):
    return redirect("https://www.instagram.com/hifipatna/?igshid=NDk5N2NlZjQ%3D")
def r9(request):
    return redirect("https://instagram.com/penvoiceofficial?igshid=NDk5N2NlZjQ=")
def r10(request):
    return redirect("https://www.instagram.com/hifipatna/?igshid=NDk5N2NlZjQ%3D")
def r11(request):
    return redirect("https://www.instagram.com/hifipatna/?igshid=NDk5N2NlZjQ%3D")

