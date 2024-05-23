#!/usr/bin/python3.10

import ftime as ft
from write import fait_writer
import os
from faitsession import Fait


fait = Fait()

fait.premiere()


parent_dir="/home/ryan/Documents/fait-marquant/"
path = os.path.join(parent_dir, ft.datefmt())+"/"

	
try :
	os.mkdir(path)
except OSError as error:  
    print(error)

try :
	fait.client
except NameError:
	fait.client = "empty"
	file_name = ft.hourfmt()+"-"+fait.client+".md"
else:
	file_name = ft.hourfmt()+"-"+fait.client+".md"

full_path = path+file_name

print(full_path)

fait_writer(full_path, fait.client, fait.objet, fait.serveur, fait.ticket, fait.debut, fait.fin, fait.description)

