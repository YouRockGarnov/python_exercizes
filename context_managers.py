from contextlib import contextmanager
import sys


@contextmanager
def supresser(*args):
    try:
        yield
    except Exception as ex:
        if type(ex) not in args:
            raise ex


@contextmanager
def retyper(type_from, type_to):
    try:
        yield
    except type_from as ex:
        args = ex.args
        traceback = ex.__traceback__

        result = type_to()
        result.args = args
        result.__traceback__ = traceback

        raise result


@contextmanager
def dumper(stream):
    try:
        yield
    except Exception as ex:
        stream.write(type(ex).__name__ + ': ')

        descr = str()
        for arg in ex.args:
            descr += arg + ', '
        descr = descr[:-2
                ]
        stream.write(descr)
        stream.write('\n')
        #stream.write(str(ex.__traceback__.tb_frame.f_trace))

        raise ex