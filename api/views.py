from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from api.serializers import BookSerializer
from Books.models import Book
# Create your views here.
#api/books-> for creating and listing all books

class BookList(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)

    def post(selfself,request):
        form=BookSerializer(request.POST)