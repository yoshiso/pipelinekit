__author__ = 'Sho Yoshida'
__version__ = '0.0.1'
__license__ = 'MIT'

from collections import OrderedDict


class Pipeline(object):
    """
        Experiment pipeline to preprocess datasets.
    """

    def __init__(self):
        self.pipes = OrderedDict()

    def pipe(self, func, pipe_name=None, use_pipe=True, **kwargs):
        if pipe_name is None:
            pipe_name = len(self.pipes)

        if not use_pipe:
            return self

        if isinstance(func, Pipe):
            self.pipes[pipe_name] = func.assign(**kwargs)
        else:
            self.pipes[pipe_name] = Pipe(func).assign(**kwargs)
        return self

    def execute(self, data):
        for pipe in self.pipes.values():
            data = pipe(data)
        return data

    def __call__(self, data, **kwargs):
        """Short cut for pipeline connection
        """
        return self.execute(data)

    def __str__(self):
        names = ['    ' + str(pipe) for pipe in self.pipes.values()]
        return 'Pipeline<[\n' + \
               '\n'.join(names) + \
               '\n]>'


class Pipe(object):

    def __init__(self, func, pipe_type='stateless'):
        self.func = func
        self.pipe_type = pipe_type
        self.kwargs = {}
        self.context = {}

    def assign(self, **kwargs):
        self.kwargs = kwargs
        return self

    def clear(self):
        self.context = {}

    def __call__(self, data):
        if self.pipe_type == 'statefull':
            return self.func(self, data, **self.kwargs)
        elif self.pipe_type == 'stateless':
            return self.func(data, **self.kwargs)
        raise RuntimeError('Undefined pipe_type: {}'.format(self.pipe_type))

    def __str__(self):
        if hasattr(self.func, '__name__'):
            return 'Pipe<{}>'.format(self.func.__name__)
        return 'Pipe'


def make_pipe(func):
    """
        Simple make unsupported function to be compatible.
    """
    return Pipe(lambda x, **kwargs: func(x), pipe_type='stateless')


def make_statefull_pipe(func):
    return Pipe(func, pipe_type='statefull')


def make_pipeline():
    return Pipeline()
