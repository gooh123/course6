from rest_framework import serializers
from phonenumber_field import serializerfields

from skymarket.ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author_id")
    ad_id = serializers.ReadOnlyField(source="ad_id")
    author_first_name = serializers.ReadOnlyField(source="author_first_name")
    author_last_name = serializers.ReadOnlyField(source="author_last_name")

    class Meta:
        model = Comment
        fields = ("pk", "text", "created_at", "author_id", "ad_id", "author_first_name", "author_last_name")


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "image", "tittle", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author_first_name")
    author_last_name = serializers.ReadOnlyField(source="author_last_name")
    phone = serializerfields.PhoneNumberField(source="author_phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author_id")

    class Meta:
        model = Ad
        fields = (
         "pk", "image", "tittle", "price", "phone", "author_first_name", "author_last_name", "description", "author_id")
