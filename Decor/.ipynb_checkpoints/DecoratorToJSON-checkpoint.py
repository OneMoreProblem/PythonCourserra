import functools
import json


def to_json(func):
    @functools.wraps(func)
    def translator(*args,**kwargs):
        return json.dumps(func(*args,**kwargs))
    return translator

# @to_json
# def get_data():
#     return {
#         'data': 42
#     }
  
# get_data()  # вернёт '{"data": 42}'