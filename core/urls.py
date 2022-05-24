from django.urls import path
from rest_framework.routers import DefaultRouter
from core.views import BookViewSet, JournalViewSet, GenreViewSet


app_name = 'core'

router = DefaultRouter()

urlpatterns = [
    path(
        "books/",
        BookViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }),
        name="get/create books",
    ),
    path(
        "books/<int:pk>/",
        BookViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy"
            }),
        name="get/put/delete book",
    ),
    path(
        "journals/",
        JournalViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }),
        name="get/create journals",
    ),
    path(
        "journals/<int:pk>/",
        JournalViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy"
            }),
        name="get/put/delete journal",
    ),
    path(
        "genres/",
        GenreViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }),
        name="get/create genres",
    ),
    path(
        "genres/<int:pk>/",
        GenreViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy"
            }),
        name="get/put/delete genre",
    )
]

urlpatterns += router.urls
