from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField



class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

class Category(models.Model):
	title=models.CharField(max_length=100)
	slug=models.SlugField(max_length=100, unique=True)
	image=models.ImageField(upload_to='images/category', blank=True)
	

	class Meta:
		verbose_name= 'category'
		verbose_name_plural='categories'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogapp:list_of_post_by_category',args=[self.slug])


# Create your models here.
class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title=models.CharField(max_length=250)
	slug=models.SlugField(max_length=250, unique_for_date='publish')
	image=models.ImageField(upload_to='images', blank=True)
	author=models.ForeignKey(User, related_name='blog_posts')
	body=RichTextUploadingField()
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	category=models.ManyToManyField(Category)


	objects=models.Manager()
	published=PublishedManager()


	class Meta:
		ordering = ('-publish',)

	def recent_publication(self):
		return self.publish <= timezone.now().date()
		"""return self.publish>=timezone.now().date()-datetime.timedelta(weeks=8)"""

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogapp:post_detail',args=[self.slug])

#Model Comment here
class Comment(models.Model):
	post=models.ForeignKey('blogapp.Post', related_name='comments')
	author=models.CharField(max_length=200)
	body=models.TextField()
	created=models.DateTimeField(default=timezone.now)
	updated=models.DateTimeField(auto_now=True)
	approved_comment=models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.author, self.post)

	

	
