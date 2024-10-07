from django.db.models import Model, DateField, CharField, EmailField, SET_NULL, ForeignKey


class Player(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = EmailField()
    phone = CharField(max_length=20)
    birth_date = DateField()

    team = ForeignKey('Team', on_delete=SET_NULL, null=True, related_name='players')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
