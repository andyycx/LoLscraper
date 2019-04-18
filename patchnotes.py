import requests
from bs4 import BeautifulSoup
import re
import functools

f = open("lolpatches.txt", "w+")

r = requests.get("https://euw.leagueoflegends.com/en/news/game-updates/patch")
soup = BeautifulSoup(r.text, "html.parser")
last_patch = soup.find("div", "views-row views-row-1 views-row-odd views-row-first").text.strip()

for replacement in (("Notes", "Notes:\n"), ("notes", "Notes:\n")):
    last_patch = last_patch.replace(*replacement)
f.write(last_patch + "\n")

link = "https://euw.leagueoflegends.com" + soup.find("div", "views-row views-row-1 views-row-odd views-row-first").find("a").get("href")
f.write(link)

r = requests.get(link)
soup = BeautifulSoup(r.text, "html.parser")
contents = soup.find("div", id="patch-notes-container").text.strip()

f.write(contents.replace("\u21d2", "TO"))

f.close()
