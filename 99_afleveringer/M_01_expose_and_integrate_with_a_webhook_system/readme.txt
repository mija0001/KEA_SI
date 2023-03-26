--- Task ---
Work in pairs (two and two). Switch role between exposee and integrator. 

-Exposee
Create a way for the integrator to register and unregister webhooks of various type events. Don’t worry about authentication and authorization for this assignment. 
An event could be “payment received, payment processed” or “invoice processing, invoice completed” etc. You decide the theme of your system as long as you make it clear in the documentation.
It’s a good idea to save the registered endpoints in persistent storage. Don’t overthink it and Sqlite, Nedb or even just plaintext files are some of the excellent choices.  
You must create scripts that can be invoked which will update the integrators endpoint for certain types of event with certain types of data. A dummy payload is fine. 
You must create a ping event when a webhook has been registered. To help the integrator maybe you could create something that will call all the endpoints at random intervals. 

-Integrator
Create a script that registers endpoints.
Create a server where the endpoint is defined which is ready to received data from the webbhook.

-Hosting
The system must be deployed at one point but it’s not requirement for it to run for the exam.

-Documentation.
As always, all information on how to integrate should be clear via documentation.


--- Solution ---
/registrar/app.py - A server that serves a webpage interface for registering, listing and unregistering webhooks, aswell as API endpoints for registering and unregistering.
/publisher/main.py - A script that sends a randomized dummy event to the registered webhooks every 60 seconds.
/data/webhooks.csv - A CSV file for persistent storage of the registered webhooks, used by both the Registrar and Publisher.
/webhook/main.py - A server with a webhook endpoint that can receive events from the exposees webhook system.
/integrator_script/main.py - A script that can register or unregister the webhook with all event types to the exposees webhook system.
/documentation.html - The documentation on were to reach and how to use the webhook system.

The Registrar and Publisher were hosted on a Azure VM and the documentation was made available to the integrator, so they could test the system.
The Webhook and integrator_script were run locally using ngrok, to test the exposees system.

Note: since I never received access to my partners system, the integrator part of the assignment was done against my own system.