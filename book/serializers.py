from rest_framework import serializers
from . models import Author,Book,BookCategory


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


    def validate_name(self,value)    :
        if value[0].islower():
            raise serializers.ValidationError("Your First Letter must be captilized")
    def validate_age(self,value):
        if value <=18:
            raise serializers.ValidationError ("You are not eligble")


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'        