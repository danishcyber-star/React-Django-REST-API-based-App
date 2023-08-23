from django.urls import path, include
# from .views import article_list, article_details
from .views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    # path('articles/', ArticleViewSets.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view())

    # path('articles/', views.article_list),
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),
]


# path('articles/', views.article_list)