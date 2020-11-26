import pandas as pd
import tweepy
import time
from covid import Covid

CONSUMER_KEY ='F67C19ozYx9W7b1L8ssGs2TAh'
CONSUMER_SECRET ='HcRtg1PumnD1cryxEKJoy5bEYfpOYhrx32hBbG9DMxPOTMUNNX'
ACCESS_KEY ='1331239074175221767-w8M0YCvwVN9C86WLomrdfOM7BXQnUy'
ACCESS_SECRET ='fV0Npz70LCarL7EQXa0tH05U8eWyOKGFg65CHqEDeEh75'

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)

FILE_NAME = 'lst_seen_id.txt'

def ret_lst_seen_id(file_name):
	f_read=open(file_name,'r')
	lst_seen_id=int(f_read.read().strip())
	f_read.close()                             
	return lst_seen_id

def store_lst_seen_id(lst_seen_id,file_name):
	f_write=open(file_name,'w')
	f_write.write(str(lst_seen_id))
	f_write.close()
	return

def reply_to_tweets():
	lst_seen_id=ret_lst_seen_id(FILE_NAME)
	mentions=api.mentions_timeline(lst_seen_id,tweet_mode='extended')
	for mention in reversed(mentions):
		print(str(mention.id)+'-'+mention.full_text)
		lst_seen_id=mention.id
		store_lst_seen_id(lst_seen_id,FILE_NAME)

		if '#heyabhishek' in mention.full_text.lower():
			print('Found the hashtag')
			print('Responding back..')
			name=mention.user.name
			api.update_status('@' + mention.user.screen_name + ' hey '+ name + ', hope you are doing good, Be safe and Wear a mask :)', mention.id)
		
		if '#anime' in mention.full_text.lower():
			print("Giving feedback")
			name=mention.user.name
			api.update_status('@' + mention.user.screen_name + ' Well , for me Attack On Titan is the best anime series followed by Naruto !! Goodbye ' \
                        + name + '', mention.id)
		
		if '#followme' in mention.full_text.lower():
			print("Responding")
			mention.user.follow()
			api.update_status('@' + mention.user.screen_name + ' Done :)', mention.id)

		if '#covid' in mention.full_text.lower():
                        print("responding")
                        covid = Covid()
                        ind=covid.get_status_by_country_name("india")
                        name=mention.user.name
                        api.update_status('@' + mention.user.screen_name + ' hi ' + name + '\n' 'The confirmed cases are : ' + str(ind['confirmed']) + '\n' \
                        'Be safe and Wear a mask :)', mention.id)
                        


while True:
	reply_to_tweets()
	time.sleep(5)
