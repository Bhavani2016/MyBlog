from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blogapp.models import Post, Category,Comment
from .forms import CommentForm

# Create your views here.
def home(request):
	posts=Post.published.all()
	allCategory=Category.objects.all()
	
	# Show 3 posts per page
	paginator=Paginator(posts,3)
	page=request.GET.get('page')
	try:
		allPost = paginator.page(page)
	except PageNotAnInteger:
		#If page is not an integer, deliver first page
		allPost=paginator.page(1)
	except EmptyPage:
		#If page is out of range, deliver last page of results
		allPost=paginator.page(paginator.num_pages)

	return render(request, 'blogapp/home.html', {'posts':allPost, 'page': page, 'categorys':allCategory})

def post_detail(request,post):
	allCategory=Category.objects.all()
	#similarPost=get_object_or_404(Post, slug=category_slug, status='published')
	post= get_object_or_404(Post, slug=post,
								  status='published')

	#List of active comments for this post
	comments=post.comments.filter(approved_comment=True)
	if request.method == 'POST' :
		# A comment wast posted
		comment_form= CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment=comment_form.save(commit=False)
			#Assign the current post to the comment
			new_comment.post=post
			#Save the comment to the database
			new_comment.save()
	else:
		comment_form=CommentForm()

	return render(request, 'blogapp/detail.html', {'post': post, 'categorys':allCategory, 'comments':comments, 'comment_form':comment_form})


def list_of_post_by_category(request, category_slug):
	categories= Category.objects.all()
	post=Post.objects.filter(status='published')
	if category_slug:
		category=get_object_or_404(Category, slug=category_slug)
		post=post.filter(category=category)
	paginator=Paginator(post,3)
	page=request.GET.get('page')
	try:
		post = paginator.page(page)
	except PageNotAnInteger:
		#If page is not an integer, deliver first page
		post=paginator.page(1)
	except EmptyPage:
		#If page is out of range, deliver last page of results
		post=paginator.page(paginator.num_pages)
	return render(request, 'category/list_of_post_by_category.html', { 'post':post,'category':category, 'categories':categories})


	


