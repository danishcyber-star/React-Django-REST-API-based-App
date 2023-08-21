from rest_framework import serializers
from .models import Article



# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     description = serializers.CharField(max_length=100)


#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
    

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)




class ArticleSerializer(serializers.ModelSerializer):
    # by default Model serializer provides create and update unlike serializer where we have to manually declare it
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']