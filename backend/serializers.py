from rest_framework import serializers
from .models import User, UserProfile, Post, Image, Comment


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        comment = Comment.objects.create(
            post=validated_data.get('post'),
            author=validated_data.get('author'),
            content=validated_data.get('content'),
            created=validated_data.get('created')
        )
        return comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(source='image_set', many=True, read_only=True)
    comments = CommentSerializer(
        source='comment_set', many=True, read_only=True)
    comment_count = serializers.ReadOnlyField()
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('url', 'images', 'comments', 'images',
                  'created', 'content', 'author', 'comment_count', 'like_count')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        post = Post.objects.create(
            created=validated_data.get('created'),
            author=self.context['request'].user,
            content=validated_data.get('content')
        )
        for image_data in images_data.values():
            Image.objects.create(post=post, image=image_data)
        return post


class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    is_self = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ('nickname', 'profile_image', 'bio',
                  'phone', 'like_posts',
                  'followers_count', 'following_count', 'is_self', 'following')

    def get_is_self(self, user):
        if 'request' in self.context:
            request = self.context['request']
            if user.id == request.user.id:
                return True
            else:
                return False
        return False

    def get_following(self, obj):
        if 'request' in self.context:
            request = self.context['request']
            if obj in request.user.profile.following.all():
                return True
        return False


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    posts = PostSerializer(source='post_set', many=True, read_only=True)
    post_count = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password',
                  'profile', 'post_count', 'posts')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        userprofile = UserProfile.objects.create(user=user,
                                                 nickname=profile_data['nickname'],
                                                 profile_image=profile_data['profile_image'],
                                                 bio=profile_data['bio'],
                                                 phone=profile_data['phone'])
        # userprofile.followers.set(profile_data['followers'])
        # userprofile.following.set(profile_data['following'])
        # userprofile.like_posts.set(profile_data['like_posts'])
        # userprofile.like_comments.set(profile_data['like_comments'])
        # userprofile.save()

        #UserProfile.objects.create(user = user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()
        profile.profile_image = profile_data.get(
            'profile_image', profile.profile_image)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.nickname = profile_data.get('nickname', profile.nickname)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.followers.set(profile_data.get(
            'followers', profile.followers.all()))
        profile.following.set(profile_data.get(
            'following', profile.following.all()))
        profile.like_posts.set(profile_data.get(
            'like_posts', profile.like_posts.all()))
        profile.save()

        return instance
