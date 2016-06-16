from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
	"""Show the first 7 posts."""
	post_list = Post.objects.order_by('-pub_date')[:7]
	context = {
		'post_list': post_list,
	}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	"""Show a particular blog post."""
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/detail.html', {'post': post})
