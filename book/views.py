from rest_framework.views import APIView
from.models import Author,Book,BookCategory
from.serializers import AuthorSerializer,BookSerializers,CategorySerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


class BookList(APIView):
    @api_view(['GET'])
    def list(self,request):
        book = Book.objects.all()
        serializer = BookSerializers(book,many=True)
        return Response(serializer.data)
