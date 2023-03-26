--- Task ---
Create an SSE example. 

We already created two during the class but create one in any language that you understand for the exam. 

--- Solution ---
/app.py - This is a flask webserver. The / index page contains an event listener, that receives messages sent via a form on the /sendmessage page.

OBS: Since flask's sse module uses Redis to cache the event stream, a Redis server should be running on localhost, ie. through Docker.