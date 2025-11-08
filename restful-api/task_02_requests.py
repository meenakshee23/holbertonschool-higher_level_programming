#!/usr/bin/python3
"""This module simplifies HTTP communication and allows users 
to send HTTP requests using Python"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all post from JSONPlaceholder"""
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get("title"))
        else:
            print("Failed to fetch posts from the API.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")

def fetch_and_save_posts():
    """Fetches all post from JSONPlaceholder"""
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            posts = response.json()

            data = [
                {"id": post.get("id"), "title": post.get("title", ""), "body": post.get("body", "")}
                for post in posts
            ]

            with open("posts.csv", "w", newline="", encoding="utf-8") as file:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

            print("Posts saved to posts.csv")
        else:
            print("Failed to fetch posts from the API.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
    except (OSError, IOError) as e:
        print(f"Error writing to CSV file: {e}")
