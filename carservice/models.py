# Create your models here.
# from CMS.settings import MEDIA_URL
from django.db import models
# from passlib.hash import pbkdf2_sha256
# from django.core.urlresolvers import reverse
from django.urls import reverse
# from somewhere import handle_uploaded_file
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime



class RandomID(models.Model):
	"""docstring for active"""
	def random_uid(obj):
		rmin = 10000
		rmax = 90000
		while True:
			uid = randint(rmin, rmax)
			res = obj.objects.get(iud = iud)
			if not res:
				return iud
		

# class User(models.Model):
# 	username = models.CharField(max_length=50)
# 	fullname = models.CharField(max_length=100)
# 	phone = models.CharField(max_length=100)
# 	password = models.CharField(max_length=500)
# 	permision = models.IntegerField()

# class User(User):
# 	"""docstring for Ủe"""
# 	phone = models.CharField(max_length=12)
# # 	permision = models.IntegerField()
		

# # class ManuFacturers(models.Model):
# # 	"""docstring for ClassName"""
# # 	dè __str__(self): 
# # 		return self.name
# # 	name = models.CharField(mã_length=32)
# # 	logo = models.ImageField(null = True, upload_to = 'images/avatar/', default = '/static/images/default.jpeg')
class Customer(models.Model):
	"""docstring for Customer"""
	def __str__(self):
		return self.cName
	cName = models.CharField(max_length=50) #Ten xe
	cAvatar = models.ImageField(blank = True, upload_to = 'avatar/', default = 'default/user.jpg')
	cPhone = PhoneNumberField()
	cAddress = models.CharField(max_length=100, blank = True) #Ten xe	
	cID = models.CharField(max_length=50, blank = True) #CMND 

class Car(models.Model):
	"""docstring for Car"""
	def __str__(self): return self.nameofcar + ' (' + self.carid + ')'
	MANU_CHOOSE = (('AUDI','AUDI'), ('BMW','BMW'), ('CHEVROLET','CHEVROLET'),('FORD','FORD'),('TOYOTA','TOYOTA'),( 'HONDA', 'HONDA'),('HYUNDAI','HYUNDAI') , ('ISUZU','ISUZU'),('KIA','KIA') , ('LAND ROVER','LAND ROVER'),('LEXUS','LEXUS') ,('MAZDA','MAZDA') , ('MERCEDES-BENZ','MERCEDES-BENZ'),('MITSUBISHI','MITSUBISHI') ,('NISSAN','NISSAN') , ('PEUGEOT','PEUGEOT'),('PORSCHE','PORSCHE') ,('RENAULT','RENAULT') , ('SUZUKI','SUZUKI'), ('VOLKSWAGEN','VOLKSWAGEN'), ('FUSO','FUSO'), ('HINO','HINO'), ('INFINITI','INFINITI'), ('JAGUAR','JAGUAR'), ('LAMBORGINI','LAMBORGINI'), ('LUXGEN','LUXGEN'), ('MASERATI','MASERATI'), ('MINI','MINI'), ('ROLLS ROYCE','ROLLS ROYCE'), ('SAMSUNG','SAMSUNG'), ('SUBARU','SUBARU'), ('SYM','SYM'), ('THACO','THACO'), ('VINAXUKI','VINAXUKI'), ('VOLVO','VOLVO'))
	carid = models.CharField(max_length=50)  #Bien so xe
	nameofcar = models.CharField(max_length=50) #Ten xe
	manufacturer = models.CharField(max_length=100) #Hang san xuat =>> models.ForeignKey(ManuFacturers, on_delete=models.CASCADE)#
	owner = models.CharField(max_length=100) #Chu so huu
	typecar = models.CharField(max_length=15)  #so cho ngoi
	yearofmanu = models.CharField(max_length=15) # nam san xuat
	avatar = models.ImageField(blank = True, upload_to = 'avatar/', default = 'default/car.jpg')
	locate_code =  models.CharField(max_length=50, default = '') # Ma dinh vi
	about_car = models.CharField(max_length=1000)

