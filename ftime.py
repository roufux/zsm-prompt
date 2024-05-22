import datetime

def datefmt():
	return(datetime.datetime.now().strftime("%Y-%m-%d"))
	
def hourfmt():
	return(datetime.datetime.now().strftime("%H-%M-%S"))
