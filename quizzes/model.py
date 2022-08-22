from datetime import datetime
from os import environ as env

from pynamodb.attributes import (ListAttribute, MapAttribute, NumberAttribute,
                                 UnicodeAttribute, UTCDateTimeAttribtute)
from pynamodb.models import Model


class Quiz(MapAttribute):

    question_list = ListAttribute(null=False)
    correct_answer = NumberAttribute(null=False)

class Quizzes(Model):

    class Meta:

        table_name = env['QUIZZES_TABLE']
        region = env['AWS_REGION']
        host = f'https://dynamodb.{region}.amazonaws.com'

    id = UnicodeAttribute(hash_key=True, null=False)
    quiz_name = UnicodeAttribute(null=False)
    quiz = Quiz(null=False)
    modified_time =UTCDateTimeAttribtute(null=False)

    def save(self, *_):
        
        self.modified_time = datetime.now()
        super(Quizzes, self).save()
