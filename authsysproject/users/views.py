from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import models
from django.contrib.auth.models import User
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, VaccineForm, ChildForm, ImmunizationForm
from .models import Child,Immunization
from django.db.models import Q


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has been added')
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    context = {

    }
    return render(request, 'profile/profile.html', context)
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm( instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form,

    }
    return render(request, 'profile/profile_update.html', context)

def vaccine_edit(request, pk):
    from .models import Vaccine
    item = Vaccine.objects.get(id=pk)
    if request.method == 'POST':
        form = VaccineForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            vaccine_type = form.cleaned_data.get('child_registration_no')
            messages.success(request, f'{vaccine_type} has been deleted')
            return redirect('vaccine')
    else:
        form = VaccineForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'users/vaccine_edit.html', context)

def childedit(request,pk):
    item = Child.objects.get(id=pk)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            vaccine_type = form.cleaned_data.get('child_registration_no')
            messages.success(request, f'{vaccine_type} has been updated')
            return redirect('childRegistration')
    else:
        form = ChildForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'users/childedit.html', context)


@login_required
def vaccine1(request):
    from .models import Vaccine
    data = Immunization.objects.all()
    items= Vaccine.objects.all()
    #items = vaccine.objects.raw('SELECT * FROM authsysproject_vaccine')
    if request.method =='POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            vaccine_type = form.cleaned_data.get('vaccine_type')
            messages.success(request, f'{vaccine_type} has been added')
            return redirect('vaccine')
    else:
        form = VaccineForm()
    context = {
        'items': items,
        'form':form,
        'data':data,
    }

    return render(request, 'users/vaccine.html',context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'users/home.html')

def adminchildview(request):
    items = Child.objects.all()
    
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(child_registration_no__icontains=q) | Q(phone_no__icontains=q))
        data = Child.objects.filter(multiple_q)
    else:
        data = Child.objects.all()

    context = {
        'items': items,
         'data': data,
    }
    return render(request, 'users/adminchildview.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    return render(request, 'users/login.html')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_request(request):
    messages.success(request, "You have successfully logged out.")
    return redirect("login")

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def base(request):
    from .models import Vaccine
    from .models import Profile
    from .models import Child
    vaccine = Vaccine.objects.all()
    vaccine_count = vaccine.count()
    staff = User.objects.all()
    staff_count = staff.count()
    child = Child.objects.all()
    child_count = child.count()

    context = {
        'vaccine':vaccine,
        'vaccine_count': vaccine_count,
        'staff_count': staff_count,
        'child_count': child_count,

    }
    return render(request, 'users/base.html',context)

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def staff(request):
    workers = User.objects.all()
    context ={
        'workers':workers
    }
    return render(request, 'users/staff.html',context)

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def immunization1(request,pk):
    from .models import Immunization
    items = Immunization.objects.get(id=pk)
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('childview')
    else:
        form = ImmunizationForm()
    context ={
        'items':items,
        'form':form,
    }
    return render(request, 'users/immunization.html',context)



def staff_details(request,pk):
    workers = User.objects.get(id=pk)
    context ={
        'workers':workers
    }
    return render(request, 'users/staff_details.html',context)

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def childRegistration(request):
    from .models import Child
    items = Child.objects.all()
   

    # items = vaccine.objects.raw('SELECT * FROM authsysproject_vaccine')
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('childRegistration')
    else:
        form = ChildForm()
    context = {
        'items': items,
        'form': form,

    }
    return render(request, 'users/childRegistration.html',context)

@login_required

def adminprofile(request):
    return render(request, 'users/adminprofile.html')

def childview(request):
    from .models import Child
    item = Child.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(child_registration_no__icontains=q) | Q(phone_no__icontains=q))
        item = Child.objects.filter(multiple_q)
    else:
        item = Child.objects.all()
    context = {
        'item': item
    }
    return render(request, 'users/childview.html', context)

def decorator(request):
    return render(request, 'users/decorator.html')

def vaccine_delete(request, pk):
    from .models import Vaccine
    item = Vaccine.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('vaccine')
    context = {
        'item': item
    }

    return render(request, 'users/vaccine_delete.html',context)


def childdelete(request, pk):
    from .models import Child
    item = Child.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('childRegistration')
    context = {
        'item': item
    }

    return render(request, 'users/childdelete.html',context)



# Create your views here.
