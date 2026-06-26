"""
MetaBoost - Daily Engagement Bot
Auto-likes recent posts under target hashtags, with safe daily limits.

Requirements: pip install instagrapi python-dotenv
"""

import os
import random
import time
import logging
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("MetaBoost")

TARGET_HASHTAGS = ["shiba", "dogs", "petlover"]
DAILY_LIKE_LIMIT = 80
DAILY_FOLLOW_LIMIT = 15
DELAY_RANGE = (4, 10)          # seconds between actions


def get_client() -> Client:
    cl = Client()
    try:
        cl.load_settings("session.json")
        cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
    except Exception:
        cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
        cl.dump_settings("session.json")
    return cl


def run(cl: Client):
    liked = 0
    followed = 0

    for tag in TARGET_HASHTAGS:
        if liked >= DAILY_LIKE_LIMIT:
            break

        log.info(f"Scanning #{tag}...")
        medias = cl.hashtag_medias_recent(tag, amount=25)

        for media in medias:
            if liked >= DAILY_LIKE_LIMIT:
                break

            try:
                cl.media_like(media.id)
                liked += 1
                log.info(f"Liked {media.id} by @{media.user.username}  [{liked}/{DAILY_LIKE_LIMIT}]")

                if followed < DAILY_FOLLOW_LIMIT and random.random() < 0.15:
                    cl.user_follow(media.user.pk)
                    followed += 1
                    log.info(f"  → Followed @{media.user.username}  [{followed}/{DAILY_FOLLOW_LIMIT}]")

            except Exception as e:
                log.warning(f"Skipped {media.id}: {e}")

            time.sleep(random.uniform(*DELAY_RANGE))

    log.info(f"Done. Liked: {liked}  Followed: {followed}")


if __name__ == "__main__":
    cl = get_client()
    run(cl)
