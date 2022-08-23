from os import environ as env

from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class Quizzes(Model):

    class Meta:

        table_name: str = env['DYNAMODB_TABLE']
        region = 'ap-southeast-1'
        host = f'https://dynamodb.{region}.amazonaws.com'

    device_id = UnicodeAttribute(hash_key=True)
    quizzes = UnicodeAttribute(null=False)

    def save(self, *_):
        
        super(Quizzes, self).save()

    def __iter__(self):

        for name, attribute in self._get_attributes().items():
            yield name, attribute.serialize(getattr(self, name))
