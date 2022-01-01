from fyers_api import fyersModel
from fyers_api import accessToken
from django.http import HttpResponse
from django.shortcuts import render,redirect



def index(request):
     return HttpResponse('login/index.html') 


def generateAuthCode(request):
   
    

    session=accessToken.SessionModel(client_id=client_id,
    secret_key=secret_key,redirect_uri=redirect_uri, 
    response_type=response_type, grant_type=grant_type)

    response = session.generate_authcode()  
    return redirect(response)
    
def generateToken(request):
   

    print(request)
    session.set_token(auth_code)
    response = session.generate_token()

def getFund():
    result = fyers.funds()

def getProfile():
    result = fyers.get_profile()

def getHoldings():
    result = fyers.holdings()

