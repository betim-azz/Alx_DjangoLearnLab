# Likes and Notifications - API Documentation

## Overview
This document describes the likes and notifications functionality in the Social Media API, enabling users to like posts and receive real-time notifications for various interactions.

## Features

### Likes System
- Like/unlike posts
- Prevent duplicate likes
- Automatic notification to post author
- Track like timestamps

### Notifications System
- Notifications for new followers
- Notifications for post likes
- Notifications for post comments
- Read/unread status tracking
- Chronological ordering

## API Endpoints

### Likes Endpoints

#### 1. Like a Post
**Endpoint:** `POST /api/posts/<int:pk>/like/`

**Authentication:** Required (Token)

**Description:** Like a specific post. Creates a notification for the post author.

**Request:**
```http
POST /api/posts/1/like/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response (200 OK):**
```json
{
    "message": "Post liked successfully."
}
```

**Response (400 Bad Request) - Already Liked:**
```json
{
    "message": "You already liked this post."
}
```

**Notes:**
- Users cannot like their own posts (no notification created)
- Duplicate likes are prevented by unique constraint
- Notification is created only if post author is different from liker

#### 2. Unlike a Post
**Endpoint:** `POST /api/posts/<int:pk>/unlike/`

**Authentication:** Required (Token)

**Description:** Remove a like from a specific post.

**Request:**
```http
POST /api/posts/1/unlike/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response (200 OK):**
```json
{
    "message": "Post unliked successfully."
}
```

**Response (400 Bad Request) - Not Liked:**
```json
{
    "message": "You have not liked this post."
}
```

### Notifications Endpoints

#### 1. Get User Notifications
**Endpoint:** `GET /api/notifications/`

**Authentication:** Required (Token)

**Description:** Retrieve all notifications for the authenticated user, ordered by newest first.

**Request:**
```http
GET /api/notifications/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response (200 OK):**
```json
[
    {
        "id": 3,
        "actor": "johndoe",
        "verb": "liked your post",
        "timestamp": "2024-01-15T10:30:00Z",
        "is_read": false
    },
    {
        "id": 2,
        "actor": "janedoe",
        "verb": "commented on your post",
        "timestamp": "2024-01-15T09:15:00Z",
        "is_read": false
    },
    {
        "id": 1,
        "actor": "bobsmith",
        "verb": "started following you",
        "timestamp": "2024-01-14T14:20:00Z",
        "is_read": true
    }
]
```

**Response Fields:**
- `id` - Notification ID
- `actor` - Username of the user who performed the action
- `verb` - Description of the action
- `timestamp` - When the notification was created
- `is_read` - Whether the notification has been read

## Models

### Like Model
**Location:** `posts/models.py`

**Fields:**
- `user` - ForeignKey to User (who liked)
- `post` - ForeignKey to Post (what was liked)
- `created_at` - DateTime (when liked)

**Constraints:**
- `unique_together = ('post', 'user')` - Prevents duplicate likes

**Example:**
```python
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('post', 'user')
```

### Notification Model
**Location:** `notifications/models.py`

**Fields:**
- `recipient` - ForeignKey to User (who receives notification)
- `actor` - ForeignKey to User (who performed action)
- `verb` - CharField (action description)
- `target` - GenericForeignKey (related object)
- `content_type` - ForeignKey to ContentType
- `object_id` - PositiveIntegerField
- `timestamp` - DateTimeField (auto_now_add)
- `is_read` - BooleanField (default=False)

**Example:**
```python
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="actions")
    verb = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
```

## Notification Triggers

### 1. New Follower
**Trigger:** User A follows User B
**Notification to:** User B
**Verb:** "started following you"
**Code Location:** `accounts/views.py` - `FollowUserView`

### 2. Post Liked
**Trigger:** User A likes User B's post
**Notification to:** User B (post author)
**Verb:** "liked your post"
**Code Location:** `posts/views.py` - `like_post`

### 3. Post Commented
**Trigger:** User A comments on User B's post
**Notification to:** User B (post author)
**Verb:** "commented on your post"
**Code Location:** `posts/views.py` - `CommentViewSet.perform_create`

## Testing Examples

### Test Scenario 1: Like a Post

```bash
# Step 1: Create a post (as user1)
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Authorization: Token USER1_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Post","content":"This is a test post"}'

# Step 2: Like the post (as user2)
curl -X POST http://127.0.0.1:8000/api/posts/1/like/ \
  -H "Authorization: Token USER2_TOKEN"

# Step 3: Check notifications (as user1)
curl -X GET http://127.0.0.1:8000/api/notifications/ \
  -H "Authorization: Token USER1_TOKEN"
```

### Test Scenario 2: Follow and Comment

```bash
# Step 1: User2 follows User1
curl -X POST http://127.0.0.1:8000/api/accounts/follow/1/ \
  -H "Authorization: Token USER2_TOKEN"

# Step 2: User2 comments on User1's post
curl -X POST http://127.0.0.1:8000/api/comments/ \
  -H "Authorization: Token USER2_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"post":1,"content":"Great post!"}'

# Step 3: User1 checks notifications
curl -X GET http://127.0.0.1:8000/api/notifications/ \
  -H "Authorization: Token USER1_TOKEN"
