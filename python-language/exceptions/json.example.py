import json
json_data = '}}'

try:
    data = json.loads(json_data)
except (ValueError, TypeError) as e:
    print(type(e), e)