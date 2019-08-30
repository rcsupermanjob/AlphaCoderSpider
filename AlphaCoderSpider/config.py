port = 55555
cache = list()
cache_ = list()


def delete_create():
    global cache, cache_
    del cache, cache_
    cache = list()
    cache_ = list()


def store(data):
    global cache, cache_
    print(data)
    cache = data
    cache_ = cache
    print(cache_)


def get_content():
    global cache_
    print('get content ' + str(len(cache_)))
    return cache_
