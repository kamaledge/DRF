from django.db.models import fields
from .models import Singer, Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'



class SingerSerializer(serializers.ModelSerializer):
    
    # Serializer Realtion based on model data
    # if this field is not defined and still related_name is used as fields = ['id', 'name', 'gender', 'song'], the song is is reflected
    
    # song = serializers.StringRelatedField(many=True, read_only=True) 
    # shows string related data of the releated field. Song is here the related name used in ForeignKey Parameter.
   
    
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only = True) 
    
    # song = serializers.HyperlinkedRelatedField(many=True, read_only = True, view_name='song-detail') # link to songs created
    # view_name is <modelname><-><detail>

    # song = serializers.SlugRelatedField(many=True, read_only = True, slug_field='duration')

    song = serializers.HyperlinkedIdentityField(view_name='song-detail') # view_name is <modelname><-><detail>
    
    
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']
        # fields = '__all__' # if fields mentioned explicitly, we must put song as the one in related_name