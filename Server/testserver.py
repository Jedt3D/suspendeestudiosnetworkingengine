import gmserver



app = gmserver

def cow(message,client):
    app.emit("event","I am a banana",client)
    print('sent data')

app.addFunc("event",cow)

app.server('0.0.0.0',14579,20)
