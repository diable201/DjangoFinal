from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser
from core.models import Book, Journal, Genre
from core.serializers import BookSerializer, JournalSerializer, GenreSerializer


class BookViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer


class JournalViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return Journal.objects.all()

    def get_serializer_class(self):
        return JournalSerializer


class GenreViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer
