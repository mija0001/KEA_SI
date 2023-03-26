import requests, time, random

### Configuration
webhooksDataFilePath = "../data/webhooks.csv"
listOfEventTypes = ["OrderCreated", "OrderUpdated", "OrderCancelled", "OrderPaid", "OrderFulfilled"]


### Functions
def getListOfWebhooksFromFile():
    listOfWebhooks = []
    with open(webhooksDataFilePath, "r") as file:
        for line in file:
            webhookUrl, eventType, *_ = line.split(",")
            listOfWebhooks.append([webhookUrl, eventType])
    return listOfWebhooks


def sendEventToWebhook(webhookUrl, eventType, message):
    try:
        r = requests.post(webhookUrl, json={"messageType": "Event", "eventType": eventType, "message": message}, timeout=0.1) # Low timeout since we don't care about the response
    except:
        pass


def orderCreated(OrderId):
    listOfWebhooks = getListOfWebhooksFromFile()
    for webhook in listOfWebhooks:
        webhookUrl, eventType = webhook
        if eventType == "OrderCreated":
            sendEventToWebhook(webhookUrl, eventType, "Order id: " + str(OrderId) + " was created")


def orderUpdated(OrderId):
    listOfWebhooks = getListOfWebhooksFromFile()
    for webhook in listOfWebhooks:
        webhookUrl, eventType = webhook
        if eventType == "OrderUpdated":
            sendEventToWebhook(webhookUrl, eventType, "Order id: " + str(OrderId) + " was updated")


def orderCancelled(OrderId):
    listOfWebhooks = getListOfWebhooksFromFile()
    for webhook in listOfWebhooks:
        webhookUrl, eventType = webhook
        if eventType == "OrderCancelled":
            sendEventToWebhook(webhookUrl, eventType, "Order id: " + str(OrderId) + " was cancelled")
            
            
def orderPaid(OrderId):
    listOfWebhooks = getListOfWebhooksFromFile()
    for webhook in listOfWebhooks:
        webhookUrl, eventType = webhook
        if eventType == "OrderPaid":
            sendEventToWebhook(webhookUrl, eventType, "Order id: " + str(OrderId) + " was paid")
            
            
def orderFulfilled(OrderId):
    listOfWebhooks = getListOfWebhooksFromFile()
    for webhook in listOfWebhooks:
        webhookUrl, eventType = webhook
        if eventType == "OrderFulfilled":
            sendEventToWebhook(webhookUrl, eventType, "Order id: " + str(OrderId) + " was fulfilled")


### Test code for generating events with random order ids every 60 seconds cycling through all event types
if __name__ == "__main__":
    while(True):
        time.sleep(60)
        orderCreated(random.randint(10000, 99999))
        time.sleep(60)
        orderUpdated(random.randint(10000, 99999))
        time.sleep(60)
        orderCancelled(random.randint(10000, 99999))
        time.sleep(60)
        orderPaid(random.randint(10000, 99999))
        time.sleep(60)
        orderFulfilled(random.randint(10000, 99999))