from django.db.models import CharField, Model


class Tag(Model):
    name = CharField(max_length=30, null=False, unique=True)

    def __str__(self) -> str:
        return self.name
