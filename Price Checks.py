def priceCheck(products, productPrices, productSold, soldPrice):
    price_map = {}
    for i in range(len(products)):
        price_map[products[i]] = productPrices[i]
    error_count = 0
    for i in range(len(productSold)):
        if price_map[productSold[i]] != soldPrice[i]:
            error_count += 1
    return error_count

if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    products_count = int(input().strip())
    products = []
    for _ in range(products_count):
        products_item = input().strip()
        products.append(products_item)

    productPrices_count = int(input().strip())
    productPrices = []
    for _ in range(productPrices_count):
        productPrices_item = float(input().strip())
        productPrices.append(productPrices_item)

    productSold_count = int(input().strip())
    productSold = []
    for _ in range(productSold_count):
        productSold_item = input().strip()
        productSold.append(productSold_item)

    soldPrice_count = int(input().strip())
    soldPrice = []
    for _ in range(soldPrice_count):
        soldPrice_item = float(input().strip())
        soldPrice.append(soldPrice_item)

    result = priceCheck(products, productPrices, productSold, soldPrice)
    print(result)