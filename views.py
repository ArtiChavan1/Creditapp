from django.shortcuts import render, redirect
from .forms import LoanApplicationForm
from .models import LoanApplication


def home(request):
    return render(request, 'home.html')

def apply_loan(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loan_success')
    else:
        form = LoanApplicationForm()
    return render(request, 'loan_application_form.html', {'form': form})


def dashboard(request):
    applications = LoanApplication.objects.all()
    total_applications = applications.count()
    pending_loans = applications.filter(status='Pending').count()
    approved_loans = applications.filter(status='Approved').count()
    rejected_loans = applications.filter(status='Rejected').count()

    context = {
        'total_applications': total_applications,
        'pending_loans': pending_loans,
        'approved_loans': approved_loans,
        'rejected_loans': rejected_loans,
    }
    return render(request, 'dashboard.html', context)
