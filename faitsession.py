from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from complet import readfile
import ftime as ft

customer_completer = WordCompleter(readfile('client.txt'),ignore_case=True,)
time_completer = WordCompleter([f"{ft.datefmt()}"])

class Fait:
    def __init__(self):
        self.client_session = PromptSession(completer=customer_completer)
        self.temps_session = PromptSession(completer=time_completer)
        self.session = PromptSession()
        
    def premiere(self):
        self.client = self.client_session.prompt('Client: ')
        self.objet = self.session.prompt('Objet: ')
        self.serveur = self.session.prompt('Serveur touché: ')
        self.ticket = self.session.prompt('Ticket: ')
        self.debut = self.temps_session.prompt('Début: ')
        self.fin = self.temps_session.prompt('Fin: ' )
        self.description = self.session.prompt('Description: ')

