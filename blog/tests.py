from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Mark',
            email='mark@gmail.com',
            password='pass-word'
        )

        self.post = Post.objects.create(
            title='A good title',
            author=self.user,
            body='Nice body content'
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f"{self.post.body}", 'Nice body content')
        self.assertEqual(f"{self.post.author}", 'Mark')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        resp = self.client.get('/post/1/')
        no_resp = self.client.get('/post/1000/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, 'A good title')
        self.assertTemplateUsed(resp, 'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': "New title",
            'Body': "New text",
            'author': self.user.id,
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args=1), {
            'title': 'Updated title',
            'body': 'Updated text',
        })

        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=1))

        self.assertEqual(response.status_code, 302)
