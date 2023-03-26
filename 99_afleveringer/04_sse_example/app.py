from flask import Flask, render_template, request, redirect, url_for
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost" # Flask-sse uses Redis to cache messages.
app.register_blueprint(sse, url_prefix='/stream')

### Routes
@app.route('/') # Default route, will show messages sent from /api/sendmessage in an alert box.
def index():
    return render_template('index.html')


@app.route('/sendmessage') # Route with form to send messages to /api/sendmessage
def sendMessage():
    return render_template('sendmessage.html')


@app.route('/api/sendmessage', methods=['POST']) # API route to send messages to the event stream
def apiSendMessage():
    message = request.form['message']
    sse.publish({"message": message}, type='messageFromOtherPage')
    return redirect(url_for('sendMessage'))


### Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    print("App is running on port 8080")