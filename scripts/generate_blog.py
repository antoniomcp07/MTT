import datetime
import os
import random

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(ROOT_DIR, "content", "posts")
DATE = datetime.datetime.now().strftime("%Y-%m-%d")

# change to AI-based generation
TOPICS = [
    "Latest Tech Trends", "AI in Daily Life", "Cybersecurity Tips",
    "Web Development Best Practices", "The Future of Cloud Computing",
    "Blockchain Explained", "Productivity Hacks", "Machine Learning Basics"
]

TOPIC = random.choice(TOPICS)
TOPIC_SLUG = TOPIC.lower().replace(" ", "-")  # Convert to URL-friendly format
SLUG = f"{TOPIC_SLUG}-{DATE}"  # Ensure uniqueness with date
POST_DIR = f"{BLOG_DIR}/{SLUG}"
os.makedirs(POST_DIR, exist_ok=True)

# Define the front matter for Hugo (Hinode-compatible)
BLOG_CONTENT = f"""---
title: "{TOPIC} - {DATE}"
date: {DATE}T10:00:00+00:00
draft: false
summary: "Automated blog post about {TOPIC} for {DATE}."
categories: ["Automation"]
tags: ["weekly", "tech"]
---

## {TOPIC}

🚀 This is an automatically generated blog post about **{TOPIC}** for {DATE}. Stay tuned for more updates!
"""

POST_FILE = f"{POST_DIR}/index.md"
if not os.path.exists(POST_FILE):
    with open(POST_FILE, "w") as file:
        file.write(BLOG_CONTENT)
    print(f"✅ Blog post created: {POST_FILE}")
else:
    print("⚠️ Blog post already exists. Skipping...")
