from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('feed/', FeedView.as_view(), name='user_feed'),
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', like_post, name='like_post'),       # <-- exact path
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'), # <-- exact path
]