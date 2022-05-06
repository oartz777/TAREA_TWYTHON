from twython import Twython
from auth import  (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

twitter = Twython (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )



#Tweet para texto
#message= "Manchester"
#twitter.update_status(status=message)
#print("Tweeted: " + message)


#Tweet para imagen:
#message = "Liverpool"
#image = open ("liverpool.png" , "rb" )
#response = twitter.upload_media(media=image)              
#media_id = [response["media_id"]]              
#twitter.update_status(status=message, media_ids=media_id)
#print("Tweeted: " + message)

#Tweet para video:
message = "Gooool"
video = open ("gol5.mp4" , "rb" )
response = twitter.upload_video(media=video, media_type="video/mp4")              
media_id = [response["media_id"]]              
twitter.update_status(status=message, media_ids=media_id)
print("Tweeted: " + message)


