from faker import Faker
from myapp.models import Product

fake = Faker()

def create_fake_product():
    """
    Create a fake Product instance with random data.
    """
    name = fake.word()
    category = fake.word()
    availability = fake.random_element(elements=("In stock", "Out of stock"))
    price = fake.random_number(digits=2)
    
    product = Product.objects.create(
        name=name,
        category=category,
        availability=availability,
        price=price
    )
    
    return product
