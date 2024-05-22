#!/usr/bin/python3.10

from prompt_toolkit import PromptSession, prompt
from prompt_toolkit.completion import WordCompleter
import ftime as ft
import os


#def datefmt():
#	return(datetime.datetime.now().strftime("%Y-%m-%d"))
	
#def hourfmt():
#	return(datetime.datetime.now().strftime("%H-%M-%S"))
	
customer_completer = WordCompleter(
    [
        "Agde",
        "Vif",
        "Cholet",
        "Cerfacs",
        "Grades",
        "Renater",
        "DGDDI",
    ],
    ignore_case=True,
)

time_completer = WordCompleter(
	[
		f"{ft.datefmt()}" ]
)

# Create prompt object.
client = PromptSession(completer=customer_completer)
session = PromptSession()
time = PromptSession(completer=time_completer)

# Do multiple input calls.
client = client.prompt('Client: ')
objet = session.prompt('Objet: ')
serveur = session.prompt('Serveur touché: ')
ticket = session.prompt('Ticket: ')
debut = time.prompt('Début: ')
fin = time.prompt('Fin: ' )
description = session.prompt('Description: ')

#########################################################


parent_dir="/home/ryan/Documents/fait-marquant/"
path = os.path.join(parent_dir, ft.datefmt())+"/"

	
try :
	os.mkdir(path)
except OSError as error:  
    print(error)
#########################################################    

try :
	client
except NameError:
	client = "empty"
	file_name = ft.hourfmt()+"-"+client+".md"
else:
	file_name = ft.hourfmt()+"-"+client+".md"

full_path = path+file_name

print(full_path)

with open(full_path, 'w') as file:
	file.write(f'##Client : {client}\n')
	file.write(f'##Objet : {objet}\n')
	file.write(f'##Serveur(s) : {serveur}\n')
	file.write(f'##Ticket : {ticket}\n')
	file.write(f'##Début : {debut}\n')
	file.write(f'##Fin : {fin}\n')
	file.write(f'##Description : {description}')


