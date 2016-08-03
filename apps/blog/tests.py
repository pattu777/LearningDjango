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


def create_post(author, title, content, days=0):
	"""
	Create a blog post.
	"""
	pub_date = timezone.now() + datetime.timedelta(days)
	return Post.objects.create(author=author, title=title, content=content,
		pub_date=pub_date)


class TestIndexView(TestCase):
	def test_index_view_with_no_posts(self):
		"""
		if no posts exist, an appropriate message should be displayed.
		"""
		response = self.client.get(reverse("blog:index"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No blog posts available.")
		self.assertQuerysetEqual(response.context['post_list'], [])

	def test_index_view_with_one_post(self):
		"""
		A post created in the past should be displayed on the front page.
		"""
		author = create_author(name="John P.", age=30, email='test@test.com')
		create_post(author, title='New Post', content='Hello John. Nice to meet you.', 
			days=-30)

		response = self.client.get(reverse("blog:index"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(
			response.context['post_list'],
			['<Post: New Post>']
		)

	def test_index_view_with_multiple_posts(self):
		"""
		Multiple posts created in the past should be displayed on the front page.
		"""
		author = create_author(name="John P.", age=30, email='test@test.com')
		create_post(author, title='First Post', content="This is the first post.", 
			days=-10)
		create_post(author, title='Hello Post', content="Hello John. Nice to meet you.", 
			days=-15)
		#create_post(author, title='Hidden Post', content="This post won't be displayed.", 
		#	days=15)
		
		response = self.client.get(reverse("blog:index"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(
			response.context['post_list'],
			['<Post: First Post>', '<Post: Hello Post>']
		)


class TestDetailView(TestCase):
	def test_detail_view_with_future_post(self):
		"""
		Detail view should show appropriate message when no post is found.
		"""
		author = create_author(name="John P.", age=30, email='test@test.com')
		post = create_post(author, title='First Post', content='This is the first post.', 
			days=10)
		
		response = self.client.get(reverse("blog:detail", args=(post.id,)))
		self.assertEqual(response.status_code, 404)


	def test_detail_view_with_a_post(self):
		"""
		Detail view of a post should return it's content.
		"""
		author = create_author(name="John P.", age=30, email='test@test.com')
		post = create_post(author, title='First Post', content='This is the first post.', 
			days=-10)
		
		response = self.client.get(reverse("blog:detail", args=(post.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, post.title)
		