from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# This function will render the Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']
        return balance(request, pk)
    content = {'form': form}    # pass content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/index.html', content)


# this function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)   # retrieve the account form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): # check to see if the submitted form is valid and if so, saves the form
            form.save()     # saves new account
            return redirect('index')    # returns the user back to the home page
    content = {'form': form}             # saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# this function will render the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk)  # retrieve all of that account's transactions
    current_total = account.initial_deposit # create account_total variable, starting with initial deposit value
    table_contents = {} # create a dictionary into which transaction info will be placed
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount                   # if deposit add amount to balance
            table_contents.update({t: current_total})   # add transaction and total to the dictionary
        else:
            current_total -= t.amount                   # if withdrawal subtract amount from balance
            table_contents.update({t: current_total})   # add transaction and total to the dictionary
    # pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    print(table_contents)
    return render(request, 'checkbook/BalanceSheet.html', content)


# this function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)   # retrueve the Transaction form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): # check to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account']
            form.save()     # saves new account
            return balance(request, pk)  # returns the user back to the home page
    content = {'form': form}             # saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
