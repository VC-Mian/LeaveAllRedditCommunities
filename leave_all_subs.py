import praw
import time

client_id = 'INSERT CLIENT ID HERE'
client_secret = 'INSERT CLIENT SECRET HERE'
user_agent = 'Leave All Subs'
username = 'INSERT USERNAME HERE'
password = 'INSERT PASSWORD HERE'

# Initialize Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

# Fetch the list of joined subreddits
subreddits = reddit.user.subreddits(limit=None)

# Leave each subreddit
for subreddit in subreddits:
    print(f"Leaving: {subreddit.display_name}") # Prints name of subreddit left
    subreddit.unsubscribe() #Reddit's API method to unsubscribe from subreddits
    time.sleep(2) # wait 2 seconds after leaving each subreddit

print("Left all subreddits.")
