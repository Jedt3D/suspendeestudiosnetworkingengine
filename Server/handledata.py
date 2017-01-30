import gmserver
import json
app = gmserver

def auth(message,client):
    app.emit("event",json.dumps({'text':message.upper()}),client)

def data(message,client):
    print(message)
    mes = json.loads(message)
    print(mes)
    print(mes['text'])
    app.broadcast('event',json.dumps({'text':'oowowowowowo'}))


print("Server Started")
app.addFunc("data",data)
app.addFunc("authentication",auth)
app.server("127.0.0.1",13068,60)
