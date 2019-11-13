from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Post, Image, User, Image, Comment, UserProfile
from .serializers import PostSerializer, UserSerializer, CommentSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class CommentList(APIView):
    def post(self, request, pk, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=Post.objects.get(pk=pk),
                            author=User.objects.get(pk=request.user.id))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        queryset = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class CommentDetail(APIView):
    def get_object(self, post_pk, comment_pk):
        try:
            return Comment.objects.get(post_id=post_pk, pk=comment_pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, post_pk, comment_pk):
        comment = self.get_object(post_pk, comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, post_pk, comment_pk, format=None):
        comment = self.get_object(post_pk, comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk, comment_pk, format=None):
        comment = self.get_object(post_pk, comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 유저1이 유저2를 팔로우하면 유저2도 유저1을 팔로우하게되는 현상 발생중
class FollowUser(APIView):
    def post(self, request, user_id, format=None):
        userP = UserProfile.objects.get(user=request.user)
        try:
            user_to_follow = UserProfile.objects.get(
                user=User.objects.get(id=user_id))
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        userP.following.add(user_to_follow)
        user_to_follow.followers.add(userP)
        return Response(status=status.HTTP_200_OK)

# 팔로우와 같은 현상 발생


class UnFollowUser(APIView):
    def post(self, request, user_id, format=None):
        userP = UserProfile.objects.get(user=request.user)
        try:
            user_to_unfollow = UserProfile.objects.get(
                user=User.objects.get(id=user_id))
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        userP.following.remove(user_to_unfollow)
        user_to_unfollow.followers.remove(userP)
        return Response(status=status.HTTP_200_OK)


class LikePost(APIView):
    def get(self, request, post_id, format=None):
        likes = Post.objects.get(id=post_id)
        like_ids = likes.likes_post.all()
        users = User.objects.filter(id__in=like_ids)
        serializer = UserSerializer(
            users, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id, format=None):
        user = request.user

        try:
            get_post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            already_like = UserProfile.objects.get(
                user=user,
                like_posts=get_post
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except UserProfile.DoesNotExist:
            new_like = UserProfile.objects.get(
                user=user
            )
            new_like.like_posts.add(get_post)
            new_like.save()
            return Response(status=status.HTTP_201_CREATED)


class UnLikePost(APIView):

    def delete(self, request, post_id, format=None):
        user = request.user
        try:
            already_like = UserProfile.objects.get(
                user=user,
                like_posts=post_id
            )
            already_like.like_posts.remove(post_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)


class Search(APIView):
    def get(self, request, format=None):
        username = request.query_params.get('username', None)
        if username is not None:
            users = User.objects.filter(username__istartswith=username)
            serializer = UserSerializer(
                users, many=True, context={'request': request})
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
