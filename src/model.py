from os import environ as env

from pynamodb.attributes import (ListAttribute, MapAttribute, NumberAttribute,
                                 UnicodeAttribute)
from pynamodb.models import Model


class Question(MapAttribute):

    question = UnicodeAttribute()
    answer_index = NumberAttribute()
    options = ListAttribute(of=UnicodeAttribute)

class Quiz(MapAttribute):

    quiz_name = UnicodeAttribute(hash_key=True, null=False)
    questions = ListAttribute(of=Question)
class Quizzes(Model):

    class Meta:

        table_name: str = env['DYNAMODB_TABLE']
        region = 'ap-southeast-1'
        host = f'https://dynamodb.{region}.amazonaws.com'

    device_id = UnicodeAttribute(hash_key=True)
    quizzes = ListAttribute(of=Quiz)
    modified_time =UnicodeAttribute(null=False)

    def save(self, *_):
        
        super(Quizzes, self).save()
