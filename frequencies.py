import os
from lxml import etree
import re
from collections import Counter

patterns = {
    "hi": "[\u0915-\u0939]",
    "gu": "[\u0A95-\u0AB9]",
    "hy": "[\u0531-\u0556\u0561-\u0587\uFB13-\uFB17]",
}

# patterns = {
#     #"Gujarati": ("gu", ur"([^\u0930\W]\u094d.\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d[^\u0200\W])"),
#     "hi: "(.\u094d.\u094d.\u094d[^\u0200\W]|.\u094d.\u094d[^\u0200\W]|.\u094d[^\u0200\W])"),
#     #"Marathi": ("mr", ur"([^\u0930\W]\u094d.\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d[^\u0200\W])"),
#     #"Nepali": ("ne", ur"([^\u0930\W]\u094d.\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d[^\u0200\W])"),
#     #"Bengali": ("bn", ur"([^\u0930\W]\u094d.\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d.\u094d[^\u0200\W]|[^\u0930\W]\u094d[^\u0200\W])"),
# }

def main():
    datadir = "sourcedata/"

    for code, pattern in patterns.items():
        count = Counter()
        for xml in os.listdir(datadir):
            if xml.startswith(code):
                print("Parsing %s" % xml)
                RE = re.compile(pattern)
                for event, element in etree.iterparse(os.path.join(datadir, xml)):
                    if "text" in element.tag and element.text != None:
                        texter = (element.text)
                        characters = RE.findall(texter)
                        for character in characters:
                            count[character] += 1

        path = os.path.join("character-frequencies", "%s.txt" % code)
        with open(path, "w", encoding="utf-8") as cf:
            for character in sorted(count, key=count.get)[::-1]:
                cf.write("%s %s\n" % (count[character], character))
        print("-> saved to %s" % path)


if __name__ == "__main__":
    main()