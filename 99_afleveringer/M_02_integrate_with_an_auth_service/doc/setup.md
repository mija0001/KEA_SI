# OAuth example with Google
## Setup
### Setup the Google API client
First we need to setup a Google API client.
1. Go to https://console.cloud.google.com/apis/
2. Click 'Credentials' in the navigation pane.
3. Click 'Create Credential' -> 'OAuth client ID'
4. Select 'Application Type' -> 'Web application'
5. Enter a name for the app. (This is only for identification within the Google API portal)
6. Click 'Authorized JavaScript origins' -> 'ADD URI', and enter the domain/ip of the application. Since this is example is running on localhost, we will enter http://127.0.0.1/
7. Click 'Authorized redirect URIs' -> 'ADD URI', and enter the domain/ip + endpoint of the app callback endpoint. Since this is example is running on localhost, we will enter http://127.0.0.1/login/authorized/
8. Click 'Create'
9. Once the client has been created, copy the 'Client ID' and 'Client secret'.<br>These are the secrets used to authenticate the app to the Google OAuth service.

### Setup the application
1. Clone the files from the repository to you project folder.
2. On the same level as app.py, create a file names credentials.py, the files contents should be: 

(Replace square brackets with the secrets from the Google API client section)
```
    google_client_id = "[CLIENT-ID]"
    google_client_secret = "[CLIENT-SECRET]"
```
3. Open a terminal in the project folder, same level as app.py.
4. Enter: poetry init -n
5. Enter: poetry add flask flask-oauthlib
6. Enter: poetry shell
7. Enter: python app.py

The server is now be running, and is accessible at http://127.0.0.1:8000
