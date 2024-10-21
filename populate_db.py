import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cleanservice_project.settings')
django.setup()


from django.core.files import File
from app.models import Category, Cloth  # Импортируйте вашу модель


def populate():
    # Path to folder with pictures
    images_dir = os.path.join('static', 'media', 'initial_images')

    # add few categories
    check_categories = Category.objects.all()
    if len(check_categories) == 0:
        category_data = [
            {'name_category': 'Clothes'},
            {'name_category': 'Bedroom'},
            {'name_category': 'Bathroom'},
        ]
        for category in category_data:
            adding_name_category = category['name_category']
            if adding_name_category in check_categories:
                pass
            else:
                add_category = Category(name_category=adding_name_category)
                add_category.save()
    # add few things
    check_clothes = Cloth.objects.all()
    if len(check_clothes) == 0:
        objects_data = [
            {'name': 'Towel', 'price': 10, 'image_name': 'towel.png', 'category': Category.objects.get(name_category='Bathroom')},
            {'name': 'Pillow', 'price': 15, 'image_name': 'pillow.png', 'category': Category.objects.get(name_category='Bedroom')},
            {'name': 'Blanket', 'price': 20, 'image_name': 'blanket.png', 'category': Category.objects.get(name_category='Bedroom')},
            {'name': 'Coat', 'price': 30, 'image_name': 'coat.png', 'category': Category.objects.get(name_category='Clothes')},
        ]
        for data in objects_data:
            image_path = os.path.join(images_dir, data['image_name'])
            if os.path.exists(image_path):
                with open(image_path, 'rb') as img_file:
                    # Create object and add picture
                    obj = Cloth(name=data['name'], price=data['price'], category=data['category'])
                    obj.img.save(data['image_name'], File(img_file), save=True)
                    print(f'Added {data["name"]} with image {data["image_name"]}')


if __name__ == '__main__':
    populate()
