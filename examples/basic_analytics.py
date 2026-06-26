"""
MetaBoost - Basic Analytics Example
Fetches your last 20 posts and prints engagement stats.

Requirements: pip install instagrapi python-dotenv
Setup: create a .env file with IG_USERNAME and IG_PASSWORD
"""

import os
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()


def get_client() -> Client:
    cl = Client()
    try:
        cl.load_settings("session.json")
        cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
    except Exception:
        cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
        cl.dump_settings("session.json")
    return cl


def main():
    cl = get_client()
    username = os.getenv("IG_USERNAME")

    user_id = cl.user_id_from_username(username)
    info = cl.user_info(user_id)

    print(f"\n=== @{username} ===")
    print(f"Followers : {info.follower_count:,}")
    print(f"Following : {info.following_count:,}")
    print(f"Posts     : {info.media_count:,}")
    print()

    medias = cl.user_medias(user_id, amount=20)

    print(f"{'Date':<12} {'Likes':>6} {'Comments':>9} {'Eng%':>6}  Caption")
    print("-" * 70)

    for m in medias:
        eng = (m.like_count + m.comment_count) / max(info.follower_count, 1) * 100
        caption = (str(m.caption_text)[:35] + "...") if m.caption_text else "(no caption)"
        date = m.taken_at.strftime("%Y-%m-%d") if m.taken_at else "unknown"
        print(f"{date:<12} {m.like_count:>6} {m.comment_count:>9} {eng:>5.2f}%  {caption}")


if __name__ == "__main__":
    main()
