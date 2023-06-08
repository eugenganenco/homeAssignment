import requests

if __name__ == '__main__':
    products = []
    # stores the number of products already collected in the current price range
    productsRetrieved = 0
    url = 'https://api.ecommerce.com/products'
    params = {
        'minPrice': 0,
        'maxPrice': 10000
    }

    with requests.Session() as session:
        while params['maxPrice'] <= 100000:
            # I assume every request returns a different list of products. You can find the explanation in the Readme file.
            response = session.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                products.extend(data["products"])
                productsRetrieved += data["count"]

                if productsRetrieved == data["total"]:
                    productsRetrieved = 0
                    params["minPrice"] += 10000
                    params["maxPrice"] += 10000
            else:
                print('Request failed with status code:', response.status_code)

    print(f"Product list is: \n {products}")



