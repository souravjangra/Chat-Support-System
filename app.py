from bocadillo import App, configure
import random

app = App()
configure(app)

greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi", "whatsup")
greeting_responses = ["hey", "hey hows you?", "*nods*", "hello, how you doing", "hello", "Welcome, I am good and you"]

def send_greetings(greeting):
	for token in greeting.split():
		if token.lower() in greeting_inputs:
			return random.choice(greeting_responses)
		else:
			return "Sorry, I did'nt understand! Connecting you to our customer executive."

@app.websocket_route("/conversation")
async def converse(ws, clients: set):
    clients.add(ws)
    try:
    	async for message in ws: 
        	await ws.send(str("bot: ")+str(send_greetings(message)))
    finally:
        clients.remove(ws)

@app.route("/client-count")
async def client_count(req, res, clients):
    res.json = {"count": len(clients)}

@app.route("/")
async def index(req, res):
    res.json = {"hello": "world"}