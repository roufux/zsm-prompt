def fait_writer(path, client, objet, serveur, ticket, debut, fin, description):
    with open(path, 'w') as file:
        file.write(f'##Client : {client}\n')
        file.write(f'##Objet : {objet}\n')
        file.write(f'##Serveur(s) : {serveur}\n')
        file.write(f'##Ticket : {ticket}\n')
        file.write(f'##Début : {debut}\n')
        file.write(f'##Fin : {fin}\n')
        file.write(f'##Description : {description}')

