def calculate_total(products, disccount):
    total = 0
    for product in products:
        total += product["price"] * (1 - disccount)
    return total


def test_calculate_total_with_empty_list():
    products = []
    assert calculate_total(products, 0.30) == 0


def test_calculate_total_with_single_product():
    products = [{"name": "Product 1", "price": 10}]
    assert calculate_total(products, 0.10) == 9


def test_calculate_total_with_products():
    products = [
        {"name": "Product 1", "price": 10},
        {"name": "Product 2", "price": 20},
        {"name": "Product 3", "price": 30},
    ]
    assert calculate_total(products, 0.20) == 48


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_products()
    print("All tests passed!")
