from django.db.models import CASCADE, CharField, ForeignKey, Model, \
    UniqueConstraint

from fpq_author.models import Author


class Quote(Model):
    author = ForeignKey(Author, CASCADE)
    phrase = CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.phrase

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['author', 'phrase'],
                name='Quote of author',
            ),
        ]
