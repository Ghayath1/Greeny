import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()



from faker import Faker 
import random
from products.models import Product , Brand , Category
from blog.models import Post

images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg']

def create_category(n):
    fake = Faker()
    for x in range(n):
        Category.objects.create(
         name = fake.name(),
         image = f"category/{images[random.randint(1,10)]}" 
        )
    print(f"{n} category was created successfully ... ")

def create_brand(n):
    fake = Faker()
    for x in range(n):
        Brand.objects.create(
         name = fake.name(),
         image = f"brand/{images[random.randint(1,10)]}" ,
         category = Category.objects.get(id=random.randint(1,30))
        )
    print(f"{n} brand was created successfully ... ")



def create_product(n):
    fake = Faker()
    flag = ['New','Feature','Sale']
    for x in range(n):
        Product.objects.create(
         name = fake.name(),
         subtitle = fake.text(max_nb_chars=300),
         description = fake.text(max_nb_chars=7000),
         sku = random.randint(100,1000000),
         price = round(random.uniform(20.99,99.99),2),  
         flag = flag[random.randint(0,2)],
         image = f"products/{images[random.randint(2,10)]}" ,
         category = Category.objects.get(id=random.randint(1,30)),
         brand = Brand.objects.get(id=random.randint(1,30))
        )
    print(f"{n} product was created successfully ... ")




# call 
create_category(30)
create_brand(30)
create_product(30)
# create_post(5)