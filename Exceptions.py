class PathNotFind(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class FileNotFind(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
# hyeongchang : commit_2
