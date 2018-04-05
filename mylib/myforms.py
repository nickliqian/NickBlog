from django.forms import ModelForm, Textarea, CharField, Form
from article.models import Comment

from django.contrib.auth.forms import UserCreationForm
from account.models import Account


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['article', 'userOfComment', 'content']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class CustomForm(Form):
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("username", "email")
