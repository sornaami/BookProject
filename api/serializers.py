from rest_framework.serializers import ModelSerializer



class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields=["bookname","price","pages","author"]