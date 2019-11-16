# Instagram Clone Project
## root

> `GET /`

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
{
    "posts": "http://127.0.0.1:8000/posts/",
    "users": "http://127.0.0.1:8000/users/"
}
```
## 포스트 목록

> `GET /posts/`

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "url": "http://127.0.0.1:8000/posts/3/",
        "images": [],
        "comments": [
            {
                "id": 4,
                "content": "d",
                "created": "2019-11-14T15:16:28.449344+09:00",
                "post": 3,
                "author": 1
            },
            {
                "id": 5,
                "content": "dd",
                "created": "2019-11-14T15:24:47.264818+09:00",
                "post": 3,
                "author": 1
            }
        ],
        "created": "2019-11-13T18:51:01.636387+09:00",
        "content": "게시글 남겨봅니다.",
        "author": "http://127.0.0.1:8000/users/1/",
        "comment_count": 2,
        "like_count": 0
    }
]
```
## 포스트 조회

> `GET /posts/<int:pk>/`

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "url": "http://127.0.0.1:8000/posts/5/",
    "images": [],
    "comments": [],
    "created": "2019-11-14T15:58:35.782935+09:00",
    "content": "GitHub",
    "author": "http://127.0.0.1:8000/users/1/",
    "comment_count": 0,
    "like_count": 0
}
```
## 포스트 작성

> `POST /posts/`
>> param {"content":"내용"}

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Location: http://127.0.0.1:8000/posts/13/
Vary: Accept

{
    "url": "http://127.0.0.1:8000/posts/13/",
    "images": [],
    "comments": [],
    "created": "2019-11-14T16:06:05.283704+09:00",
    "content": "asdfasdf",
    "author": "http://127.0.0.1:8000/users/1/",
    "comment_count": 0,
    "like_count": 0
}
```
## 포스트 삭제

> `DELETE /posts/<int:pk>/`

```
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
## 포스트 좋아요

> `POST /posts/<int:pk>/likes/`

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
## 포스트 좋아요 취소

> `DELETE /posts/<int:pk>/unlikes/`

```
HTTP 204 No Content
Allow: DELETE, OPTIONS
Content-Type: application/json
Vary: Accept
```
## 댓글 조회

> `GET /posts/<int:pk>/comments/`

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "content": "test",
        "created": "2019-11-13T19:18:45.467223+09:00",
        "post": 4,
        "author": 1
    },
    {
        "id": 3,
        "content": "2번째 댓글",
        "created": "2019-11-13T19:21:37.141675+09:00",
        "post": 4,
        "author": 1
    }
]
```
## 댓글 작성

> `POST /posts/<int:pk>/comments/`
>> param {"content":"내용"}

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 6,
    "content": "댓글남기기",
    "created": "2019-11-14T16:11:05.365103+09:00",
    "post": 4,
    "author": 1
}
```
## 유저 리스트

> `GET /users/`

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "url": "http://127.0.0.1:8000/users/2/",
        "username": "SongTT",
        "email": "shg9411@nate.com",
        "profile": {
            "nickname": null,
            "profile_image": null,
            "bio": "",
            "phone": null,
            "like_posts": [],
            "followers_count": 1,
            "following_count": 0,
            "is_self": false,
            "following": true
        },
        "post_count": 1,
        "posts": [
            {
                "url": "http://127.0.0.1:8000/posts/4/",
                "images": [],
                "comments": [
                    {
                        "id": 2,
                        "content": "test",
                        "created": "2019-11-13T19:18:45.467223+09:00",
                        "post": 4,
                        "author": 1
                    },
                    {
                        "id": 3,
                        "content": "2번째 댓글",
                        "created": "2019-11-13T19:21:37.141675+09:00",
                        "post": 4,
                        "author": 1
                    },
                    {
                        "id": 6,
                        "content": "댓글남기기",
                        "created": "2019-11-14T16:11:05.365103+09:00",
                        "post": 4,
                        "author": 1
                    }
                ],
                "created": "2019-11-14T16:05:41.079775+09:00",
                "content": "asdfasdf77345e",
                "author": "http://127.0.0.1:8000/users/2/",
                "comment_count": 3,
                "like_count": 0
            }
        ]
    }
]
```
## 유저 조회

