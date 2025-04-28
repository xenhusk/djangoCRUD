from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import Accounts, Ledgers
from decimal import Decimal


def Home(request):
    data = {
        'ledgers':Ledgers.objects.select_related('account_no').all()
    }
    return render(request,'savingsapp/home.html', data)

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('pangalan')
        lname = request.POST.get('apelyido')
        account = Accounts(fname=fname,lname=lname)
        account.save()
        ledger = Ledgers(account_no=account)
        ledger.save()
        return redirect('bahay')
    return render(request,'savingsapp/register.html')

def Cashin(request):
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        accountNum = request.POST.get('account')
        account = get_object_or_404(
                        Accounts,
                        savings_account=accountNum
                        )
        ledger = get_object_or_404(
            Ledgers,
            account_no=account
        )
        ledger.current +=  amount
        ledger.save()
        return redirect('bahay')
    
    data = {
        'account_no': request.GET.get('account_no')
    }
    return render(request, 'savingsapp/addbalance.html',data)