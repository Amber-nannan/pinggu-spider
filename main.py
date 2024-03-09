import argparse
import logging
from crawler.ask import AskCrawler, main_ask
from crawler.thread import ThreadCrawler, main_thread

logging.basicConfig(
    # filename="main.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',)

def get_args():
    # The command parser
    parser = argparse.ArgumentParser()
    # Target:
    #   - bbs: forum threads
    #   - ask: question and answering
    parser.add_argument("target", help="Choose the platform to crawl data from.",
                        choices=["thread", "ask"])
    return parser.parse_args()

args = get_args()
if args.target == "thread":
    main_thread()
elif args.target == "ask":
    main_ask()
else:
    pass