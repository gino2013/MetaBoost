"""
MetaBoost - Post to Threads via Official API
Requires: THREADS_USER_ID and THREADS_ACCESS_TOKEN in .env

Get tokens at: https://developers.facebook.com (add Threads product to your app)
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

USER_ID = os.getenv("THREADS_USER_ID")
TOKEN = os.getenv("THREADS_ACCESS_TOKEN")
BASE = "https://graph.threads.net/v1.0"


def post_text(text: str) -> dict:
    container = requests.post(
        f"{BASE}/{USER_ID}/threads",
        params={"media_type": "TEXT", "text": text, "access_token": TOKEN}
    ).json()

    result = requests.post(
        f"{BASE}/{USER_ID}/threads_publish",
        params={"creation_id": container["id"], "access_token": TOKEN}
    ).json()

    return result


def post_with_image(text: str, image_url: str) -> dict:
    container = requests.post(
        f"{BASE}/{USER_ID}/threads",
        params={
            "media_type": "IMAGE",
            "image_url": image_url,
            "text": text,
            "access_token": TOKEN
        }
    ).json()

    result = requests.post(
        f"{BASE}/{USER_ID}/threads_publish",
        params={"creation_id": container["id"], "access_token": TOKEN}
    ).json()

    return result


def get_insights(media_id: str) -> list:
    metrics = ["views", "likes", "replies", "reposts", "quotes"]
    r = requests.get(
        f"{BASE}/{media_id}/insights",
        params={"metric": ",".join(metrics), "access_token": TOKEN}
    ).json()
    return r.get("data", [])


if __name__ == "__main__":
    result = post_text("Hello from MetaBoost! 🐕 #MetaBoost")
    print(f"Posted: {result}")
