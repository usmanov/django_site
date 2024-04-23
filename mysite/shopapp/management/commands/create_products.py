from django.core.management.base import BaseCommand

from mysite.shopapp.models import Product


class Command(BaseCommand):
    """
    Creates products table
    """

    def handle(self, *args, **options):
        self.stdout.write('Creating products')
        product_names = [
            "Laptop",
            "Desktop",
            "Smartphone",
        ]
        product = Product(name=product_names[0])
        product.save()
        # for product_name in product_names:
        #     products, created = Product.objects.get_or_create(name="asdfgh")
        #     self.stdout.write(f'Created product {products}')
        self.stdout.write(self.style.SUCCESS('Successfully created products'))

