import argparse

# The command parser
parser = argparse.ArgumentParser()

# Target:
#   - bbs: forum threads
#   - ask: question and answering
parser.add_argument("target", help="Choose the platform to crawl data from.",
                    choices=["bbs", "ask"])


# Parse arguments
args = parser.parse_args()

if args.target == "bbs":
    print("BBS")
elif args.target == "ask":
    print("ASK")
else:
    pass