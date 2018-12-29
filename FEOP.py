from flask import Flask, request
import telepot
import urllib3

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "bot"
bot = telepot.Bot('744988034:AAF9H6SaS588maPyDGJuCT7SPzznPLmQc50')
bot.setWebhook("https://tahamoh.pythonanywhere.com/{}".format(secret), max_connections=1)

# Function for nth Fibonacci number

def Fibonacci(n):
	if n<0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n==0:
		return 0
	# Second Fibonacci number is 1
	elif n==1:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)


# Python program to check if the input number is odd or even.
# A number is even if division by 2 give a remainder of 0.
# If remainder is 1, it is odd number.

def evenodd(n):
    if (n % 2) == 0:
        return "It is an even number."
    else:
        return "It is an odd number."




# Python program to check if the input number is prime or not
#We all know that prime numbers are greater than 1

def primeornot(n):
# Python program to check if the input number is prime or not
# prime numbers are greater than 1
    if n > 1:
       # check for factors
       for i in range(2,n):
           if (n % i) == 0:
               return "is not a prime number."
               break
       else:
           return "It is a prime number."

    # if input number is less than
    # or equal to 1, it is not prime
    else:
       return "It is not a prime number."





def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        text=msg['text']
        if text=='/start':
            bot.sendMessage(chat_id,'Hello,Welcome to my bot , if you want to know what does this bot do , please type and send  /help keyboard.')
        elif text=='/help':
            bot.sendMessage(chat_id,'This bot get a number from you and then return for you the nth of fibonacci number  and sayto you is it even or odd and is it prime or not .')
        else:
            text=int(text)
            a=Fibonacci(text)
            b=primeornot(text)
            c=evenodd(text)
            bot.sendMessage(chat_id,a)
            bot.sendMessage(chat_id,b)
            bot.sendMessage(chat_id,c)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        handle(update["message"])
    return "OK"
