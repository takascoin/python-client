from email.utils import parseaddr
import hashlib
import hmac
import json
import re
import sys

try:
    import urllib2
    import urllib
except ImportError:
    import urllib.request
    import urllib.parse

# ---------------------------------------------------
# ------ Python CLIENT FOR TAKASCOIN PAYMENT API ----
# ---------------------------------------------------

class Takascoin:
    #----------------------------------------------------------------
    # Create new payment
    # Required : amount		# Billed amount
    # Required : apiKey		# Merchant ApiKey (merchant email)
    # Optional : options 	# Payment options : currency # Billed currency - defaults to "TRY"
    #											orderID,
    #                                           secret,
    #                                           callback,
    #                                           item,
    #                                           description,
    #                                           minconf
    # Returns   : JSON object
    #----------------------------------------------------------------
    def payment(self, amount, apiKey, options={}):
        params = {
            'amount': amount,
            'apiKey': apiKey
        }

        params.update(options)

        try:
            response = self._apiRequest('/api/takas/payment', params)

        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response

        #----------------------------------------------------------------

    # Create new payment template to use in client side
    # Required : $amount		# Billed amount
    # Required : $apiKey		# Merchant ApiKey (merchant email)
    # Optional : $options 	# Payment options : currency # Billed currency - defaults to "TRY"
    #											orderID,
    #                                           secret,
    #                                           callback,
    #                                           item,
    #                                           description,
    #                                           minconf
    # Returns   : JSON object
    #----------------------------------------------------------------
    def button(self, amount, apiKey, options={}):
        params = {
            'amount': amount,
            'apiKey': apiKey
        }

        params.update(options)

        try:
            response = self._apiRequest('/api/takas/button', params)

        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response

        #----------------------------------------------

    #---------------------------------------------------
    # Required : invoiceID
    # Returns  : JSON object
    #---------------------------------------------------
    def status(self, invoiceID):
        params = {
            'invoiceID' : invoiceID
        }

        try:
            response = self._apiRequest('/api/status', params)
        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response


    #---------------------------------------------------
    # Required : invoiceID
    # Returns  : JSON object
    #---------------------------------------------------
    def invoice(self, invoiceID):
        params = {
            'invoiceID' : invoiceID
        }

        try:
            response = self._apiRequest('/api/invoice', params)
        except Exception as ex:
            return self.error('An error occured: ' + ex.message)

        return response


    # Validates received payment notification (IPN)
    # Required : hash      # provided by IPN call
    # Required : orderID   # provided by IPN call
    # Required : invoiceID # provided by IPN call
    # Required : secret    # secret used while creating payment
    # Returns  : True/False
    #----------------------------------------------
    def validateNotification(self, hash, orderID, invoiceID, secret):
        hexString = hmac.new(secret, ":".join([orderID, invoiceID]), hashlib.sha256).hexdigest()

        return hexString == hash


    def _apiRequest(self, url, postParams=False):
        if postParams:
            data = json.dumps(postParams)
            data = data.encode('utf-8')
        else:
            data = None

        url = "https://coinvoy.net" + url

        if sys.version_info.major == 2:
            req = urllib2.Request(url, data, {'Content-type': 'application/json'})
            response = urllib2.urlopen(req)
        else:
            req = urllib.request.Request(url, data, {'Content-type': 'application/json'})
            response = urllib.request.urlopen(req)

        return json.loads(response.read().decode())

    def error(self, message=''):
        return {'success': False, 'message': message}

    def validEmail(self, email):
        return len(email) > 3 and bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email))