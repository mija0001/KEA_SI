import requests

registerWebhookUrl = "http://40.118.56.97:8080/api/registerwebhook" # The URL of the webhook service endpoint to register webhooks
unregisterWebhooksUrl = "http://40.118.56.97:8080/api/unregisterwebhook" # The URL of the webhook service endpoint to unregister webhooks
webhookUrl = "NGROK URL GOES HERE" # The URL of the webhook to register
listOfEventTypes = ["OrderCreated", "OrderUpdated", "OrderCancelled", "OrderPaid", "OrderFulfilled"] # The list of event types to register webhooks for

def registerWebhook(eventType):
    try:
        r = requests.post(registerWebhookUrl, json={"webhookUrl": webhookUrl, "eventType": eventType}, timeout=2)
        if r.status_code == 200:
            print("Successfully registered webhook for event type: " + eventType)
        else:
            print("Failed to register webhook for event type: " + eventType + " - status code: " + str(r.status_code))
    except:
        print("Failed to register webhook for event type: " + eventType + " request timed out")
        pass


def unregisterWebhook(eventType):
    try:
        r = requests.post(unregisterWebhooksUrl, json={"webhookUrl": webhookUrl, "eventType": eventType}, timeout=2)
        if r.status_code == 200:
            print("Successfully unregistered webhook for event type: " + eventType)
        else:
            print("Failed to unregister webhook for event type: " + eventType + " - status code: " + str(r.status_code))
    except:
        print("Failed to unregister webhook for event type: " + eventType + " request timed out")
        pass


def registerAllEventTypes(): # Register all webhooks for all event types, to test the webhook service
    for eventType in listOfEventTypes:
        registerWebhook(eventType)


def unregisterAllEventTypes(): # Unregister all webhooks for all event types, to clean up after testing
    for eventType in listOfEventTypes:
        unregisterWebhook(eventType)


if __name__ == "__main__":
    inputString = input("Enter 1 to register webhook for all event types, or 2 to unregister webhook for all event types: ")
    if inputString == "1":
        print("----- Attempting to register webhook for all event types -----")
        registerAllEventTypes()
        print("----- Done, exiting script -----")
    elif inputString == "2":
        print("----- Attempting to unregister webhook for all event types -----")
        unregisterAllEventTypes()
        print("----- Done, exiting script -----")
    else:
        print("Invalid input, exiting script")
