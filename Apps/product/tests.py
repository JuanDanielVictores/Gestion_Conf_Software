from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        Product.objects.create(
            name="Producto Test",
            price=99.99,
            description="Descripción de prueba"
        )

    def test_product_creation(self):
        """Verifica que el producto se cree correctamente"""
        product = Product.objects.get(name="Producto Test")
        self.assertEqual(product.name, "Producto Test")
        self.assertEqual(float(product.price), 99.99)

    def test_product_str(self):
        """Verifica el método __str__"""
        product = Product.objects.get(name="Producto Test")
        self.assertEqual(str(product), "Producto Test")

    def test_product_count(self):
        """Verifica que hay un producto en la BD"""
        count = Product.objects.count()
        self.assertEqual(count, 1)


class ProductViewTest(TestCase):
    def test_product_list_view(self):
        """Verifica que la vista de lista funciona"""
        url = reverse('product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/Product_list.html')
    def test_product_create_view(self):
        """Verifica que la vista de crear funciona"""
        url = reverse('product_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)