from rest_framework.generics import ListAPIView
from blogapp.api.serializers import PostSerializer
from blogapp.models import Post


class PostListAPIView(ListAPIView):
	""" List of Blogs """
	queryset =Post.objects.all()
	serializer_class=PostSerializer