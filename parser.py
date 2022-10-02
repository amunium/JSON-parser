import json

with open("DownUnderShop.JSON") as f:
    a = json.load(f)
    b = []
    for line in a["data"]:
        try: 
            b.append(line["useragent"])
        except:
            pass
    b = list(set(b))
    for line in b:
        print(line)