from django.shortcuts import render,redirect
from userapp.models import userregistrationdb,bookingdb,feedbackdb,history
from tourismapp.models import destinationdb
from django.contrib import messages
from django.utils.timezone import datetime



# Create your views here.
def registration_fn(req):
    return render(req,'userlogin.html')
def homepage_fn(req):
    return render(req,'homepage.html')
def saveregistrationdata(req):
    if req.method=='POST':
        un=req.POST.get('username')
        pas=req.POST.get('password')
        obj = userregistrationdb(uname=un,upass=pas)
        obj.save()
        return redirect(registration_fn)



def signup_fn(req):
    if req.method=='POST':
        uname=req.POST.get('susername')
        pwd=req.POST.get('password')
        if userregistrationdb.objects.filter(uname=uname,upass=pwd).exists():

            req.session['username']=uname
            req.session['password']=pwd
            return redirect(homepage_fn)
        else:

            return redirect(registration_fn)

    return redirect(registration_fn)

def userlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(registration_fn)
def contactpage(req):
    return render(req,'contact.html')
def hotelbooking(req):
    return render(req,'hotel.html')
def destination_page(req):
    data=destinationdb.objects.all()
    return render(req,'destination.html',{'data':data})
def singledest_fn(req,dataid):
        dest = destinationdb.objects.get(id=dataid)
        return render(req, 'singledestination.html',{'dest':dest})

def booking_fn(req):
    data=bookingdb.objects.filter(name=req.session['username'])
    # des=destinationdb.objects.all()
    return render(req,'book_ticket.html',{'data':data})
def savebooking(req):
    if req.method == 'POST':

        n= req.POST.get('name')
        des= req.POST.get('dest')
        join = req.POST.get('joi')
        em= req.POST.get('email')
        ded=req.POST.get('dd')
        pa= req.POST.get('pack')
        m= req.POST.get('mob')
        me= req.POST.get('mem')
        obj=bookingdb(name=n,destination_place=des,joining_place=join,email=em,package=pa,mobile=m,members=me,departure_date=ded)
        obj.save()
        return redirect(booking_fn)
def displaybook_fn(req):
    data=bookingdb.objects.all()
    return render(req,'displaybooking.html',{'data':data})
def deletebooking(req,dataid):
    data=bookingdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaybook_fn)
def feedback_fn(req):
    return render(req,'text_feedback.html')
def savefeedback(req):
    if req.method=='POST':
        un=req.POST.get('username')
        fb=req.POST.get('feedbac')
        obj=feedbackdb(user=un,feedback=fb)
        obj.save()
        return redirect(homepage_fn)
def contact_fn(req):
    return render(req,'contact.html')
def history_fn(req):
    data=bookingdb.objects.all()
    return render(req,'display_history.html',{'data':data})
# def savehistory(req):
#     if req.method=='POST':
#         us=req.POST.get('username')
#         dep=req.POST.get('')
#         ra=req.POST.get('')
#         obj=history(users=us,des_place=dep,rating=ra)
#         obj.save()
#         return redirect(homepage_fn)






