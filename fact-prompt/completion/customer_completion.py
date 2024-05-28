import os.path


def readfile(file_name):
    tab=[]
    with open(file_name,'r') as f:
        for line in f:
            tab.append(line.rstrip('\n'))
    return (tab)

def writefile(text, file_name):
    with open('{file_name}','a') as f:
        f.write('{text}')


