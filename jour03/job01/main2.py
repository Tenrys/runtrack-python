from os.path import dirname, abspath, join
from re import search
import xml.etree.ElementTree as ET

tree = ET.parse(join(dirname(abspath(__file__)), "..", "domains.xml"))
test = tree.getroot()

extensions = {}

for column in test.findall(".//column"):
  name = column.attrib.get("name")
  domain = column.text
  if name == "domain":
    extMatch = search("\.(\w+)$", domain)
    if extMatch:
      ext = extMatch.group(1)
      if ext:
        if not extensions.get(ext):
          extensions[ext] = 1
        else:
          extensions[ext] += 1

for ext, n in extensions.items():
  print(f"{n} domaines en .{ext}")