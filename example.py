from takascoin import Takascoin

def createPayment(amount, apiKey):
    takas = Takascoin()

    payment = takas.payment(amount, apiKey)

    print(payment)

    if payment['success']:
        status = takas.status(payment.id)

        print(status)


def getButton(amount, apiKey):
    takas = Takascoin()

    button = takas.button(amount, apiKey)

    print(button)


amount = 12 # TRY
apiKey = "takas merchant email"

# createPayment(amount, apiKey)
# getButton(amount, apiKey)