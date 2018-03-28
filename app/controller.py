from account.create_account_usecase import CreateAccountUsecase
from app.clients.payment_client import PaymentClient
from app.gateways.account_gateway_database import AccountGatewayDatabase

def signup(request):
    account_gateway = AccountGatewayDatabase()
    payment_client = PaymentClient()
    CreateAccountUsecase(account_gateway, payment_client) \
        .execute(request.POST.get('name'))
