from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'post_list'

	def get_queryset(self):
		"""Return the last seven posts."""
		return Post.objects.order_by('-pub_date')[:7]


class DetailView(generic.DetailView):
	model = Post
	template_name = 'blog/detail.html'
