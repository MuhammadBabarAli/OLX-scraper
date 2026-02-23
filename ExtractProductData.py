from bs4 import BeautifulSoup


def extractProductData(body):
    soup = BeautifulSoup(body, "html.parser")

    titles = soup.findAll('div', attrs={'aria-label': 'Title'})
    titles_list = []
    for t in titles:
        titles_list.append(t.h2.text)

    prices = soup.findAll('div', attrs={'aria-label': 'Price'})
    prices_list = []
    for p in prices:
        prices_list.append(p.span.text)

    sub_titles = soup.findAll(attrs={'aria-label': 'Subtitle'})
    sub_titles_list = []
    for s in sub_titles:
        spans = s.findAll('span', attrs={'aria-label': True})
    for sl in spans:
        sub_titles_list.append(sl.span.text)

    locations = soup.findAll('span', attrs={'aria-label': 'Location'})
    locations_list = []
    for l in locations:
        locations_list.append(l.text)

    dates = soup.findAll('span', attrs={'aria-label': 'Creation date'})
    dates_list = []
    for d in dates:
        dates_list.append(d.text)

    print(titles_list)
    print(prices_list)
    print(sub_titles_list)
    print(locations_list)
    print(dates_list)


    return titles