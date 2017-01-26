import gmserver
import json
app = gmserver


def doSomething(message,client):
    app.emit("event",json.loads(message),client)
    app.broadcast("event","{'pie':'banana'}")

















app.addFunc("authentication",doSomething)
app.server("127.0.0.1",14579,64)
