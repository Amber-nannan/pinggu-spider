from bs4 import BeautifulSoup
import os
import json
import requests
import logging
import time

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

    base_URL = "https://bbs.pinggu.org/"
    thread_path = "thread/"
    if not os.path.exists(thread_path):
        os.makedirs(thread_path)

    @classmethod
    def get_thread_info(cls, thread_id:int) -> ThreadInfo:
        request_URL = f"{cls.base_URL}thread-{thread_id}-1-1.html"

        logging.info(f"Requesting Thread {thread_id}")
        while True:
            try:
                response = requests.get(request_URL)
                break
            except Exception as e:
                logging.error(f"Request Thread {thread_id} failed")
                time.sleep(1)

        soup = BeautifulSoup(response.text, 'html.parser')
        description = soup.find("div", class_="post_content")
        title = soup.find("h1", class_="ts")
        if description is None or title is None:
            return None
        description = description.text.strip()
        title = title.text.strip()
        return ThreadInfo(thread_id=thread_id,
                          title=title,
                          description=description)
    
    @classmethod
    def crawl_thread(cls, start_id:int=1, end_id:int=11746818, chunk_size:int=20):
        """Retrieve thread information from id range of [start_id, end_id),
        save on every 1000 threads."""
        while start_id < end_id:
            chunk_limit = min(start_id + chunk_size, end_id)
            file_name = f"thread-from-{start_id}-to-{chunk_limit}.json"
            file_path = os.path.join(cls.thread_path, file_name)

            if not os.path.exists(file_path):
                threads = []
                for thread_id in range(start_id, chunk_limit):
                    thread_info = cls.get_thread_info(thread_id)
                    if thread_info is not None:
                        threads.append(thread_info.to_dict())
                        logging.info(f"Got thread_id: {thread_id}")
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(threads, file, indent=4, ensure_ascii=False)
                    logging.info(f"Thread {start_id}-{chunk_limit-1} saved to :{file_path}")
            else:
                logging.info(f"{file_name} already exists.")
            start_id += chunk_size

def main_thread():
    logging.info("Starting crawling thread...")
    ThreadCrawler.crawl_thread(start_id=1)
