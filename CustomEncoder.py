import datetime
import json
from uuid import UUID


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        if hasattr(obj, '__call__'):
            pass
        return json.JSONEncoder.default(self, obj)
