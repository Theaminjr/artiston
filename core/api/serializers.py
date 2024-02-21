from rest_framework import serializers
from core.models import User,Profile,Address

class AddressSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["detail"]

class ProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["full_name","email"]

class SignUpSerializer(serializers.ModelSerializer):
    profile = ProfileSerialzer()

    class Meta:
        model = User
        fields = ['phone_number','profile','password']

    def create(self, validated_data):
        user = User(phone_number=validated_data['phone_number'])
        user.set_password(validated_data['password'])
        user.save()
        profile =Profile(**validated_data['profile'],user=user)
        profile.save()
        return user

