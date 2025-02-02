"""•	12. Write a `Payment` class with a method `process_payment()`. 
Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment`
 that override the method differently."""

class Payment:
    def process_payment(self, amount):
        raise NotImplementedError('Sub classes must implement this')
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Credit Card Payment of ${amount}"
class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"PayPal Payment of ${amount}"
class BitCoinPayment(Payment):
    def process_payment(self, amount):
        return f"BitCoin Payment of ${amount}"
def processing_payment(Payment_method,amount):
    return Payment_method.process_payment(amount)
credit_card=CreditCardPayment()
paypalpayment=PayPalPayment()
bitcoinpayment=BitCoinPayment()
print(processing_payment(credit_card,100))
print(processing_payment(paypalpayment,1000))
print(processing_payment(bitcoinpayment,200))