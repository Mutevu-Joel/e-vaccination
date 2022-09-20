from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, VaccineForm, ChildForm
from .models import Child

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
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
    from .models import vaccine
    item = vaccine.objects.get(id=pk)
    if request.method == 'POST':
        form = VaccineForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
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
            return redirect('childRegistration')
    else:
        form = ChildForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'users/childedit.html', context)


@login_required
def vaccine1(request):
    from .models import vaccine
    items= vaccine.objects.all()
    #items = vaccine.objects.raw('SELECT * FROM authsysproject_vaccine')
    if request.method =='POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccine')
    else:
        form = VaccineForm()
    context = {
        'items': items,
        'form':form,
    }

    return render(request, 'users/vaccine.html',context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'users/home.html')


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
    return render(request, 'users/base.html')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def staff(request):
    return render(request, 'users/staff.html')

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
    return render(request, 'users/childview.html')
def decorator(request):
    return render(request, 'users/decorator.html')

def vaccine_delete(request, pk):
    from .models import vaccine
    item = vaccine.objects.get(id = pk)
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
