import os
import tweepy
from main import create_app,request,redirect
app = create_app()
app.app_context().push()
from main import db


twitter_auth_keys = {
        "API_KEY"        : os.getenv("API_KEY"),
        "API_SECRET_KEY"     : os.getenv("API_SECRET_KEY"),
        "access_token"        : os.getenv("access_token"),
        "access_token_secret" : os.getenv("access_token_secret"),
    }
 
authO = tweepy.OAuthHandler(
        twitter_auth_keys['API_KEY'],
        twitter_auth_keys['API_SECRET_KEY']
        )
authO.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
        )
apitw = tweepy.API(authO)

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=os.getenv("CLIENT_ID"),
    redirect_uri= "http://127.0.0.1:5000/success",
    scope=["tweet.read", "tweet.write", "users.read", "offline.access"],
    # Client Secret is only necessary if using a confidential client
    client_secret="L_BUjZhgr75oFwPuqn6yEIkDshu-dms0jFNs7NrinJcQkWgJAM"
    )

@app.route("/")
def auth(): 
    return redirect(oauth2_user_handler.get_authorization_url())

@app.route("/success" ,methods=["GET"])
def success():
    access_token = oauth2_user_handler.fetch_token(str(request.url)[0:4]+"s"+str(request.url)[4:])
    print(access_token)
    user_client = tweepy.Client(
        access_token["access_token"]
    )
    
    media = apitw.media_upload("upload2.png", additional_owners=[int(user_client._get_authenticating_user_id())])
    user_client.create_tweet(text="No doy ma", media_ids=[media.media_id], user_auth=False)
    
    return access_token["access_token"]
	
if __name__ == '__main__':
	db.create_all()
	app.run(port = os.getenv("PORT"), debug = True)
#Cambios
