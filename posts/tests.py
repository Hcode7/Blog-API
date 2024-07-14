from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='test123')
        test_post = Post.objects.create(author=testuser1, title='title1', body='a body here')

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.author.username, 'testuser1')
        self.assertEqual(post.title, 'title1')
        self.assertEqual(post.body, 'a body here')
