import re
import urllib
import urllib.request
import sys
import os
import argparse

def search(searchquery, page=1, cats="0_0", filter=0):
    site = 'https://www.nyaa.se/'
    querystring = '?page=search&term='
    offsetstring = "&offset="
    categorystring = "&cats="
    filterstring = "&filter="
    query = searchquery
    http = urllib.request.urlopen(site+querystring+query+offsetstring+str(page)+categorystring+cats + filterstring + str(filter))
    html = http.read().decode('utf-8')
    names = []
    tids = []
    info = re.compile("<a href=\"//www\.nyaa\.se/\?page=view&#38;tid=(\d*?)\">(.*?)</a>")
    for title in info.finditer(html):
        tids.append(title.group(1))
        names.append(title.group(2))
    torrents = dict(zip(tids, names))
    return torrents


def downloadtorrents(torrents, path=""):
    for tid, title in torrents.items():
        download(tid, title, path)


def download(tid, name, path):
    # source: http://stackoverflow.com/a/31857152
    filename = cleanfilename(str(name))
    urllib.request.urlretrieve("https://www.nyaa.se/?page=download&tid=" + str(tid), path+filename+".torrent")


def openinclient(torrents):
    for tid, title in torrents.items():
        opentorrent(str(title))


def opentorrent(title):
    # source: https://stackoverflow.com/questions/434597/
    os.system("\"" + str(title) + ".torrent\"")


def cleanfilename(filename):
    # source: https://stackoverflow.com/questions/27647155/
    remove_punctuation_map = dict((ord(char), None) for char in '\/*?:"<>|')
    return filename.translate(remove_punctuation_map)


def main():
    if len(sys.argv) == 1:
        print("ERROR: No search terms")
        quit()
    try:
        page = sys.argv[2]
    except IndexError:
        page = None
    print("Searching \"" + sys.argv[1] + "\"")
    torrents = search(sys.argv[1], page)
    for tid, title in torrents.items():
        print(title)
    print("Found " + str(len(torrents)) + " titles.")
    input("Press enter to continue...")
    downloadtorrents(torrents)
    input("Press enter to attempt to open in torrent client...")
    openinclient(torrents)

parser = argparse.ArgumentParser(description="Downloads list of torrents from Nyaa.se based on a search query")
parser.add_argument('query', metavar='query', type=str, help="What to search for on Nyaa")
parser.add_argument('-p', metavar='page', type=int, help="Which page of results to grab from", default=1)
parser.add_argument('-c', metavar='category', type=str, help="Category numbers used by nyaa. To find these search something on nyaa and change the categorys. it will show as \"&cats=x_x\" in the url. For english only anime use 1_37", default="0_0")
parser.add_argument('-f', metavar='filter', type=int, help="Similar to category, shows as &filter=x in the url", default=0)
parser.add_argument('-o', metavar='outputdir', type=str, help="Where to download torrents", default="")
parser.add_argument('-s', help="Turn off messages (use this if you are getting errors related to codepage on windows)", action="store_true")
args = parser.parse_args()
torrents = search(args.query, page=args.p, cats=args.c, filter=args.f)
if not args.s:
    for tid, title in torrents.items():
        print(str(title) + " - " + str(tid))
    print("Found " + str(len(torrents)) + " titles.")
    input("Press enter to continue...")
downloadtorrents(torrents, args.o)

