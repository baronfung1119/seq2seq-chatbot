# -*- coding: UTF-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from difflib import SequenceMatcher
import os
import csv
import random

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
out_msg = ''

def get_response(userText):
	bot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
		{
			'import_path': 'chatterbot.logic.BestMatch',
			"response_selection_method": "chatterbot.response_selection.get_random_response"

		},
		{
			'import_path': 'chatterbot.logic.LowConfidenceAdapter',
			'threshold': 0.70,
			'default_response': 'I am sorry, but I do not understand.'
		}
    	],		    
	preprocessors=['chatterbot.preprocessors.clean_whitespace',
                   'chatterbot.preprocessors.unescape_html', 'chatterbot.preprocessors.convert_to_ascii'],
    	silence_performance_warning=True,
    	filters=["chatterbot.filters.RepetitiveResponseFilter"]
	)
class Booking:
	def __init__(self):
		self.surname=''
		self.forename=''
		self.film=''
		self.day=''
		self.noofseat=''
		self.bookingref=str(random.randint(0,100000))
		

		
def booking():
	bookings = []
	#bookingref = random.randint(0,100000)
	#bookingref = str(bookingref)

	print("Your Booking number: ", bookingref)
	surname = input("Please enter your surname: ")
	forename = input("Please enter your other name: ")
	film = input("Please enter the name of film you want to see: ")
	day = input("Please enter the day of the week you want to see the film: ")
	while (day not in ['1', '2', '3', '4', '5', '6', '7']):
		day = input("You input weekday not correct, please try to input again: ")	
	noofseat = input("Please enter number of the seat you want to researved: ")
	while ((noofseat.isdigit() == False) or (noofseat.isdigit() == True and int(noofseat) > 50)):
		if (noofseat.isdigit() == False):
			noofseat = input("You have input incorrect integer number, please try to input again: ")
		else:
			noofseat = input("You have inputted the number exceeds the maxium 50 seats in the cinema, please try to input again: ")	
	print ("Dear ", forename, surname, ", your booking on the film **", film, "** on day ", day, "with ", noofseat, "people has been confirmed.")
	print ("Thank you for your booking!!!")

	bookings.append(bookingref)
	bookings.append(surname)
	bookings.append(forename)
	bookings.append(film)
	bookings.append(day)
	bookings.append(noofseat)

	with open("cinema.csv","a", newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(bookings) 

def booking_ch():
	bookings = []
	bookingref = random.randint(0,100000)
	bookingref = str(bookingref)

	print("??????????????????: ", bookingref)
	surname = input("??????????????????: ")
	forename = input("??????????????????: ")
	film = input("????????????????????????: ")
	day = input("???????????????????????????: ")
	while (day not in ['1', '2', '3', '4', '5', '6', '???', '???', '???', '???', '???', '???', '???']):
		day = input("??????????????????????????????????????????????????????????????????: ")	
	noofseat = input("??????????????????????????????: ")
	while ((noofseat.isdigit() == False) or (noofseat.isdigit() == True and int(noofseat) > 50)):
		if (noofseat.isdigit() == False):
			noofseat = input("?????????????????????????????????????????????????????????????????????: ")
		else:
			noofseat = input("?????????????????????????????????????????????????????????: ")	
	print ("????????? ", surname, forename, ", ????????????????????? **", film, "** ?????????", day, "??????", noofseat, "???????????????????????????????????????")
	print ("??????????????????????????????!!!")

	bookings.append(bookingref)
	bookings.append(surname)
	bookings.append(forename)
	bookings.append(film)
	bookings.append(day)
	bookings.append(noofseat)

	with open("cinema.csv","a", newline='') as csvfile:	
		writer = csv.writer(csvfile)
		writer.writerow(bookings) 

def view_booking():
	count = 0
	with open('cinema.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			bookingref = row[0]
			surname = row[1]
			forname = row[2]
			film = row[3]
			day = row[4]
			noofseat = row[5]
			output = (bookingref, surname, forname, '**', film, '**', 'Booked Weekday:', day, 'No. of seat:', noofseat)
	return(output)

def view_booking_ch():
	count = 0
	with open('cinema.csv', 'r', encoding="utf-8", errors='ignore') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			bookingref = row[0]
			surname = row[1]
			forname = row[2]
			film = row[3]
			day = row[4]
			noofseat = row[5]
			output = (bookingref, surname, forname, '**', film, '**', '??????????????????', day, '??????:', noofseat)
	return(output)

def joking():
	joke_choice = random.randint(1,9)
	joke_choice = str(joke_choice)
	with open('joke.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		num = []
		topic = []
		detl = []
		for row in reader:
			num = row[0]
			topic = row[1]
			detl = row[2]
			if (joke_choice == num):
				return(detl)

def joking_ch():
	joke_choice_ch = random.randint(1,9)
	joke_choice_ch = str(joke_choice_ch)
	with open('joke_ch.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		num = []
		topic = []
		detl = []
		for row in reader:
			num = row[0]
			topic = row[1]
			detl = row[2]
			if (joke_choice_ch == num):
				return(detl)

def Chatbot_1(input_msg):
	bot.read_only = True

	repetitiveReply = [
    		"This question seems faimilar",
    		"You are so boring , let talk something else",
    		"boo...boo... Stop . You just asked it",
    		"Ok! Next Question",
    		"OMG! Can we talk about something else?",
    		"I am not answering such a stupid question",
    		"Talking with you is damn boring ! Why are you keep asking the same question",
    		"Ok ! Stop it , i am done! . Next Question!",
    		"Oh! Come on ! Next Question",
    		"@#$545$ You! Why are you keep asking. ",
    		"This question seems similar to the last message, Let change another Topic,ok?",
    		"Sorry, i have already answer this question"
	]

	unknownReply = [
    		"Sorry, i cannot understnad this question",
    		"Sorry, What does it mean? ",
    		"I am sorry, I did not catch what you said. Could you repeat it ",
    		"I am sorry, I did nott understand that? Would you mind repeating it",
    		"I am sorry, what was that?",
    		"What did you say?",
    		"What was that?",
    		"Excuse me? ",
	    	"What?",
	]

	last_message = ""
	counter=0

	def similar(a, b):
    		return SequenceMatcher(None, a, b).ratio()

	message = (input_msg)
	if message.strip() != 'Bye':
		if ('cinema' in message.strip()) and ('booking' in message.strip()):
			out_msg = booking()
		elif (b'\xe9\x9b\xbb\xe5\xbd\xb1'.decode('utf-8') in message.strip()) and (b'\xe9\xa0\x90\xe7\xb4\x84'.decode('utf-8') in message.strip()):
			out_msg = booking_ch()
		elif ('view' in message.strip()) and ('booking' in message.strip()):
			out_msg = view_booking()
		elif (b'\xe9\xa0\x90\xe7\xb4\x84'.decode('utf-8') in message.strip()) and (b'\xe8\xa7\x80\xe7\x9c\x8b'.decode('utf-8') in message.strip()):
			out_msg = view_booking_ch()
		elif ('joke' in message.strip()) and ('tell' in message.strip()):
			out_msg = joking()
		elif (b'\xe7\xac\x91\xe8\xa9\xb6'.decode('utf-8') in message.strip()) and (b'\xe8\xac\x9b'.decode('utf-8') in message.strip()):
			out_msg = joking_ch()
		else:
			if similar(message, last_message) > 0.4:
				out_msg = random.choice(repetitiveReply)
				counter += 1
				last_message = message
			if message == last_message:
				out_msg = random.choice(repetitiveReply)
				counter += 1
				last_message = message
			if message.strip().lower() != 'bye':
				response = bot.get_response(message)
				if(response.confidence > 0.4):
					out_msg = response
					counter = 0
				elif response.confidence <= 0.4:
					out_msg = random.choice(unknownReply)
					counter += 1
				last_message = message
			if message.strip().lower() == 'bye':
				out_msg = 'Bye'
			if counter >= 5:
				out_msg = 'I have to go now . Bye Bye!'
	if message.strip() == 'Bye':
		out_msg = 'Bye!'
	return(out_msg)

#main routine
'''
while True:
    Message = input('You:')
    #Message = '??????'
    #Message = b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8')
    #print(Message)
    output = Chatbot_1(Message)
    print('Chatbot: ', output)
    if Message == 'Bye':
        break'''
