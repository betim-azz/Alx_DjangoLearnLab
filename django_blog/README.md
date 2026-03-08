# Django Blog Application

## Overview

A fully functional Django blog application with user authentication, post management, commenting system, tagging, and search functionality.

## Features

### User Authentication
- **Registration:** Users can create an account at `/register/`. The form requires a username, email, and password. It securely hashes passwords.
- **Login/Logout:** Handled at `/login/` and `/logout/` via Django's `LoginView` and `LogoutView`.
- **Profile Management:** Authenticated users can navigate to `/profile/` to update their username, email, bio, and upload a profile picture.

### Blog Post Management
- **Create Posts:** Authenticated users can create blog posts with title, content, and tags
- **Edit Posts:** Authors can edit their own posts
- **Delete Posts:** Authors can delete their own posts
- **View Posts:** All users can view published posts
- **Author-Only Access:** Only post authors can edit or delete their posts (enforced by `LoginRequiredMixin` and `UserPassesTestMixin`)

### Commenting System
- **Add Comments:** Authenticated users can comment on posts
- **Edit Comments:** Comment authors can edit their comments
- **Delete Comments:** Comment authors can delete their comments
- **View Comments:** All users can view comments on posts

### Tagging System
- **Multiple Tags:** Each post can have multiple tags
- **Tag Creation:** New tags are automatically created when adding posts
- **Tag Filtering:** Click on tags to view all posts with that tag
- **Tag Reusability:** Tags can be associated with multiple posts
- **Comma-Separated Input:** Enter tags as comma-separated values (e.g., "python, django, web")

### Search Functionality
- **Multi-Field Search:** Search across post titles, content, and tags
- **Case-Insensitive:** Searches work regardless of letter case
- **Partial Matching:** Finds posts containing the search term anywhere
- **Distinct Results:** Eliminates duplicate results

## Security

- **CSRF Protection:** All forms include `{% csrf_token %}` to prevent Cross-Site Request Forgery.
- **Password Hashing:** Django's default PBKDF2 algorithm handles all password security.
- **Access Control:** The `@login_required` decorator and `LoginRequiredMixin` restrict unauthorized access.
- **Author Verification:** `UserPassesTestMixin` ensures only post/comment authors can edit or delete their content.

## URL Structure

### Posts
- `/` - List all posts
- `/post/<int:pk>/` - View single post
- `/post/new/` - Create new post (login required)
- `/post/<int:pk>/update/` - Edit post (author only)
- `/post/<int:pk>/delete/` - Delete post (author only)

### Tags and Search
- `/tags/<str:tag_name>/` - View posts filtered by tag
- `/search/` - Search posts by title, content, or tags

### Comments
- `/post/<int:pk>/comments/new/` - Add comment to post (login required)
- `/comment/<int:pk>/update/` - Edit comment (author only)
- `/comment/<int:pk>/delete/` - Delete comment (author only)

### Authentication
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/profile/` - User profile management (login required)

## Installation and Setup

1. Clone the repository
2. Install dependencies: `pip install django`
3. Apply migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Run the server: `python manage.py runserver`

## How to Test

### Authentication
1. Navigate to `http://127.0.0.1:8000/register/` and create an account
2. Log in at `http://127.0.0.1:8000/login/`
3. Navigate to `http://127.0.0.1:8000/profile/` to test updating information

### Blog Posts
1. Click "New Post" to create a post
2. Add tags (comma-separated): "python, django, tutorial"
3. View your post and verify tags appear
4. Click "Edit" to modify the post
5. Click "Delete" to remove the post

### Tagging and Search
1. Create posts with various tags
2. Click on a tag to filter posts
3. Use the search bar to find posts by keywords or tags
4. See detailed documentation in `TAGGING_AND_SEARCH_DOCUMENTATION.md`

### Comments
1. Navigate to any post detail page
2. Click "Add Comment" to create a comment
3. Edit or delete your own comments

## Documentation

- **Tagging and Search Features:** See `TAGGING_AND_SEARCH_DOCUMENTATION.md` for comprehensive documentation on:
  - How to use tags
  - How to search for posts
  - Technical implementation details
  - Testing guidelines
  - Troubleshooting tips

## Models

### Post
- `title` - Post title (CharField)
- `content` - Post content (TextField)
- `published_date` - Auto-generated timestamp
- `author` - ForeignKey to User
- `tags` - ManyToManyField to Tag

### Tag
- `name` - Unique tag name (CharField, max 50 characters)

### Comment
- `post` - ForeignKey to Post
- `author` - ForeignKey to User
- `content` - Comment text (TextField)
- `created_at` - Auto-generated timestamp
- `updated_at` - Auto-updated timestamp

### Profile
- `user` - OneToOneField to User
- `image` - Profile picture (FileField)
- `bio` - User biography (TextField)

## Technologies Used

- Django 4.x
- Python 3.x
- SQLite (default database)
- Django's built-in authentication system
- Django's ORM for database queries

## Project Structure

```
django_blog/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       ├── post_confirm_delete.html
│   │       ├── posts_by_tag.html
│   │       ├── search_results.html
│   │       ├── comment_form.html
│   │       ├── comment_confirm_delete.html
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── register.html
│   │       └── profile.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── django_blog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
└── TAGGING_AND_SEARCH_DOCUMENTATION.md
```

## Contributing

This is a learning project for the ALX Django course.

## License

Educational project - ALX Software Engineering Program
