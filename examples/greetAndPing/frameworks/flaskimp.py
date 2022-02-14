from flask import Flask
from markupsafe import escape
# Local
from examples.greetAndPing.GreetUseCase import greet
from examples.greetAndPing.PingAppUseCase import pingApp

app = Flask(__name__)

@app.route("/greet/<name>")
def greet_route(name): return greet(name=escape(name))


@app.route("/ping")
def ping_route(): return pingApp()

if __name__ == '__main__': app.run()
