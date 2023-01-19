from django.urls import path
from . import views

urlpatterns = [
    # sets the url path to home page index.html
    path('', views.home, name='index'),
    # sets the url path to Create New Account page CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # sets the url path to blanace sheet page BalanceSheet.html
    path('<int:pk>/balance/', views.balance, name='balance'),
    # sets the url path to Add New Transation page AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction')
]
