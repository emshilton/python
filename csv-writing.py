import requests
from bs4 import BeautifulSoup
import csv


def get_product_links_from_categories(category_url, main_url, num_pages):
    '''
    goes through each category and finds product_url to put into per product function
    :param category_url: eg. 'http://lazada.sg/shop-category/?page='
    :param num_pages: number of pages to go through per category
    '''
    for i in range(1,num_pages+1):
        soup = BeautifulSoup(requests.get(category_url+str(i)).text, "html.parser")
        for link in soup.findAll('a', {'class': 'c-product-card__name'}):
            href = main_url + link.get('href')
            product_info(href)
    return


def product_info(product_url):
    '''
    identifies various needed information per product to put into store_product function: [id, name, details, rating, store, price, discount, img_url, comments]
    :param product_url: url to product
    '''
    soup = BeautifulSoup(requests.get(product_url).text, "html.parser")
    #print('from: ' + product_url)
    # Get product ID
    id = product_url.split('-')[-1][:-5]
    # Get product name	
    try:	
    	name = soup.find('h1', {'id' : 'prod_title'}).string.strip()
    except:
	return
    # Get product details
    details = ""
    for bullet in soup.find('ul', {'class': 'prd-attributesList ui-listBulleted js-short-description'}).findAll('span'):
        # if there is a string
        if bullet.string:
            details += "--" + bullet.string
    # Get product rating
    rating = soup.findAll('div', {'class': 'product-card__rating__stars '})
    if len(rating) != 0:
        rating = int(str(rating[0].findAll('div')[1].get('style')).split()[-1][:-1])
    else:
        rating = 0
    store = soup.findAll('a', {'class': 'product-fulfillment__item__link product__seller__name__anchor'})
    # when SOLD & FULFILLED BY Lazada no store link
    if len(store) == 0:
        store = 'Lazada'
    else:
        store = store[0].find('span').string.strip()
    # Get product price
    price = float(soup.find('span', {'id':'product_price'}).string)
    # Get product discount
    discount = soup.findAll('span', {'id': 'product_saving_percentage'})
    if len(discount) != 0:
        discount = float(discount[0].string[:-1])
    else:
        discount = 0
    # Get product image
    img_url = soup.findAll('img', {'class' : 'itm-img'})[-1].get('src')

    # Store data into the product table, returns True if successful
    store_product_info(soup, id, name, details, rating, store, price, discount, img_url)
    return

def store_comment_info(id, review_rating, review_title, review_details):

	return

def store_product_info(soup, id, name, details, rating, store, price, discount, img_url):
	with open('data-scrape.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
		try:	
			spamwriter.writerow([name])
			print name
		except:
			print 'Found an error' 
			
	return

if __name__ == "__main__":
    fd = open('data-scrape.csv', 'wb')
    fd.write( 'Name,')
    fd.close()
    main_url = 'http://www.lazada.sg'
    categories = ['computers-laptops', 'cameras', 'consumer-electronics',
                  'womens-fashion', 'men-fashion',
                  'large-appliances', 'small-kitchen-appliances', 'kitchen-dining',
                  'furniture', 'home-decor', 'housekeeping', 'storage-organisation', 'home-improvement',
                  'health-beauty', 'toys-games', 'exercise-fitness']
    for category in categories:
        cat_url = main_url + '/shop-' + category + '/?page='
        get_product_links_from_categories(cat_url, main_url, 2)






