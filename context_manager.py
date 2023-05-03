
#  Context manager

class Manager:

    def __init__(self):
        print('initialized')

    def __enter__(self):
        print('entered')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exited')


with Manager() as m:
    print('here')


#  --------------------------


class FileManager:

    def __init__(self, filename, mode='r'):
        self.filename = filename
        if mode == 'w':
            raise Exception('Truncating file on open is not allowed')
        self.mode = mode
        self.file = None
        print('initialized')

    def __enter__(self):
        print('entered')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print('exited')


with FileManager('sandbox.py', 'r') as fm:
    print('here')
    print(fm.readline(100), 'inside context manager call')

