import socket
import json
import threading
import os
#Storage and Lists to keep track of users
userstorage = {}
userlist = []
userasync = {}
#Splitter, indicates the end of the message
splitter = "~§~"
#List of functions to use for each user
funclist = []
messlist = []


#Special, Do not use connect or disconnect as paths when sending from client
def disconnect(client):
    for i in funclist:
        for m in messlist:
            if messlist.index(m) == funclist.index(i) and m == "disconnect":
                i("disconnected",client)
def connect(client):
    for i in funclist:
        for m in messlist:
            if messlist.index(m) == funclist.index(i) and m == "connect":
                i("connected",client)


#def banana(message,client):
    #global splitter
    #print("Printing what was in the path")
    #jso = json.loads(message)
    #Note: If you send from the client the number as a string it will stay as a astirng until you convert it.
    #emit("event",json.dumps({'msgid':0,'num':    str(int(jso['data'])*2) }),client)
    #emit("event",json.dumps({'msgid':1,'data':'I like bananas'})       ,client)

def addFunc(message,messfunc):
    #Add functions
    #Use: addFunc("<event>","function (for example playerData() would be playerData)")
    global funclist
    global messlist
    funclist.append(messfunc)
    messlist.append(message)
    #print(funclist)



def useFunc():
    #Uses all functions
    while True:
        global funclist
        global userlist
        global messlist
        global userasync
        for f in funclist:
            for c in userlist:
                if str(c) in userasync:
                    if messlist[funclist.index(f)] in userasync[str(c)]:
                        if userasync[str(c)][messlist[funclist.index(f)]] != []:
                            useData(messlist[funclist.index(f)],f,c)
                                    #print('using function')


def useData(message,func,client):
    global userasync
    if str(client) in userasync:
        if message in userasync[str(client)]:
            for i in userasync[str(client)][message]:
                threading.Thread(target=func,args=[i,client]).start()
                #func(i,client)
            userasync[str(client)][message] = []

def fetchdata(message,client):
    global userasync
    #print(userasync)
    if message in userasync[str(client)]:
        return userasync[str(client)][message]
    else:
        return None
def processdata(message,client):
    global userasync
    global splitter
    try:
        meslis = message.split("~§~")
        meslis.remove('')
        #print("Splitting it into a list for you sir.")
        for i in meslis:
            mesdat = json.loads(i)
            for key in list(mesdat.keys()):
                if not key in userasync[str(client)]:
                        userasync[str(client)][key] = []
                #JSON.DUMPS converts keys back into strings, you may remove this if you wish
                #This checks if the key is disconnect or connect (to prevent baddies from tricking the server)
                if key != "connect" and key != "disconnect":
                    userasync[str(client)][key].append(mesdat[key])
    except:
        #Protects thread from crashing to baddies
        pass



def emit(path,message,client):
    #Message must be JSON or Message, and must be used in handleclient
    global splitter

    #
    emitdata = {}
    emitdata[path] = message
    emitdata["path"] = path
    try:
        client.send((json.dumps(emitdata)+splitter).encode('utf-8'))
        return True
    except:
        return False



def broadcast(path,message):
    #Broadcasts message across the entire server (obviously!)
    global userlist
    global splitter
    emitdata = {}
    emitdata[path] = message
    emitdata["path"] = path
    for i in userlist:
        try:
            i.send((json.dumps(emitdata)+splitter).encode('utf-8'))
            return True
        except:
            return False


def handleclient(client,addr):
    global splitter
    global userasync
    userasync[str(client)] = {}
    connect(client)
    while True:
        #sent = emit("event","{'msgid':0}",client)
        #if not sent:
            #global userlist
            #print("Client from the IP Address {} has disconnected".format(str(addr[0])))
            #disconnect(client)
            #userlist.remove(client)
            #break;
        data = ""
        #useData("authentication",banana,client)
        try:
            data = client.recv(1024)
            processdata(data.decode('utf-8'),client)
        except:
            pass
        if not data:
            global userlist
            disconnect(client)
            print("Client from the IP Address {} has disconnected".format(str(addr[0])))
            userlist.remove(client)
            break;
        #print(data)
        datv = fetchdata("authentication",client)
        #print(json.loads(datv[0]))



def server(ip,port,connlimit):
    s = socket.socket()
    s.bind((ip,port))
    s.listen(connlimit)
    global userstorage
    global userlist
    global userasync
    #addFunc("authentication",banana)
    threading.Thread(target=useFunc,args=[]).start()
    while True:
        c, addr = s.accept()
        userstorage[str(c)] = {}
        userlist.append(c)
        threading.Thread(target=handleclient,args=[c,addr]).start()






if __name__ == "__main__":
    print("Server Has Started")
    server('0.0.0.0',14579,20)
