from flask import Flask, render_template, request, make_response, jsonify
import requests

### Configuration
webhooksDataFilePath = "../data/webhooks.csv"
listOfEventTypes = ["OrderCreated", "OrderUpdated", "OrderCancelled", "OrderPaid", "OrderFulfilled"]
app = Flask(__name__)


### Routes
@app.route('/')
def home():
    listOfWebhooks = getListOfWebhooks()
    return render_template('index.html', listOfWebhooks=listOfWebhooks, listOfEventTypes=listOfEventTypes)


@app.route('/registerwebhook', methods=['POST']) 
def registerwebhook():
    webhookUrl = request.form['webhookUrl']
    eventType = request.form['eventType']
    if addHookToList(webhookUrl, eventType):
        addWebhookMessage = "Webhook was added to the list"
    else:
        addWebhookMessage = "Webhook was not added to the list, it was already in the list, or something went wrong"
    listOfWebhooks = getListOfWebhooks()
    return render_template('index.html', listOfWebhooks=listOfWebhooks, listOfEventTypes=listOfEventTypes, addWebhookMessage=addWebhookMessage)


@app.route('/unregisterwebhook', methods=['POST'])
def unregisterwebhook():
    webhookUrl = request.form['webhookUrl']
    eventType = request.form['eventType']
    removeWebhookFromList(webhookUrl, eventType)
    listOfWebhooks = getListOfWebhooks()
    return render_template('index.html', listOfWebhooks=listOfWebhooks, listOfEventTypes=listOfEventTypes)


@app.route('/api/registerwebhook', methods=['POST']) 
def apiRegisterwebhook():
    try:
        data = request.get_json()
        webhookUrl = data.get('webhookUrl')
        eventType = data.get('eventType')
        if addHookToList(webhookUrl, eventType):
            return make_response("Webhook was added to the list", 200)
        else:
            return make_response("Webhook was not added to the list, it was already in the list, or something went wrong", 400)
    except:
        return make_response("Failed to parse request", 400)


@app.route('/api/unregisterwebhook', methods=['POST'])
def apiUnregisterwebhook():
    try:
        data = request.get_json()
        webhookUrl = data.get('webhookUrl')
        eventType = data.get('eventType')
        removeWebhookFromList(webhookUrl, eventType)
        return make_response("Webhook was removed from the list", 200)
    except:
        return make_response("Failed to parse request", 400)


### Functions
# Returns True if the hook is in the list, False if not
def isHookInList(webhookUrl, eventType):
    with open(webhooksDataFilePath, "r") as file:
        for line in file:
            if webhookUrl in line and eventType in line:
                return True
            
    return False


# Adds the webhook to the list TODO: Check if webhook is of a valid type.
def addHookToList(webhookUrl, eventType):
    if isHookInList(webhookUrl, eventType):
        return False
    
    lineToBeAdded = str(webhookUrl) + "," + str(eventType) + "," + "\n"
    with open(webhooksDataFilePath, "a") as file:
        file.write(lineToBeAdded)
    pingWebhook(webhookUrl, eventType, "Webhook was registered")
    return True


# Removes the webhook from the list
def removeWebhookFromList(webhookUrl, eventType): # Rewriting the entire file may not be the best way to do this, but for small files and low troughput it should be fine
    with open(webhooksDataFilePath, "r") as file:
        lines = file.readlines()
    with open(webhooksDataFilePath, "w") as file:
        for line in lines:
            webhookUrlInLine, eventTypeInLine, *_ = line.split(",")
            if webhookUrl != webhookUrlInLine or eventType != eventTypeInLine:
                file.write(line)
    return None


# Returns a list of lists with the webhook url and event type
def getListOfWebhooks():
    listOfWebhooks = []
    with open(webhooksDataFilePath, "r") as file:
        for line in file:
            webhookUrl, eventType, *_ = line.split(",")
            listOfWebhooks.append([webhookUrl, eventType])
    return listOfWebhooks


# Ping the webhook
def pingWebhook(webhookUrl, eventType, message):
    data = {'messageType': 'Ping',
    'eventType': eventType,
    'message': message}
    try: 
        r = requests.post(webhookUrl, json=data, timeout=0.1) # Low timeout since we don't care about the response
    except:
        pass
 
    
### Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    print("App is running on port 8080")