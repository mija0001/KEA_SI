--- Task ---
Expose a frontend that allows users to log in / sign up. Use a service for federated identities that potentially provide SSO. 

Hand-in:
1.  Git link for the code. 
2.  Documentation that goes through step by step on how you set it up.
    The guide should be so detailed that anyone can follow it and reproduce the result. 

Hint: Many services for federated identities exist. Part of the assignment is to research them.
It would be a good idea to create a document that lists pros and cons and considerations during the research phase. 

Hint 2: If you are spending many hours implenting things yourself then you have likely misunderstood the assignment.
The goal is to integrate with an existing solution.


--- Solution ---
app.py - A Flask webserver, serving a index and a secret page, the secret page can only be accessed once the user has logged in via Google OAuth.

Instructions for setting up and running the application can be found in /doc/setup.md