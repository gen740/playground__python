import toml

test = {"test": {"test": 3847.1234}}

with open("test.toml", 'w+') as f:
    toml.dump(test, f)
