import pickle
import base64


def dumps(data):
    data_bytes = pickle.dumps(data)
    data_base = base64.b64encode(data_bytes)
    data_str = data_base.decode()
    return data_str


def loads(str):
    data_bytes = str.encode()
    data_base = base64.b64decode(data_bytes)
    data = pickle.loads(data_base)
    return data
