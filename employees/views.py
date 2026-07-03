from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count, Sum, Avg
from django.http import JsonResponse
from .models import Employee
from .forms import LoginForm, EmployeeForm, SearchForm


# ─────────────────────────────────────────────
#  AUTH VIEWS
# ─────────────────────────────────────────────

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.get_full_name() or username}! 👋')
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    
    return render(request, 'employees/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')


# ─────────────────────────────────────────────
#  DASHBOARD VIEW
# ─────────────────────────────────────────────

@login_required
def dashboard(request):
    total_employees = Employee.objects.count()
    active_employees = Employee.objects.filter(status='Active').count()
    inactive_employees = Employee.objects.filter(status='Inactive').count()
    on_leave_employees = Employee.objects.filter(status='On Leave').count()
    
    # Department breakdown
    dept_data = Employee.objects.values('department').annotate(count=Count('id')).order_by('-count')
    
    # Salary stats
    salary_stats = Employee.objects.aggregate(
        total=Sum('salary'),
        average=Avg('salary')
    )
    
    # Recent employees (last 5)
    recent_employees = Employee.objects.order_by('-created_at')[:5]
    
    # Employees per department for chart
    dept_labels = [d['department'] for d in dept_data]
    dept_counts = [d['count'] for d in dept_data]
    
    context = {
        'total_employees': total_employees,
        'active_employees': active_employees,
        'inactive_employees': inactive_employees,
        'on_leave_employees': on_leave_employees,
        'dept_data': dept_data,
        'salary_stats': salary_stats,
        'recent_employees': recent_employees,
        'dept_labels': dept_labels,
        'dept_counts': dept_counts,
        'page_title': 'Dashboard',
    }
    return render(request, 'employees/dashboard.html', context)


# ─────────────────────────────────────────────
#  EMPLOYEE LIST & SEARCH
# ─────────────────────────────────────────────

@login_required
def employee_list(request):
    form = SearchForm(request.GET)
    employees = Employee.objects.all()
    
    query = request.GET.get('query', '')
    department = request.GET.get('department', '')
    status = request.GET.get('status', '')
    
    if query:
        employees = employees.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(designation__icontains=query) |
            Q(phone__icontains=query)
        )
    
    if department:
        employees = employees.filter(department=department)
    
    if status:
        employees = employees.filter(status=status)
    
    context = {
        'employees': employees,
        'form': form,
        'total_results': employees.count(),
        'query': query,
        'page_title': 'Employees',
    }
    return render(request, 'employees/employee_list.html', context)


# ─────────────────────────────────────────────
#  EMPLOYEE DETAIL
# ─────────────────────────────────────────────

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee,
        'page_title': f'{employee.get_full_name()} — Details',
    }
    return render(request, 'employees/employee_detail.html', context)


# ─────────────────────────────────────────────
#  ADD EMPLOYEE
# ─────────────────────────────────────────────

@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save()
            messages.success(request, f'Employee <strong>{employee.get_full_name()}</strong> added successfully! ✅')
            return redirect('employee_list')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = EmployeeForm()
    
    context = {
        'form': form,
        'action': 'Add',
        'page_title': 'Add Employee',
    }
    return render(request, 'employees/employee_form.html', context)


# ─────────────────────────────────────────────
#  UPDATE EMPLOYEE
# ─────────────────────────────────────────────

@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee <strong>{employee.get_full_name()}</strong> updated successfully! ✏️')
            return redirect('employee_list')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = EmployeeForm(instance=employee)
    
    context = {
        'form': form,
        'employee': employee,
        'action': 'Update',
        'page_title': f'Edit — {employee.get_full_name()}',
    }
    return render(request, 'employees/employee_form.html', context)


# ─────────────────────────────────────────────
#  DELETE EMPLOYEE
# ─────────────────────────────────────────────

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        name = employee.get_full_name()
        employee.delete()
        messages.success(request, f'Employee <strong>{name}</strong> deleted successfully! 🗑️')
        return redirect('employee_list')
    
    context = {
        'employee': employee,
        'page_title': f'Delete — {employee.get_full_name()}',
    }
    return render(request, 'employees/employee_confirm_delete.html', context)
