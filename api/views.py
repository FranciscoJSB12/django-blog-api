from .models import BlogPost
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import BlogPostSerializer
# from rest_framework.views import APIView

# Get All and Create One
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    #Custom method to delete all data
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get, Update and Delete One
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()    
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'

"""
class BlogPostList(APIView):
    def get(self, request, format=None):
        Get the title from the query parameters (if none, default to empty string)
        title = request.query_params.get("title", "")

        if title:
            Filter the queryset based on the title
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            If no title is provided, return all blog posts
            serializer = BlogPostSerializer(blog_posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
"""
