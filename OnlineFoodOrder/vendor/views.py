from django.shortcuts import render,redirect
from vendor.models import VendorRegistration
from django.contrib import messages

def save_vendor(request):
    name = request.POST.get("name")
    contact1 = request.POST.get("contact1")
    contact2 = request.POST.get("contact2")
    cuisine = request.POST.get("cuisine")
    image = request.FILES["image"]
    address = request.POST.get("address")
    city = request.POST.get("city")
    password = request.POST.get("password")
    otp = 0000
    status = "pending"
    VendorRegistration(stall_name=name, contact_1=contact1, contact_2=contact2, cuisine_type_id=cuisine, photo=image, address=address,vendor_city_id=city, password=password, OTP=otp, status=status).save()
    messages.success(request, "Registration is Done, Need Approval from Admin")
    return redirect('vendor_main')


def vendorLoginCheck(request):
    if request.method == "POST":
        try:
            vendor_res = VendorRegistration.objects.get(contact1=request.POST.get("username"),
                                                password=request.POST.get("password"),status='approved')
            request.session["vendor_status"] = True
            return redirect('welcome',pk=vendor_res.id)
        except:
            return render(request, "vendor/login.html", {"error": "Invalid User"})
    else:
        request.session["vendor_status"] = False
        return render(request, "vendor/login.html", {"error": "Vendor Logout Success"})

def vendor_home(request,pk):
    request.session["vendor_id"] = pk
    vendor_details = VendorRegistration.objects.get(id=pk)
    return render(request,"vendor/home.html",{"vendor_details":vendor_details})
