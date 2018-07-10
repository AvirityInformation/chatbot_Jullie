import logging
import os
from apiai import ApiAI
import json
from common.constant.intent_type import Intent
from common.word_format.word_formatter import WordFormatter

_request_apiai_err_msg = '''
This typically means that you failed to send proper request to api.ai. To solve this, check client_access_token and session_id
'''

def request_to_apiai(df):
    try:
        message = WordFormatter.Df2Str(df)
        client_access_token = os.environ.get('client_access_token', None)
        session_id = os.environ.get('session_id', None)
        ai = ApiAI(client_access_token)
        request = ai.text_request()
        request.session_id = session_id
        request.query = message
        response = json.loads(request.getresponse().read().decode('utf-8'))

        if response is not None:
            if 'action' in response['result'].keys():
                candidate = response['result']['action']

                if Intent.has_value(candidate):
                    return Intent(candidate)

        if is_haha_intent(message):
            return Intent.HAHA

        return Intent.NORMAL
    except:
        logging.exception(_request_apiai_err_msg)
        return Intent.NORMAL


def is_haha_intent(message):
    return True if message in {'haha.', 'hahaha.', 'lol.'} else False
