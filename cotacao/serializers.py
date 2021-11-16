from rest_framework import serializers
from .models import Post

class CotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','dt_vl','vl_brl','vl_ien','vl_eur')