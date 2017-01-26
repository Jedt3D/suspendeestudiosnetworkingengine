import gmserver
import json
iden = 0


app = gmserver

def cow(message,client):
    app.emit("event","I am a banana",client)
    print('sent data')

def auth(message,client):
    global iden
    auth = json.loads(message)

    setup = {'id':iden,'x':500,'y':500,'msgid':5}
    print("Sending Data")
    app.emit("event",json.dumps(setup),client)
    print("Sending Data")
    iden = iden + 1
def connect(message,client):
    print("Connect")
def disconnect(message,client):
    print("Disconnect")
#app.addFunc("event",cow)


app.addFunc("disconnect",disconnect)
app.addFunc("connect",connect)
app.addFunc("authentication",auth)
app.server('0.0.0.0',14579,20)
