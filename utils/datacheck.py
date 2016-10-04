import hashlib, csv

#builds dictionary from csv file
def getDict():
    d = {}
    data = open( 'data/accs.csv', 'r' )
    lines = data.readlines()
    for user in lines:
        info = user.strip().split(',')
        un = info[0]
        pw = info[1]
        d[un] = pw
    return d

def addEntry(username,password):
    data = open( 'data/accs.csv', 'a' )
    data.write( username + "," + password + "\n" )
    data.close()
        
    
def hashPW(password):
    return hashlib.sha224(password).hexdigest()
