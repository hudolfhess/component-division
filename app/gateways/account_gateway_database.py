from account.account_gateway import AccountGateway

class AccountStruct(object):
    def __init__(self, account_id, name):
        self.account_id = account_id
        self.name = name

class AccountGatewayDatabase(AccountGateway):
    def save_account(name):
        return AccountStruct(1, name)
