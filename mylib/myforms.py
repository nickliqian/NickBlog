from django.forms import ModelForm, Textarea
from article.models import Comment

from django.contrib.auth.forms import UserCreationForm
from account.models import Account


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['article', 'content', 'user_name', 'user_e_mail']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("username", "email")