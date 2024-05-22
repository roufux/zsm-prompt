import datetime
import os


client = ""

parent_dir="/home/ryan/Documents/fait-marquant/"
folder_name = datetime.datetime.now().strftime("%Y-%m-%d")
path = os.path.join(parent_dir, folder_name)

if(client == None):
	file_name = "empty"+datetime.datetime.now().strftime("%H-%M")+".md"
else:
    file_name = client+datetime.datetime.now().strftime("%H-%M")+".md"

full_path = path+file_name

with open(full_path, 'w') as file:
	file.write('Hello World !')
