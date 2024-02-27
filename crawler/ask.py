from bs4 import BeautifulSoup
import os
import json
import requests

class AskPostInfo:

    def __str__(self):
        return f"question: {self.question}\ndescription:{self.description}"

    def __init__(self, ask_id:int, question: str, description: str):
        self.ask_id = ask_id
        self.question = question
        self.description = description
    
    def is_empty(self) -> bool:
        return self.question == "" and self.description == ""
    
    def to_dict(self) -> dict:
        return {
            "ask_id": self.ask_id,
            "question": self.question,
            "description": self.description,
        }

class AskCrawler:
    base_URL = "https://ask.pinggu.org/"
    ask_path = "ask/"
    @classmethod
    def get_ask_post_info(cls, ask_id:int) -> AskPostInfo:
        request_URL = f"{cls.base_URL}q-{ask_id}.html"
        response = requests.get(request_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        questionbox = soup.find("div", class_="questionbox")

        if questionbox is None:
            return None
         
        question = questionbox.find("div", class_="title").text.strip()
        description = questionbox.find("div", class_="description").text.strip()
        return AskPostInfo(ask_id=ask_id,
                           question=question,
                           description=description)
    
    @classmethod
    def crawl_ask(cls, start_id:int=1, end_id:int=666666, chunk_size:int=20):
        """Retrieve ask post information from id range of [start_id, end_id),
        save on every 1000 questions."""
        while start_id < end_id:
            chunk_limit = min(start_id + chunk_size, end_id)
            file_name = f"ask-from-{start_id}-to-{chunk_limit}.json"
            file_path = os.path.join(cls.ask_path, file_name)

            if not os.path.exists(file_path):
                ask_posts = []
                for id in range(start_id, chunk_limit):
                    ask_post_info = cls.get_ask_post_info(id)
                    if ask_post_info is not None:
                        ask_posts.append(ask_post_info.to_dict())
                with open(file_path, "w") as file:
                    json.dump(ask_posts, file, indent=4)
            else:
                pass
            start_id += chunk_size
        