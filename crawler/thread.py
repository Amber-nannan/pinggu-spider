from bs4 import BeautifulSoup
import os
import json
import requests
import logging

class ThreadInfo:

    def __init__(self, thread_id: int, title: str, description: str):
        self.thread_id = thread_id
        self.title = title
        self.description = description
	
    def __str__(self):
        return f"title: {self.title}\ndescription: {self.description}"

    def to_dict(self):
        return {
			"thread_id": self.thread_id,
			"title": self.title,
			"description": self.description,
		}

class ThreadCrawler:
    pass

def main_thread():
    pass
