import argparse
import json
import sys
import os
import urllib.request


def fetch(user, no_cache=True):
    cache = []
    if not no_cache:
        if os.path.exists("suit_cache.json"):
            with open("suit_cache.json", encoding="utf-8") as fh:
                cache = json.load(fh)
            for item in cache:
                if item["Username"] == user or item["ID"] == user:
                    return item

    try:
        user = int(user)
        isid = True
    except Exception:
        isid = False

    if isid:
        fp = urllib.request.urlopen(f"https://sui.sid72020123.repl.co/get_user/{user}")
    else:
        fp = urllib.request.urlopen(f"https://sui.sid72020123.repl.co/get_id/{user}")

    response = json.loads(fp.read().decode("utf8"))
    fp.close()

    if response["Error"] == True:
        sys.exit(f"An error occured with SUI. Here's its response for context:\n{response}")

    if no_cache:
        print("Skipping caching as it is disabled")
    else:
        with open("suit_cache.json", "w", encoding="utf-8") as fh:
            if response not in cache:
                cache.append(response)
            json.dump(cache, fh)

    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenSUIT - An open source clone of SUIT.")
    parser.add_argument("-u", "--user", help="Can be a username or ID")
    parser.add_argument("-n", "--no-cache", action="store_true", help="Disables the local cache")
    parser.add_argument("-r", "--raw", action="store_true", help="Print out the raw json data")

    args = parser.parse_args()
    if args.user == None:
        user = input("Enter a username or ID: ")
    else:
        user = args.user

    info = fetch(user, args.no_cache)
    if args.raw:
        print(info)
    else:
        print(f"{info['Username']}: {info['ID']}")
