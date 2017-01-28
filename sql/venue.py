from .mariadb import *

def fetch(params=None, page=None):
    connection = connect()
    query = '''select v.id, d.type, d.parser from venue v
               join datasource d on d.id=v.datasource_id
    ''';
    try:
        with connection.cursor() as cursor:
            cursor.execute(query);
            # params array to filter results
            # fetch by id, name, whatever
            # key is column, value is value
            results = cursor.fetchall();
            venues = []
            for result in results:
                venue = dict()
                venue['id'] = result[0]
                venue['type'] = result[1]
                venue['parser'] = result[2]
                venues.append(venue)

    finally:
        connection.close()

    return venues;

def fetchall(page):
    return fetch(None, page)

def fetchbyid(id):
    # if id is null or not int, return error
    params = {'id': id}
    return fetch(params)

def fetchbyname(name):
    params = {'name': name}
    return fetch(params)

