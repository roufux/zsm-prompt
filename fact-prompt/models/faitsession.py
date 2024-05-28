from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from completion.customer_completion import readfile
import ftime as ft

customer_completer = WordCompleter(readfile('client.txt'),ignore_case=True,)
time_completer = WordCompleter([f"{ft.datefmt()}"])

class Fait:
    client_session = PromptSession(completer=customer_completer)
    temps_session = PromptSession(completer=time_completer)
    session = PromptSession()
        
    @classmethod
    def client(cls):
        return cls.client_session.prompt('Client: ')

    @classmethod
    def objet(cls):
        return cls.session.prompt('Objet: ')

    @classmethod
    def serveur(cls):
        return cls.session.prompt('Serveur touché: ')

    @classmethod
    def ticket(cls):
        return cls.session.prompt('Ticket: ')

    @classmethod
    def debut(cls):
        return cls.temps_session.prompt('Debut: ')

    @classmethod
    def fin(cls):
        return cls.temps_session.prompt('Fin: ')

    @classmethod
    def description(cls):
        return cls.session.prompt('Description: ')
