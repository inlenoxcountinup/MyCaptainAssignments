import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)

    
    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')

    return soup

def get_detail_data(soup):
    
    try:
        title = soup.find('h1', id='itemTitle').text
        title = title.lstrip("Details about \xa0")
    except:
        title = ''

    
    try:
        p = soup.find('span', id='prcIsum').text.strip()
        currency, price = p.split(' ')
    except:
        currency = ''
        price = ''

    
    try:
        sold = soup.find('span', class_='vi-qtyS').find('a').text.strip().split(' ')[0].replace('\xa0', '')
    except:
        sold = ''

    data = {
        'title': title,
        'price': price,
        'currency': currency,
        'total_sold': sold
    }

    return data

def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    urls = [item.get('href') for item in links]
    urls = urls[1:]

    return urls

def main():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=iPhone&_sacat=0&LH_TitleDesc=0&rt=nc&_odkw=lego+star+wars+republic+gunship+set+7676&_osacat=0&LH_ItemCondition=3' # <-- ENTER SEARCH URL HERE
    numberOfHits = 15 
    sum = 0.0         
    numberOfValidItems = 0 
    average = 0.0     

    products = get_index_data(get_page(url))

    for link in products[0:numberOfHits]:
        data = get_detail_data(get_page(link))
        print(data)

        if (data['currency'] == 'US'):
            numberOfValidItems += 1
            sum +=  float(data['price'][1:]) 

    average = sum / numberOfValidItems
    print("\nThe average price of this item on Ebay is: $%.2f" % average) 

if __name__ == '__main__':
    main()
