from rest_framework import serializers
from rest_framework.compat import authenticate
from .models import User

class UserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(label='Email Address')
    password = serializers.CharField(write_only=True)
    user = None

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        users = User.objects.filter(email=email)
        user = users.first()
        if not users or not user.check_password(password):
            raise serializers.ValidationError("Email/Password is incorrect. Please try again.")

        self.user = user
        return data


class UserRegistrationSerializer(serializers.Serializer):
    """Serializer that creates a user"""

    email = serializers.EmailField(max_length=500)
    password1 = serializers.CharField(style={'input_type': 'password'})
    password2 = serializers.CharField(style={'input_type': 'password'})
    first_name = serializers.CharField(max_length=80)
    last_name = serializers.CharField(max_length=80)

    def validate(self, data):
        password1 = data['password1']
        password2 = data['password2']
        email = data['email']
        if password1 != password2:
            raise serializers.ValidationError("Password does not match")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return data

    def save(self):
        username=self.validated_data['email']
        password=self.validated_data['password1']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        user = User.objects.create(email=username,
                            first_name=first_name,
                            last_name=last_name)
        user.set_password(password)
        user.save()

class UserSerializer(serializers.ModelSerializer):
    """Serializer of a user"""
    
    class Meta:
        model = User
        fields = ('__all__')