import json

with open("DownUnderShop.JSON") as f: # change name of file here.
    a = json.load(f)
    b = []
    for line in a["data"]: # search line by line within first tag
        try: 
            b.append(line["useragent"]) # which tag to print
        except:
            pass
    b = list(set(b)) # remove duplicates
    for line in b:
        print(line)