> `GET /users/<int:pk>/`

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "url": "http://127.0.0.1:8000/users/2/",
    "username": "SongTT",
    "email": "shg9411@nate.com",
    "profile": {
        "nickname": null,
        "profile_image": null,
        "bio": "",
        "phone": null,
        "like_posts": [],
        "followers_count": 1,
        "following_count": 0,
        "is_self": false,
        "following": true
    },
    "post_count": 1,
    "posts": [
        {
            "url": "http://127.0.0.1:8000/posts/4/",
            "images": [],
            "comments": [
                {
                    "id": 2,
                    "content": "test",
                    "created": "2019-11-13T19:18:45.467223+09:00",
                    "post": 4,
                    "author": 1
                },
                {
                    "id": 3,
                    "content": "2번째 댓글",
                    "created": "2019-11-13T19:21:37.141675+09:00",
                    "post": 4,
                    "author": 1
                },
                {
                    "id": 6,
                    "content": "댓글남기기",
                    "created": "2019-11-14T16:11:05.365103+09:00",
                    "post": 4,
                    "author": 1
                }
            ],
            "created": "2019-11-14T16:05:41.079775+09:00",
            "content": "asdfasdf77345e",
            "author": "http://127.0.0.1:8000/users/2/",
            "comment_count": 3,
            "like_count": 0
        }
    ]
}
```
## 유저 검색

> `GET /search/?username=username`
>> ?username=username

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "url": "http://127.0.0.1:8000/users/2/",
        "username": "SongTT",
        "email": "shg9411@nate.com",
        "profile": {
            "nickname": null,
            "profile_image": null,
            "bio": "",
            "phone": null,
            "like_posts": [],
            "followers_count": 1,
            "following_count": 0,
            "is_self": false,
            "following": true
        },
        "post_count": 1,
        "posts": [
            {
                "url": "http://127.0.0.1:8000/posts/4/",
                "images": [],
                "comments": [
                    {
                        "id": 2,
                        "content": "test",
                        "created": "2019-11-13T19:18:45.467223+09:00",
                        "post": 4,
                        "author": 1
                    },
                    {
                        "id": 3,
                        "content": "2번째 댓글",
                        "created": "2019-11-13T19:21:37.141675+09:00",
                        "post": 4,
                        "author": 1
                    },
                    {
                        "id": 6,
                        "content": "댓글남기기",
                        "created": "2019-11-14T16:11:05.365103+09:00",
                        "post": 4,
                        "author": 1
                    }
                ],
                "created": "2019-11-14T16:05:41.079775+09:00",
                "content": "asdfasdf77345e",
                "author": "http://127.0.0.1:8000/users/2/",
                "comment_count": 3,
                "like_count": 0
            }
        ]
    },
    {
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "SongHyeongGuen",
        "email": "shg9411@naver.com",
        "profile": {
            "nickname": "tt",
            "profile_image": null,
            "bio": "자기소개 수정",
            "phone": null,
            "like_posts": [],
            "followers_count": 0,
            "following_count": 1,
            "is_self": true,
            "following": false
        },
        "post_count": 9,
        "posts": [
            {
                "url": "http://127.0.0.1:8000/posts/3/",
                "images": [],
                "comments": [
                    {
                        "id": 4,
                        "content": "d",
                        "created": "2019-11-14T15:16:28.449344+09:00",
                        "post": 3,
                        "author": 1
                    },
                    {
                        "id": 5,
                        "content": "dd",
                        "created": "2019-11-14T15:24:47.264818+09:00",
                        "post": 3,
                        "author": 1
                    }
                ],
                "created": "2019-11-13T18:51:01.636387+09:00",
                "content": "게시글 남겨봅니다.",
                "author": "http://127.0.0.1:8000/users/1/",
                "comment_count": 2,
                "like_count": 0
            },
            {
                "url": "http://127.0.0.1:8000/posts/6/",
                "images": [],
                "comments": [],
                "created": "2019-11-14T16:00:38.009682+09:00",
                "content": "게시글 작성",
                "author": "http://127.0.0.1:8000/users/1/",
                "comment_count": 0,
                "like_count": 0
            },
            {
                "url": "http://127.0.0.1:8000/posts/7/",
                "images": [],
                "comments": [],
                "created": "2019-11-14T16:03:05.050073+09:00",
                "content": "게시글 작성",
                "author": "http://127.0.0.1:8000/users/1/",
                "comment_count": 0,
                "like_count": 0
            },
            {
                "url": "http://127.0.0.1:8000/posts/8/",
                "images": [],
                "comments": [],
                "created": "2019-11-14T16:05:50.956147+09:00",
                "content": "asdf",
                "author": "http://127.0.0.1:8000/users/1/",
                "comment_count": 0,
                "like_count": 0
            },
            {
                "url": "http://127.0.0.1:8000/posts/9/",
                "images": [],
                "comments": [],
                "created": "2019-11-14T16:06:01.766544+09:00",
                "content": "asdfasdf",
                "author": "http://127.0.0.1:8000/users/1/",
                "comment_count": 0,
                "like_count": 0
            },
            {
                "url": "http://127.0.0.1:8000/posts/10/",
                "images": [],
                "comments": [],
                "created": "2019-11-14T16:06:03.238513+09:00",
                "content": "asdfasdf",
                "author": "http://127.0.0.1:8000/users/1/",
                "comment_count": 0,
                "like_count": 0
            },
            {
                "url": "http://127.0.0.1:8000/posts/11/",
                "images": [],
                "comments": [],
                "created": "2019-11-14T16:06:04.021391+09:00",
                "content": "asdfasdf",
                "author": "http://127.0.0.1:8000/users/1/",
                "comment_count": 0,
                "like_count": 0
            },
            {
                "url": "http://127.0.0.1:8000/posts/12/",
                "images": [],
                "comments": [],
                "created": "2019-11-14T16:06:04.679340+09:00",
                "content": "asdfasdf",
                "author": "http://127.0.0.1:8000/users/1/",
                "comment_count": 0,
                "like_count": 0
            },
            {
                "url": "http://127.0.0.1:8000/posts/13/",
                "images": [],
                "comments": [],
                "created": "2019-11-14T16:06:05.283704+09:00",
                "content": "asdfasdf",
                "author": "http://127.0.0.1:8000/users/1/",
                "comment_count": 0,
                "like_count": 0
            }
        ]
    }
]
```
