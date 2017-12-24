from django.forms import ModelForm, Textarea, CharField, Form
from DjangoUeditor.models import UEditorField
from article.models import Comment

from django.contrib.auth.forms import UserCreationForm
from account.models import Account


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['article', 'userOfComment', 'content']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 5}),
            # 'content': CharField(label="内容", widget=UEditorWidget(width=1000, height=300, imagePath="uploads/blog/images/", filePath='uploads/blog/files/', toolbars='besttome')),
        }


class CustomForm(Form):
    # description = UEditorField(verbose_name='abc', width=600, height=300, toolbars="full",
    #                             imagePath="uploads/blog/images/", filePath="uploads/blog/files/")
    # Description=UEditorField("描述",initial="abc",width=600,height=800)
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("username", "email")
