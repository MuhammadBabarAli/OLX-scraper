from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

URL = "https://www.olx.com.pk/"
categories = {
    0: 'none',
    1: 'vehicles_c5',
    2: 'mobiles_c1411',
    3: 'bikes_c1898',
    4: 'jobs_c4',
    5: 'furniture-home-decor_c628',
    6: 'fashion-beauty_c87',
    7: 'property-for-sale_c2',
    8: 'property-for-rent_c3',
    9: 'services_c619',
    10: 'animals_c103',
    11: 'electronics-home-appliances_c99',
    12: 'books-sports-hobbies_c767',
    13: 'kids_c88'
}

print("WELCOME TO OLX SCRAPER!")
print("""
0: NONE
1: VEHICLES
2: MOBILES
3: BIKES
4: JOBS
5: FURNITURE HOME DECOR
6: FASHION & BEAUTY
7: PROPERTY FOR SALE
8: PROPERTY FOR RENT
9: SERVICES
10: ANIMALS
11: ELECTRONICS & HOME APPLIANCES
12: BOOKS, SPORTS & HOBBIES
13: KIDS
""")
category_input = int(input(("Please select a category (or none) for your search: ")))
category = categories[category_input]

search = input("Enter search string: ")

def urlMaker(query, category):
    query_split = query.split(" ")
    query_with_dashes = "-".join(_ for _ in query_split)

    print(category)

    if category == "none":
        URL_query = f'{URL}/items/q-{query_with_dashes}'
    else:
        URL_query = f'{URL}/{category}/q-{query_with_dashes}'

    return URL_query

def extractHtml(body):
    soup = BeautifulSoup(body, "html.parser")
    return soup.prettify()

URL_complete = urlMaker(search, category)
print(URL_complete)
req = Request(URL_complete, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(req).read()
extracted_html = extractHtml(webpage)

print(extracted_html)
with open('extracted_html.txt', 'w', encoding='utf-8') as f:
    f.write(extracted_html)

