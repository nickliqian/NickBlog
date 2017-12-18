from django.forms import ModelForm, Textarea
from article.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['article', 'content', 'user_name', 'user_e_mail']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 5}),
        }