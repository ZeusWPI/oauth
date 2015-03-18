# Python 2.7 example with requests_oauthlib

from requests_oauthlib import OAuth2Session


client_id = 'your_client_id'
client_secret = 'your_secret'
redirect_uri = 'your_redirect_url'

authorize_url = 'https://kelder.zeus.ugent.be/oauth/oauth2/authorize/'
access_token_url = 'https://kelder.zeus.ugent.be/oauth/oauth2/token/'

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
authorization_url, state = oauth.authorization_url(authorize_url)

print 'Please go to %s and authorize access.' % authorization_url

authorization_response = raw_input('Enter the full callback URL: ')

# Use verify=False as we don't have our verified certs yet
token = oauth.fetch_token(access_token_url, authorization_response=authorization_response, client_secret=client_secret, verify=False)


print token