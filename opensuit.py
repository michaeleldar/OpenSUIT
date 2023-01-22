import sys, json, time
print("OpenSUIT - An open source clone of SUIT.")

flags = [] # --no-cache -n 

def parse_args():
    global flags
    args = sys.argv.__len__()
    if args == 1:
        username = input("Enter a username or user ID: ")
    elif args == 2:
        username = sys.argv[1]
    else:
        username = sys.argv[sys.argv.__len__() - 1]
        for x in range(0, sys.argv.__len__()):
            if x == 0:
                continue
            elif x == sys.argv.__len__():
                break
            else:
                if sys.argv[2] == "--no-cache" or sys.argv[2] == '-n':
                    flags.append("no-cache")
    return username

def fetch(user):
    try:
        user = int(user)
        isid = True
    except:
        isid = False
    import urllib.request
    if isid:
        fp = urllib.request.urlopen(f"https://sui.sid72020123.repl.co/get_user/{user}")
    else:
        fp = urllib.request.urlopen(f"https://sui.sid72020123.repl.co/get_id/{user}")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    return mystr

def parsefetch(data):
    jsondata = json.loads(data)
    if jsondata["Error"] == True:
        print("SUI encountered an error.")
        quit()
    return jsondata["Username"] + ": " + jsondata["ID"]



if __name__ == "__main__":
    uname = parse_args()
    print(parsefetch(fetch(uname)))

