from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import  render,redirect
from django.contrib.auth.models import User
from .models import expense_table
from django.utils import timezone
from django.db.models import Sum
from .forms import *
from django.db.models import F

# Generic View of Signup Page

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Home Page view

def home(request):
    if not request.user.is_authenticated :
        return redirect('/accounts/login')
    username = request.user
    all_expense=expense_table.objects.filter(user=username).all()  # All Expense List of user
    total = expense_table.objects.filter(user=username).aggregate(Sum('cost'))# total expense of user
    form = PhotoForm()
    return render(request,'home.html',{'all_expense':all_expense,'total':total,'form':form})

# New Expense Add View

def add(request):
    if request.method == 'POST':
        new_expense = expense_table()
        new_expense.user = request.user
        new_expense.name = request.POST.get('name')
        new_expense.cost = request.POST.get('cost')
        new_expense.expense_date = timezone.now()
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            new_expense.image = post

        new_expense.save()
        return redirect('/home')


# Delete Existing Expense

def delete(request):
    expense = expense_table.objects.get(pk=request.POST['expense'])
    expense.delete()
    return redirect('/home')

# rendering update page for clicked expense

def update(request):
    expense = expense_table.objects.get(pk=request.POST['expense'])
    form = PhotoForm()
    return render(request, 'update.html',{'expense':expense,'form':form})

# update Existing Expense

def updatedone(request):
    expense=expense_table.objects.get(pk=request.POST['expense'])
    expense.name = request.POST['name']
    expense.cost = request.POST['cost']
    expense.save()
    return redirect('/home')

#  ascending order sort by name

def sortbyname(request):
    username = request.user
    all_expense = expense_table.objects.filter(user=username).order_by('name').all()
    total = expense_table.objects.filter(user=username).aggregate(Sum('cost'))
    form = PhotoForm()
    return render(request, 'home.html', {'all_expense': all_expense, 'total': total, 'form': form})

# descending order sort by name

def sortbyname_(request):
    username = request.user
    all_expense = expense_table.objects.filter(user=username).order_by('-name').all()
    total = expense_table.objects.filter(user=username).aggregate(Sum('cost'))
    form = PhotoForm()
    return render(request, 'home.html', {'all_expense': all_expense, 'total': total, 'form': form})

#  ascending order sort by cost

def sortbycost(request):
    username = request.user
    all_expense = expense_table.objects.filter(user=username).order_by('cost').all()
    total = expense_table.objects.filter(user=username).aggregate(Sum('cost'))
    form = PhotoForm()
    return render(request, 'home.html', {'all_expense': all_expense, 'total': total, 'form': form})

# descending order sort by cost

def sortbycost_(request):
    username = request.user
    all_expense = expense_table.objects.filter(user=username).order_by('-cost').all()
    total = expense_table.objects.filter(user=username).aggregate(Sum('cost'))
    form = PhotoForm()
    return render(request, 'home.html', {'all_expense': all_expense, 'total': total, 'form': form})
#  ascending order sort by date

def sortbydate(request):
    username = request.user
    all_expense = expense_table.objects.filter(user=username).order_by('expense_date').all()
    total = expense_table.objects.filter(user=username).aggregate(Sum('cost'))
    form = PhotoForm()
    return render(request, 'home.html', {'all_expense': all_expense, 'total': total, 'form': form})

# descending order sort by name

def sortbydate_(request):
    username = request.user
    all_expense = expense_table.objects.filter(user=username).order_by('-expense_date').all()
    total = expense_table.objects.filter(user=username).aggregate(Sum('cost'))
    form = PhotoForm()
    return render(request, 'home.html', {'all_expense': all_expense, 'total': total, 'form': form})

def sortbyimage(request):
    username = request.user
    all_expense = expense_table.objects.filter(user=username).order_by('image').all()
    total = expense_table.objects.filter(user=username).aggregate(Sum('cost'))
    form = PhotoForm()
    return render(request, 'home.html', {'all_expense': all_expense, 'total': total, 'form': form})

def sortbyimage_(request):
    username = request.user
    all_expense = expense_table.objects.filter(user=username).order_by('-image').all()
    total = expense_table.objects.filter(user=username).aggregate(Sum('cost'))
    form = PhotoForm()
    return render(request, 'home.html', {'all_expense': all_expense, 'total': total, 'form': form})







