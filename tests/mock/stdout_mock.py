
class StdoutMock():
    def __init__(self, *args, **kwargs):
        self.content = ''

    def write(self, content):
        self.content += content

    def read(self):
        return self.content

    def __str__(self):
        return self.read()
