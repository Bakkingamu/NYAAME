# NYAAME
Nyaa torrents batch downloader

This script downloads all torrents returned by a search on nyaa.se

By default it gets everything on page 1 of the results.
Supports categories, filters, and different pages through arguments
### IF YOU ARE GETTING CODEPAGE ERRORS ON WINDOWS USE -s

# USAGE
`nyaame.py "query"`

query What to search for on Nyaa

-p Which page of results to grab from.

-c Category numbers used by nyaa.

-f Filter numbers used by nyaa.

-o Where to download torrents.

-s Turn off messages`

# EXAMPLE
This example will return the search results for "yuru yuri san hai" from the English-translated Anime category with the A+ only filter

All of these filters are taken directly from nyaa. To find out these categories and filters, play around with the category and filter dropdowns and check the url on the results page (&cats= ; &filter=)

`nyaame.py "yuru yuri san hai" -c "1_37" -f 3`

The script will list the titles of the torrents along with their ID on the website. Pressing enter will continue the script and download all the torrents to the current directory (or the give directory)
