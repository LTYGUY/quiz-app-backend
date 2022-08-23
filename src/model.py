from os import environ as env

from pynamodb.attributes import (ListAttribute, MapAttribute, NumberAttribute,
                                 UnicodeAttribute)
from pynamodb.models import Model


class Question(MapAttribute):

    question = UnicodeAttribute()
    answers = ListAttribute(of=UnicodeAttribute)
    answer_index = NumberAttribute()

class Quiz(Model):

    class Meta:

        table_name = env['DYNAMODB_TABLE']
        region = 'ap-southeast-1'
        host = f'https://dynamodb.{region}.amazonaws.com'

    quiz_name = UnicodeAttribute(hash_key=True, null=False)
    modified_time =UnicodeAttribute(null=False)
    questions = ListAttribute(of=Question)

    def save(self, *_):
        
        super(Quiz, self).save()
