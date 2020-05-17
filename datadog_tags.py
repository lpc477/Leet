"""
We have a stream of tags (e.g. 'host:c', 'role:db,region:us') that we receive from our
customers and we want to build a page to summarize the tags they send.
Write a function that takes this list of tags as input returns a data structure that contains
the count of each tag.
String[] stream = {
    "host:a,role:web,availability-zone:us-east-1a",
    "host:b,role:web,availability-zone:us-east-1b",
    "host:a,role:web,availability-zone:us-east-1a",
    "host:c,role:db,db_role:master,availability-zone:us-east-1e",
    "host:d,role:db,db_role:replica,availability-zone:us-east-1a",
    "host:e,role:intake,availability-zone:us-east-1a",
    "host:e,role:intake,availability-zone:us-east-1a",
    "host:f,role:kafka,availability-zone:us-east-1a"
}
// Example output
{
    'availability-zone:us-east-1a': 6,
    'db_role:master': 1,
    'availability-zone:us-east-1b': 1,
    'host:d': 1,
    'role:db': 2,
    'host:b': 1,
    'host:c': 1,
    'host:a': 2,
    'role:web': 3,
    'host:f': 1,
    'role:kafka': 1,
    'host:e': 2,
    'availability-zone:us-east-1e': 1,
    'db_role:replica': 1,
    'role:intake': 2
}"""


def dog_tags(stream):
    result = {}
    for line in stream:
        tags = line.split(",")
        for tag in tags:
            if tag in list(result.keys()):
                value = result[tag] + 1
                result[tag] = value
            else:
                result[tag] = 1
    return result


def main():
    stream = [
        "host:a,role:web,availability-zone:us-east-1a",
        "host:b,role:web,availability-zone:us-east-1b",
        "host:a,role:web,availability-zone:us-east-1a",
        "host:c,role:db,db_role:master,availability-zone:us-east-1e",
        "host:d,role:db,db_role:replica,availability-zone:us-east-1a",
        "host:e,role:intake,availability-zone:us-east-1a",
        "host:e,role:intake,availability-zone:us-east-1a",
        "host:f,role:kafka,availability-zone:us-east-1a"
    ]
    result = dog_tags(stream)
    print(result)


if __name__ == '__main__':
    main()
