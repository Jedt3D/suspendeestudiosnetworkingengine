import gmserver
import json
app = gmserver

def auth(message,client):
    app.sessionset("x",{'ok':'data'},client)
    dat = app.sessionrequest("x",client)
    print(list(dat.keys()))
    app.emit("event",{'text':message.upper()},client)

def data(message,client):
    print('data being received')
    print(message)
    print('printing {}'.format(message['text']))
    print(message['text'])

    #print(mes)
    #print(mes['text'])
    app.broadcast('event',{'text':'oowowowowowo'})


print("Server Started")
app.addFunc("data",data)
app.addFunc("authentication",auth)
app.server("127.0.0.1",13068,60)
