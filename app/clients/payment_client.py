from payment.create_trial_subscription_to_account_usecase import CreateTrialSubscriptionToAccountUsecase

class PaymentClient(object):
    def trial_subscription_to_account(self, account_id):
        CreateTrialSubscriptionToAccountUsecase().execute(account_id)