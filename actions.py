'''
	defining actions to be performed
'''

import random
import time

def send_mail(user):
	print(f"sending emails to members of {user}'s mailing list")

def print_task(user):
	print(f"performing task for {user}")

def process_payment(user):
	signal = [0, 1]
	print(f"processing payment to {user} approved vendor...")
	time.sleep(3)
	sig = random.choice(signal) # <- to simulate a conditional execution
	if not sig:
		# failed payment: Should execute a function
		print("payment to vendor failed")
		time.sleep(2)
	else:
		print("Payment successful")
		time.sleep(2)



from controller import register_actions, actionlist
def build_action_list():
	register_actions("send mail", send_mail)
	register_actions("print tasks", print_task)
	register_actions("process payment", process_payment)

# print("Action list: ", actionlist)