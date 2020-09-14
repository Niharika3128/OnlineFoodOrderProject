from django.shortcuts import render,redirect
from admin.models import AdminLogin

def adminLoginCheck(request):
    if request.method == 'POST':
        try:
            AdminLogin.objects.get(username=request.POST.get('username'),password=request.POST.get('password'))
            request.session['admin_status'] = True
            return redirect('welcome_admin')
        except:
            return render(request,'admin/admin_login.html',{'error':'Invalid User'})
    else:
        request.session['admin_status'] = False
        return render(request,'admin/admin_login.html',{'error':'Admin Logout Success'})

def admin_home(request):
    return render(request,'admin/home.html')
