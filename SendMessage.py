import random

from random import randint


# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException


def sendMessage(code):
    # Specify your login credentials
    username = "Kunene"
    apikey   = "be141cfbfa9cf4ac79d6784ef3cf41e88a542ccf9757b93125724bdbfe23c238"
    # Specify the numbers that you want to send to in a comma-separated list
    # Please ensure you include the country code (+254 for Kenya)
    send_to      = "+254702212525"
    # And of course we want our recipients to know what we really do
   
    #message = str(code)

    message = "Please come'over"
    # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apikey)
    # Any gateway errors will be captured by our custom Exception class below, 
    # so wrap the call in a try-catch block


    try:
        # Thats it, hit send and we'll take care of the rest.
        
        results = gateway.sendMessage(to, message)
        
        for recipient in results:
            # status is either "Success" or "error message"
            print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                recipient['status'],
                                                                recipient['messageId'],
                                                                recipient['cost'])
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)


def generateCode(limit):
    """   """
    range_start = 10**(limit-1)
    range_end = (10**limit)-1
    code = randint(range_start, range_end)
    sendMessage(code)

generateCode(4)

def receiveTrigger():
    """ Receive a trigger from bank API """
    pass