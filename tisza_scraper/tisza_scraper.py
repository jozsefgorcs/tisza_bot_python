from bs4 import BeautifulSoup

from models.product import Product


def get_shoes(html_content, size):
    if(html_content is None):
        return []
    soup = BeautifulSoup(html_content,'html.parser')
    category_products = soup.find_all(class_='category__product')

    # Print the found elements
    result = []
    for product in category_products:
        link = product.find(class_='category__link')
        url = link.get("href")
        name = link.find("img").get("title")
        bdi = product.find("bdi")
        price = bdi.contents[0].strip()
        currency = bdi.select_one('span.woocommerce-Price-currencySymbol').text.strip()
        result.append(Product(
            url=url,
            name=name,
            price=price,
            currency=currency,
            size=size
        ))
    return result