from json import dumps

ResponseType = dict[str, any]

def response(status, message) -> ResponseType:

    return {
        'status': status,
        'body': dumps({
            'message': message
        })
    }

def error_response(status, error_message) -> ResponseType:

    return {
        'status': status,
        'body': dumps({
            'error_message': error_message
        })
    }