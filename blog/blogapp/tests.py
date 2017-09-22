
from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Post

# Create your tests here.

class PostMethodTests(TestCase):

	def test_recent_pub(self):
		"""
		recent_publication() should return False for future publication dates """

		futuredate=timezone.now().date()+datetime.timedelta(days=5)
		future_pub=Post(publish=futuredate)
		self.assertEqual(future_pub.recent_publication(), False)


# Create your tests here.
