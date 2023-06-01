from .models import Article
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "text", "date", "author",)
        read_only_fields = ("id", "date",) #te ktorych nie chce dostawac przy wysyłaniu requesta

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
    email = serializers.EmailField(
        required = False,
        validators=[UniqueValidator(
            queryset = User.objects.all(),
            message = "A user with that email already exists."
        )]
    )
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "articles",)
        extra_kwargs = {
            "password": {"write_only":True},
        }

    def create(self, data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        else:
            if email:
                emailTaken = User.objects.filter(email=email).exists()
                if not emailTaken:
                    user = User.objects.create(username=username,email=email,password=password)
                else:
                    raise serializers.ValidationError("This email is already taken.")
            else:
                user = User.objects.create_user(username=username,password=password)
                
            return user
