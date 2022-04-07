from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Category
from api.models import Product

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email')

class CategorySerializer(serializers.ModelSerializer):
	##user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	#user = serializers.StringRelatedField()
	user = UserSerializer(read_only=True)
	user_id = serializers.PrimaryKeyRelatedField(
		queryset=User.objects.all(),
		write_only=True,
		source='user'
	)
	class Meta:
		model = Category
		fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
	categories = CategorySerializer(read_only=True, many=True)
	categories_id = serializers.PrimaryKeyRelatedField(
		queryset=Category.objects.all(),
		write_only=True,
		source='categories',
		many=True
	)
	class Meta:
		model = Product
		#fields = '__all__'
		fields = ('id', 'name', 'price', 'categories', 'categories_id')