```

### Test Scenario 3: Prevent Duplicate Likes

```bash
# Like a post
curl -X POST http://127.0.0.1:8000/api/posts/1/like/ \
  -H "Authorization: Token USER_TOKEN"

# Try to like again (should fail)
curl -X POST http://127.0.0.1:8000/api/posts/1/like/ \
  -H "Authorization: Token USER_TOKEN"

# Unlike the post
curl -X POST http://127.0.0.1:8000/api/posts/1/unlike/ \
  -H "Authorization: Token USER_TOKEN"
```

## Python Testing Script

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# User tokens (get from login)
user1_token = "token1"
user2_token = "token2"

# User2 likes User1's post
response = requests.post(
    f"{BASE_URL}/api/posts/1/like/",
    headers={"Authorization": f"Token {user2_token}"}
)
print("Like response:", response.json())

# User1 checks notifications
response = requests.get(
    f"{BASE_URL}/api/notifications/",
    headers={"Authorization": f"Token {user1_token}"}
)
print("Notifications:", response.json())

# User2 unlikes the post
response = requests.post(
    f"{BASE_URL}/api/posts/1/unlike/",
    headers={"Authorization": f"Token {user2_token}"}
)
print("Unlike response:", response.json())
```

## Postman Collection

```json
{
    "info": {
        "name": "Likes and Notifications",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Like Post",
            "request": {
                "method": "POST",
                "header": [{"key": "Authorization", "value": "Token {{token}}"}],
                "url": "http://127.0.0.1:8000/api/posts/1/like/"
            }
        },
        {
            "name": "Unlike Post",
            "request": {
                "method": "POST",
                "header": [{"key": "Authorization", "value": "Token {{token}}"}],
                "url": "http://127.0.0.1:8000/api/posts/1/unlike/"
            }
        },
        {
            "name": "Get Notifications",
            "request": {
                "method": "GET",
                "header": [{"key": "Authorization", "value": "Token {{token}}"}],
                "url": "http://127.0.0.1:8000/api/notifications/"
            }
        }
    ]
}
```

## Error Handling

### Common Errors

**401 Unauthorized:**
```json
{
    "detail": "Authentication credentials were not provided."
}
```
**Solution:** Include valid token in Authorization header

**404 Not Found:**
```json
{
    "detail": "Not found."
}
```
**Solution:** Verify post ID exists

**400 Bad Request:**
```json
{
    "message": "You already liked this post."
}
```
**Solution:** Check if already liked before attempting to like

## Database Schema

### Likes Table
```sql
CREATE TABLE posts_like (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    created_at DATETIME NOT NULL,
    UNIQUE(post_id, user_id),
    FOREIGN KEY(user_id) REFERENCES accounts_customuser(id),
    FOREIGN KEY(post_id) REFERENCES posts_post(id)
);
```

### Notifications Table
```sql
CREATE TABLE notifications_notification (
    id INTEGER PRIMARY KEY,
    recipient_id INTEGER NOT NULL,
    actor_id INTEGER NOT NULL,
    verb VARCHAR(255) NOT NULL,
    content_type_id INTEGER,
    object_id INTEGER,
    timestamp DATETIME NOT NULL,
    is_read BOOLEAN DEFAULT 0,
    FOREIGN KEY(recipient_id) REFERENCES accounts_customuser(id),
    FOREIGN KEY(actor_id) REFERENCES accounts_customuser(id),
    FOREIGN KEY(content_type_id) REFERENCES django_content_type(id)
);
```

## Performance Considerations

### Indexing
- Add index on `notifications.recipient_id` for faster queries
- Add index on `notifications.timestamp` for ordering
- Add index on `likes.post_id` for counting likes

### Optimization
```python
# Count likes efficiently
post.likes.count()

# Get unread notifications count
user.notifications.filter(is_read=False).count()

# Prefetch related data
Notification.objects.select_related('actor', 'recipient').filter(recipient=user)
```

## Security

### Authentication
- All endpoints require token authentication
- Users can only like posts once
- Users cannot like their own posts (no notification)

### Authorization
- Users can only view their own notifications
- Users can only unlike posts they have liked

### Validation
- Post existence validated before like/unlike
- User authentication verified
- Duplicate likes prevented by database constraint

## Best Practices

### For Frontend Developers

1. **Real-time Updates:** Poll notifications endpoint every 30-60 seconds
2. **Badge Count:** Display unread notification count
3. **Like Button State:** Track liked posts to show correct button state
4. **Optimistic UI:** Update UI immediately, rollback on error

### For Backend Developers

1. **Avoid N+1 Queries:** Use `select_related()` and `prefetch_related()`
2. **Pagination:** Implement pagination for notifications
3. **Cleanup:** Periodically delete old read notifications
4. **Caching:** Cache notification counts

## Future Enhancements

- [ ] Mark notifications as read
- [ ] Delete notifications
- [ ] Notification preferences
- [ ] Email notifications
- [ ] Push notifications
- [ ] Notification grouping
- [ ] Like counts on posts
- [ ] Who liked a post endpoint

## Support

For issues or questions:
- Check the main API documentation
- Review Django ContentTypes framework: https://docs.djangoproject.com/en/stable/ref/contrib/contenttypes/
- Review the test cases in the repository
