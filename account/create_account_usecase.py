class CreateAccountUsecase(objec):
    def __init__(self, account_gateway, payment_client):
        self.account_gateway = account_gateway
        self.payment_client = payment_client

    def execute(self, name):
        account = self.account_gateway.save_account(name)
        self.payment_client.trial_subscription_to_account(account.account_id)
