from flask import Flask, redirect, url_for, session, request, render_template # Flask framework - pip install flask
from flask_oauthlib.client import OAuth # Flask OAuth module - pip install flask-oauthlib
import credentials # Credientials file for storing secrets, without them to the repo.


#region Configuration
app = Flask(__name__)                                               # Create the Flask app.
app.config['GOOGLE_ID'] = credentials.google_client_id              # Set the Google client ID.
app.config['GOOGLE_SECRET'] = credentials.google_client_secret      # Set the Google client secret.
app.debug = True                                                    # Debug mode, should be disabled in production.
app.secret_key = 'development'                                      # Secret key for session management, used to sign the session cookie, should be changed to a random string in production.
oauth = OAuth(app)                                                  # Create the OAuth object, and pass the app to it.


# Create the Google OAuth object, and set the required parameters for the Google OAuth API.
google = oauth.remote_app(
    'google',                                                       # Name of the OAuth provider.
    consumer_key=app.config.get('GOOGLE_ID'),                       # The client ID from the Google API console.
    consumer_secret=app.config.get('GOOGLE_SECRET'),                # The client secret from the Google API console.
    request_token_params={'scope': 'email'},                        # The scope of the request, in this case we only need the email address.
    base_url='https://www.googleapis.com/oauth2/v1/',               # The base URL for the Google API.
    request_token_url=None,                                         # The request token URL, not used for Google.
    access_token_method='POST',                                     # The method to use to get the access token, Google uses POST.
    access_token_url='https://accounts.google.com/o/oauth2/token',  # The access token URL for Google.
    authorize_url='https://accounts.google.com/o/oauth2/auth',      # The authorization URL for Google.
)
#endregion


#region Routes
# Index page, accessible to everyone
@app.route('/')
def index():
    if is_logged_in(): # If user is logged in, display their email and profile picture, and a logout button.
        me = google.get('userinfo')
        return render_template('index.html', user_logged_in = True, user_email = me.data.get('email'), user_image=me.data.get('picture'))
    
    # Usernot logged in, display login button.
    return render_template('index.html', user_logged_in = False)


# Secret page, only accessible if logged in
@app.route('/secret')
def secret():
    if is_logged_in(): # If user is logged in, direct them to the secret page.
        return render_template('secret.html')
    
    # User not logged in, redirect to login page, and display a message.
    return render_template('index.html', message='Access denied, please log in to view the secret page.')


# Login, redirect to Google for authorization, Google will redirect back to the callback URL.
@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


# Logout, remove the token from the session, then redirect to the index page.
@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))


# Google Callback URL, Google will redirect back to this after authorization.
# This URL must be specified in the Google API console. https[:]//console.cloud.google[.]com/apis/credentials
@app.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    return redirect(url_for('index'))
#endregion


#region Functions
# Get the access token from the session.
@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


# Check if the user is logged in.
def is_logged_in():
    if 'google_token' in session and google.get('userinfo').data.get('verified_email'): # Check if the user is logged in and if the email is verified.
        return True
    else:
        return False
#endregion


#region Run
# Run the app, listen on all IPs on port 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
#endregion