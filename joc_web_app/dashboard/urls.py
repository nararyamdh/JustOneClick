from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard_home, name="dashboard_home"),
    path('cashier/calculator/history/', views.dashboard_calculator_history, name="dashboard_calculator_history"),
    path('cashier/calculator/product/', views.dashboard_calculator_product, name=".dashboard_calculator_product"),
    path('cashier/calculator/smart/', views.dashboard_calculator_smart, name="dashboard_calculator_smart"),
    path('cashier/transaction/history/', views.dashboard_transaction_history, name="dashboard_transaction_history"),
    path('loan/', views.dashboard_loan_list, name="dashboard_loan_list"),
    path('loan/report/', views.dashboard_loan_report, name="dashboard_loan_report"),
    path('payment/', views.dashboard_payment, name="dashboard_payment"),
    path('product/', views.dashboard_product, name="dashboard_product"),
    path('income/', views.dashboard_income, name="dashboard_income"),
    path('expenditure/', views.dashboard_expenditure, name="dashboard_expenditure"),
    path('budget/', views.dashboard_budget, name="dashboard_budget")
]