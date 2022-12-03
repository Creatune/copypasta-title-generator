import praw
import pandas as pd
from langdetect import detect

reddit = praw.Reddit(client_id = 'awQQIuPKloaAdhDgWbVMhVg',
                     client_secret = 'GUzHnXz3w096bgIptuAsWKWeSDUQtQw',
                     username='notLeakingMyUsername',
                     password='notLeakingMyPassword',
                     user_agent='notLeakingThisEither')

subreddit = reddit.subreddit('copypasta')

hot_copypastas = subreddit.top(time_filter="all")

posts = []

post_titles = ""

for p in hot_copypastas:
    try:
        if (not p.stickied):
            post_titles = post_titles + p.title + "\n"
            posts.append([p.title, p.score, p.id, p.created])
    except:
        continue

posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'created'])

print(post_titles)

posts.to_csv('/home/rjoshi/Desktop/reddit_post_generator/data/top_all_time.csv')

with open('/home/rjoshi/Desktop/reddit_post_generator/gpt-2/src/training.txt', 'w') as f:
    f.write(post_titles)

