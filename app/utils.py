import json
from io import BytesIO

from bson import json_util
from flask import send_file, render_template

from config import APP_NAME


def get_form_payload(form):
    """
    Return Dict of form.data where items have data
    :param form:
    :return:
    """
    try:
        form = form.data
    except Exception:
        mydict = {}
        return mydict  # Empty dict will behave normal
    return dict([(k, v) for k, v in form.items() if v != '' and k != 'csrf_token'])


def page_render(template, ctx={}):
    ctx['APP_NAME'] = APP_NAME
    return render_template(template, **ctx)


def parse_json(data):
    return json.loads(json_util.dumps(data))


def serialize_data(data, find_one=False):
    if find_one:
        data = dict(parse_json(data))
    elif not isinstance(data, list):
        data = list(parse_json(data))
    return data