class Schedule(models.Model):
	"""docstring for Schedule"""
	def __str__(self): 
		return str(self.departure_day) + '->' + str(self.destination_day)
	def __iter__(self):
		return iter( self.customer) 
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	# guess_name = models.CharField(max_length=200) 
	# email = models.EmailField(default='example@gmail.com')
	
	# phone_number = PhoneNumberField()
	
	departure_day = models.DateField('date published')
	destination_day = models.DateField('date published')
	
	departure = models.CharField(max_length=500)  #noi xuat phat
	destination = models.CharField(max_length=500) # noi den
	
	departure_time = models.TimeField('date published')  # gio khoi hanh
	
	price = models.DecimalField(max_digits=10, decimal_places=2)
	deposit = models.DecimalField(max_digits=10, decimal_places=2) #tien coc
	status = models.BooleanField(default=False) #trang thai dat xe

class Driver(models.Model):
	"""docstring for Driver"""
	idcard = models.CharField(max_length=10)  #Chung minh nhan dan
	drivername = models.CharField(max_length=50)  #Ten tai xe
	address = models.CharField(max_length=200)  #Dia chi
	introduce = models.CharField(max_length=1000)  #Thong tin gio thieu
	birthday = models.DateField()  #Tuoi
	experience = models.IntegerField()  #Kinh nghiem
	avatar = models.ImageField(null = True, upload_to = 'avatar/', default = 'default/user.jpg')
	phone_number = PhoneNumberField()
class Cost(models.Model):
	"""docstring for Cosst"""
	
	schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
	total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default = 0) # tong doanh thu
	spent_oil = models.DecimalField(max_digits=10, decimal_places=2, default = 0)  #Tien xang dau
	spent_steersman =  models.DecimalField(max_digits=10, decimal_places=2, default = 0) # Tien tai xe
	spent_arises =  models.DecimalField(max_digits=10, decimal_places=2, default = 0) #Phi phat sinh



class Album(models.Model):
	"""docstring for Album"""
	def __str__(self): 
		return self.title
	title = models.CharField(max_length=200)
	decription = models.CharField(max_length=200)

class Photo(models.Model):
	"""docstring for Photo"""
	
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	path_img = models.FileField(upload_to =  'travel/', default = 'default/thumbnail.jpg', blank = True)
	comment_img = models.CharField(max_length=200)
	


class Content(models.Model):
	"""docstring for Content"""
	avatar = models.ImageField(upload_to = 'avatar/', default = 'default/car.jpg', blank = True)
	title = models.CharField(max_length=200)
	phone = PhoneNumberField()
	address = models.CharField(max_length=200)
	email = models.EmailField(default='nhanknth@gmail.com')
	link = models.CharField(max_length=200)
	summary = models.TextField() 

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('content_edit', kwargs={'pk': self.pk})
		# def form_valid(self, form):
		# 	handle_uploaded_file(request.FILES['file'])
		# 	return super().form_valid(form)
		# 	

class TypeNews(models.Model):
	"""docstring for TypeNews"""
	def __init__(self, arg):
		super(TypeNews, self).__init__()
		self.arg = arg
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

class Blog(models.Model):
	"""docstring for News"""
	# def __init__(self):
		# super(Blog, self).__init__()
		# return self.title
	title = models.CharField(max_length=200)
	typenews = models.ForeignKey(TypeNews, on_delete=models.CASCADE) 
	slug = models.SlugField(max_length=200)
	content = RichTextUploadingField(blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	dateSubmit = models.DateField('date published', default=datetime.date.today)
	view = models.IntegerField(default=0)
	def save(self):
		self.slug = slugify(self.title)
		super(Blog, self).save()
	def __str__(self):
		return '%s' % self.title

class Comment(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	title = models.CharField(max_length= 200)
	content = models.CharField(max_length=5000)
	comment = models.ForeignKey(Blog, on_delete=models.CASCADE)

