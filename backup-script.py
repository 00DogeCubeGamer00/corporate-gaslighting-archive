import os
import json
import csv
from datetime import datetime
import praw

# CONFIGURATION
# To avoid hardcoding credentials in a public GitHub repository,
# we use environment variables. Set these on your local system before running.
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USERNAME = os.getenv("REDDIT_USERNAME")
PASSWORD = os.getenv("REDDIT_PASSWORD")
USER_AGENT = "DataPreservationScript:v1.0 (by /u/anonymous)"

def initialize_reddit():
    """Authenticates against the API using personal developer script keys."""
    if not all([CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD]):
        print("[!] Error: Missing required environment variables.")
        print("Ensure REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, and REDDIT_PASSWORD are set.")
        exit(1)
        
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        password=PASSWORD,
        user_agent=USER_AGENT
    )

def backup_history():
    print("[*] Contacting server... Bypassing UI layers.")
    reddit = initialize_reddit()
    user = reddit.user.me()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("backup_data", exist_ok=True)
    
    # 1. ARCHIVE COMMENTS
    comment_file = f"backup_data/comments_{timestamp}.csv"
    print(f"[*] Extracting comment logs to {comment_file}...")
    
    with open(comment_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Timestamp (UTC)", "Subreddit", "Permalinks", "Score", "Body"])
        
        # Pulls up to 1,000 of your most recent comments directly from the user object
        for comment in user.comments.new(limit=1000):
            created_utc = datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([
                comment.id,
                created_utc,
                comment.subreddit.display_name,
                f"https://reddit.com{comment.permalink}",
                comment.score,
                comment.body
            ])
            
    # 2. ARCHIVE POSTS / SUBMISSIONS
    post_file = f"backup_data/posts_{timestamp}.csv"
    print(f"[*] Extracting submission logs to {post_file}...")
    
    with open(post_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Timestamp (UTC)", "Subreddit", "Title", "URL/Permalink", "Score", "Content"])
        
        # Pulls up to 1,000 of your most recent post submissions
        for submission in user.submissions.new(limit=1000):
            created_utc = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
            content = submission.selftext if submission.is_self else submission.url
            writer.writerow([
                submission.id,
                created_utc,
                submission.subreddit.display_name,
                submission.title,
                f"https://reddit.com{submission.permalink}",
                submission.score,
                content
            ])

    print(f"[+] Success! Backup completed. Files safely stored inside '/backup_data'.")

if __name__ == "__main__":
    backup_history()