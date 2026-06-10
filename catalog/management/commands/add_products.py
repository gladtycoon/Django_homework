from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Очищает таблицы Category и Product и заполняет их тестовыми данными"

    def handle(self, *args, **options):
        # Очистка таблиц
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write("Старые данные удалены.")

        # Создание категорий
        cat1 = Category.objects.create(
            name="Электроника", description="Техника и гаджеты"
        )
        cat2 = Category.objects.create(
            name="Книги", description="Художественная литература"
        )
        cat3 = Category.objects.create(
            name="Одежда", description="Мужская, женская, детская"
        )

        # Создание продуктов
        Product.objects.create(
            name="iPhone 99",
            description="Смартфон Apple",
            category=cat1,
            price=999999.00,
        )
        Product.objects.create(
            name="Ноутбук Huawei",
            description="Ultrabook",
            category=cat1,
            price=120000.00,
        )
        Product.objects.create(
            name="Война и мир", description="Толстой", category=cat2, price=2500.00
        )
        Product.objects.create(
            name="Футболка", description="Хлопок", category=cat3, price=750.00
        )

        self.stdout.write(self.style.SUCCESS("Тестовые продукты добавлены."))
