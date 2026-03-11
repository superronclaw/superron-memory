#!/usr/bin/env python3
"""
Twitter/X Tweet Fetcher (No Login Required)
基於 Guest Token 攞取公開推文
"""

import requests
import json
import argparse
import csv
from datetime import datetime

# Guest Token 認證
AUTH_TOKEN = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'

def get_guest_token():
    """攞取 Guest Token"""
    headers = {
        'authorization': AUTH_TOKEN,
    }
    resp = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers)
    return resp.json()['guest_token']

def fetch_tweets(username, limit=100):
    """攞取推文"""
    guest_token = get_guest_token()
    
    headers = {
        'authorization': AUTH_TOKEN,
        'x-guest-token': guest_token,
    }
    
    # 攞用戶 ID
    user_url = 'https://api.twitter.com/graphql/SAMkL5y_N9pmahSw8yy6gw/UserByScreenName'
    params = {
        'variables': json.dumps({"screen_name": username}),
    }
    
    resp = requests.get(user_url, headers=headers, params=params)
    user_data = resp.json()
    user_id = user_data['data']['user']['rest_id']
    
    # 攞推文
    tweets_url = 'https://api.twitter.com/graphql/XicnWRbyQ3WgVY__VataBQ/UserTweets'
    tweets = []
    cursor = None
    
    while len(tweets) < limit:
        variables = {
            "userId": user_id,
            "count": min(100, limit - len(tweets)),
            "cursor": cursor,
        }
        
        params = {'variables': json.dumps(variables)}
        resp = requests.get(tweets_url, headers=headers, params=params)
        data = resp.json()
        
        timeline = data['data']['user']['result']['timeline_v2']['timeline']['instructions']
        entries = [e for inst in timeline if inst['type'] == 'TimelineAddEntries' for e in inst.get('entries', [])]
        
        for entry in entries:
            if entry['content']['entryType'] == 'TimelineTimelineItem':
                tweet = entry['content']['itemContent']['tweet_results']['result']
                legacy = tweet['legacy']
                tweets.append({
                    'id': tweet['rest_id'],
                    'text': legacy['full_text'],
                    'created_at': legacy['created_at'],
                    'retweets': legacy['retweet_count'],
                    'likes': legacy['favorite_count'],
                })
        
        # 攞下一頁 cursor
        cursor_entries = [e for e in entries if e['content'].get('cursorType') == 'Bottom']
        if not cursor_entries or len(tweets) >= limit:
            break
        cursor = cursor_entries[0]['content']['value']
    
    return tweets[:limit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch Twitter/X tweets without login')
    parser.add_argument('--username', required=True, help='Twitter username')
    parser.add_argument('--limit', type=int, default=100, help='Max tweets to fetch')
    parser.add_argument('--output', default='tweets.csv', help='Output file')
    
    args = parser.parse_args()
    
    print(f"[+] Fetching tweets from @{args.username}...")
    tweets = fetch_tweets(args.username, args.limit)
    
    with open(args.output, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'text', 'created_at', 'retweets', 'likes'])
        writer.writeheader()
        writer.writerows(tweets)
    
    print(f"[+] Saved {len(tweets)} tweets to {args.output}")
