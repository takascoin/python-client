TAKASCOIN PAYMENT API - Python Client Library
================================

Python client library for Takascoin API


##About Takascoin

Takascoin is an online Bitcoin exchange platform. Takascoin is also a payment services provider for merchants.

##Get started

Just include takascoin.py in your document and use it freely.

```
from takascoin import Takascoin

takascoin = Takascoin()

# Create invoice
amount   = 0.012
apiKey   = "Takas merchant email"
options = {
    'currency'    : 'TRY', // OR 'BTC'
    'item'        : 'T-shirt',
    'description' : '100% cotton natural T-shirt'
}

payment = takascoin.payment(amount, apiKey)

print(payment)

# payment.url     - payment frame url to display to user
# payment.html    - default behaviour, includes an iframe and js listener
# payment.address - display payment address

```

###List of all commands:
- payment($amount, $currency, $address, $options);                - creates payment
- button($amount, $currency, $address, $options);                 - prepares a button template
- validateNotification($hash, $orderID, $invoiceID, $secret);     - checks if incoming payment notification is valid.
- status($invoiceID);                                             - current status of invoice [new,approved,confirmed,completed,cancelled]
- invoice($invoiceID);                                            - get latest invoice object


Your feedback and suggestions are very much welcome. Please contact info@takascoin.com for any input. 

Enjoy!

Takascoin

