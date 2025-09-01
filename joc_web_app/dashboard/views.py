from django.shortcuts import render, redirect

def dashboard_home(request):
    return render(request, "dashboard_home.html")

def dashboard_calculator_history(request):
    return render(request, "dashboard_calculator_calchistory.html")

def dashboard_calculator_product(request):
    return render(request, "dashboard_calculator_products.html")

def dashboard_calculator_smart(request):
    return render(request, "dashboard_calculator_smart.html")

def dashboard_transaction_history(request):
    return render(request, "dashboard_calculator_transhistory.html")

def dashboard_loan_list(request):
    return render(request, "dashboard_loan_list.html")

def dashboard_loan_report(request):
    return render(request, "dashboard_loan_report.html")

def dashboard_payment(request):
    return render(request, "dashboard_payment.html")

def dashboard_product(request):
    return render(request, "dashboard_product.html")

def dashboard_income(request):
    return render(request, "dashboard_report_income.html")

def dashboard_expenditure(request):
    return render(request, "dashboard_report_expenditure.html")

def dashboard_budget(request):
    return render(request, "dashboard_report_budgets.html")