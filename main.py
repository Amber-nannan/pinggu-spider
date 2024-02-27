import argparse
from crawler.ask import AskCrawler


# The command parser
parser = argparse.ArgumentParser()

# Target:
#   - bbs: forum threads
#   - ask: question and answering
parser.add_argument("target", help="Choose the platform to crawl data from.",
                    choices=["bbs", "ask"])

# Parse arguments
args = parser.parse_args()

def main_ask():
    AskCrawler.crawl_ask()

if args.target == "bbs":
    print("BBS")
elif args.target == "ask":
    main_ask()
else:
    pass