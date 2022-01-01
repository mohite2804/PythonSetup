from fyers_api import fyersModel
from fyers_api import accessToken
from django.http import HttpResponse
from django.shortcuts import render,redirect



def index(request):
     return HttpResponse('login/index.html') 


def generateAuthCode(request):
   
    client_id = 'CTHGZMLT8U-100'
    secret_key = '05GM16LPGL'
    redirect_uri='https://myapi.fyers.in/docs/'
    state = "MAHARASHTRA"
    response_type = "code"
    sample_nonce = "sample_nonce"
    grant_type = "authorization_code"

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

