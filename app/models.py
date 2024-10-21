from django.db import models


class Category(models.Model):
	"""Name of cloth category"""
	name_category = models.CharField('Name of cloth category', max_length=200)

	def __str__(self):
		return self.name_category

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


class Cloth(models.Model):
	"""Name of cloth"""
	name = models.CharField('Cloth', max_length=100)
	price = models.FloatField('Cloth price', default=0)
	img = models.ImageField('Picture', upload_to='photo/')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cloth', verbose_name='Cloth category')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Cloth'
		verbose_name_plural = 'Clothes'


class Calculation(models.Model):
	data = models.JSONField()

	def __str__(self):
		return self.id


class Order(models.Model):
	"""Order"""
	date_create = models.DateTimeField(auto_now_add=True)
	customer_name = models.CharField('Name', max_length=100)
	email = models.EmailField('Email', max_length=100, blank=True, null=True)
	address = models.CharField('Address', max_length=250, blank=True, null=True)
	comment = models.TextField('Comment', max_length=250, blank=True, null=True)
	cost = models.IntegerField('Order cost', blank=True, null=True)
	calculation = models.IntegerField('Number of calculation', blank=True, null=True)
	order_list = models.TextField('Order list', max_length=1000, blank=True, null=True)

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'
