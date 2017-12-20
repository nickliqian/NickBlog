from haystack import indexes
from article.models import Article


# 索引模型
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # title = indexes.CharField(model_attr='title')
    # content = indexes.CharField(model_attr='content')

    def get_model(self):
        return Article

    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.all()
