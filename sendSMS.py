__author__ = 'Vyasraj Vaidya'

# assignement from Plivo
# Scenarios :
# 1. Use any two numbers listed in the account for sending message. use message api to send an sms from a number to another number.
# 2. Once message api is successful, response give message uuid.Using this message uuid get the details of the message using details api.
# 3. Use pricing api to determine the rate of the message which is outbound rate under message object in this case.
# 4. Verify the rate and the price deducted for the sending message, should be same.
# 5. And finally after sending message, using account details api, account cash credit should be less than by the deducted amount.

import plivo, requests
from plivo import Message

class messageScenarios():
    def __init__(self):
        self.auth_id = 'SAZGJJMTQ5NMVJODK4NM'
        self.auth_token = 'ZWMxYzg2NDliYjIyODkwMGNkNzc4MzQxMzFjODhl'

    def sendSMS(self):
        p = plivo.RestAPI(self.auth_id, self.auth_token)
        params = {  'request_url': 'https://api.plivo.com/v1/.',
                    'number_1': 'https://api.plivo.com/v1/Account/{auth_id}/PhoneNumber/src', # use a loop ?
                    'number_2': 'https://api.plivo.com/v1/Account/{auth_id}/PhoneNumber/src', # store it differently as a json object?
                    'to': 'number_1', # to and from seems redundant
                    'from': 'number_2', #
                    'message_url': 'https://api.plivo.com/v1/Account/{auth_id}/Message/src', # need to check the src with the country_iso
                    # the pricing url displayed a specific response to the charges and
                    # assuming the message application does not need a change this url may be re-used
                    'pricing_url': 'https://api.plivo.com/v1/Account/{auth_id}/Pricing/country_iso',
        }
        response = p.Message(params)

    def process(self):
        self.sendSMS()

if __name__ == "__main__":
    c = messageScenarios()
    c.process()