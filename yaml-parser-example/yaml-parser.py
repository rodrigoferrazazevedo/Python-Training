import yaml

def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result


if __name__ == "__main__":
    filepath = "test.yaml"
    data = yaml_loader(filepath)
    print(data)

    items = data.get('items')
    for item_name, item_value in items.items():
        print(item_name, item_value)

    data2 = find('name', data)
    print(list(data2))

 
    filepath2 = "test2.yaml"
    data2 = {
        "items": {
            "sword": 100,
            "axe": 80,
            "boots": 40
        }
    }
    yaml_dump(filepath2, data2)