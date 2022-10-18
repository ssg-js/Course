from .models import Artist, Music
from rest_framework import serializers


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        field = ('id', 'name',)


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        pass


class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        field = ('id', 'title',)


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        pass