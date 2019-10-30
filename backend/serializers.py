from rest_framework import serializers
from .models import Post, Image
from .models import User, UserProfile


class PostSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('nickname','profile_image', 'bio', 'phone', 'followers',
                  'following', 'like_posts', 'like_comments')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url','username', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.profile_image = profile_data.get('profile_image', profile.profile_image)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.followers.set(profile_data.get('followers', profile.followers))
        profile.following.set(profile_data.get('following', profile.following))
        profile.like_posts.set(profile_data.get('like_posts', profile.like_posts))
        profile.like_comments.set(profile_data.get('like_comments', profile.like_comments))
        profile.save()

        return instance
