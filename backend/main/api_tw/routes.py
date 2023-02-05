import tweepy
from flask import request, jsonify, Blueprint, redirect
from flask_jwt_extended import jwt_required
import os

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
    redirect_uri= "http://190.15.198.27:5000/tw/success",
    scope=["tweet.read", "tweet.write", "users.read", "offline.access"],
    # Client Secret is only necessary if using a confidential client
    client_secret="L_BUjZhgr75oFwPuqn6yEIkDshu-dms0jFNs7NrinJcQkWgJAM"
    )

tw = Blueprint('tw', __name__, url_prefix='/tw')


@tw.route("/upload", methods=["POST"])
@jwt_required()
def upload():
    file = request.files['image']
    file.save(os.getenv("UPLOAD_FOLDER") + file.filename)
    os.popen("cp " + str(os.getenv("UPLOAD_FOLDER")) + str(file.filename) + " /tmp/image_api_tw")
    file.save("/tmp/image_api_tw")
    return jsonify({'message': 'File uploaded successfully',
                    "url": oauth2_user_handler.get_authorization_url()
                    })

@tw.route("/success" ,methods=["GET"])
def success():
    access_token = oauth2_user_handler.fetch_token(str(request.url)[0:4]+"s"+str(request.url)[4:])
    # print(access_token)
    user_client = tweepy.Client(
        access_token["access_token"]
    )
    
    media = apitw.media_upload("/tmp/image_api_tw", additional_owners=[int(user_client._get_authenticating_user_id())])
    response_create_tw = user_client.create_tweet(text="Image upload from WebApp-MarcosRicciardi", media_ids=[media.media_id], user_auth=False)
    # print("tweet response_create_tw: " + str(response_create_tw.data['id']))
    # print("usuario: " + str(user_client.get_me(user_auth= False).data))
    return redirect("https://twitter.com/" + 
                    str(user_client.get_me(user_auth= False).data) + 
                    "/status/" + 
                    str(response_create_tw.data['id'])
                    )
