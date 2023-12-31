from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only":True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class UserLoginSerializers(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['role'] = user.role
        return token