import gmserver
import json
app = gmserver

def auth(message,client):
    print('data')
    app.sessionset("x",{'ok':'data'},client)
    app.sessionset("yogurt",'banana',client)
    app.sessionset("eating",'burgers',client)
    print(app.sessionvariables(client))
    dat = app.sessionrequest("x",client)
    print(app.sessiongetlist("yogurt","banana"))
    print(app.sessiongetlist("eating","burgers"))
    #print(list(dat.keys()))
    app.emit("event",{'text':message.upper()},client)

def data(message,client):
    print('data being received')
    print(message)
    print('printing {}'.format(message['text']))
    print(message['text'])
    print(message['text'])
    app.broadcast('event',{'text':'oowowowowowo'})

def createData(message,client):
    dat = app.sessionrequest('x',client)
    if dat == None:
        app.sessionset("x",200,client)
    print(app.sessionrequest('x',client))
    for i in app.sessionvariables(client):
        app.sessionset(i,None)

    rooms = app.sessiongetlist("room","Player1")





print("Server Started")
app.addFunc("data",data)
app.addFunc("authentication",auth)
app.server("127.0.0.1",13068,60)
