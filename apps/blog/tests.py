import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Post, Author


def create_author(name, age, email):
	"""
	Create a Author.
	"""
	return Author.objects.create(name=name, age=age, email=email)


def create_post(author, title, content, pub_date):
	"""
	Create a blog post.
	"""
	return Post.objects.create(author=author, title=title, content=content,
		pub_date=pub_date)


class TestPost(TestCase):

	def test_index_view_with_no_posts(self):
		"""
		if no posts exist, an appropriate message should be displayed.
		"""
		response = self.client.get(reverse("blog:index"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No blog posts available.")
		self.assertQuerysetEqual(response.context['post_list'], [])

	def test_index_view_with_post(self):
		"""
		Sites with creation date in the past should be displayed on the
		front page.
		"""
		author = create_author(name="John P.", age=30, email='test@test.com')
		create_post(author, title='New Post', content='Hello John. Nice to meet you.', 
			pub_date=timezone.now())
		
		response = self.client.get(reverse("blog:index"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(
			response.context['post_list'],
			['<Post: New Post>']
		)
