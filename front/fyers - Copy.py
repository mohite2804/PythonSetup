from fyers_api import fyersModel
from fyers_api import accessToken




def index(request):
    session=accessToken.SessionModel(client_id=client_id,
    secret_key=secret_key,redirect_uri=redirect_uri, 
    response_type=response_type, grant_type=grant_type)   


def generateAuthCode():
    
    client_id = 'CTHGZMLT8U-100'
    secret_key = '05GM16LPGL'
    redirect_uri='https://myapi.fyers.in/docs/'
    state = "MAHARASHTRA"
    response_type = "code"
    sample_nonce = "sample_nonce"
    grant_type = "authorization_code"

    session=accessToken.SessionModel(client_id=client_id,
    secret_key=secret_key,redirect_uri=redirect_uri, 
    response_type=response_type, grant_type=grant_type,
    state=state,scope=scope,nonce=nonce)

    response = session.generate_authcode()  

def getFund():
    result = fyers.funds()

def getProfile():
    result = fyers.get_profile()

def getHoldings():
    result = fyers.holdings()

