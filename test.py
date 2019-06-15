# coding=utf8

import sys
import time


class TestA():
    def __init__(self):
        self.a = 5

    def just_do_it(self, x, y):
        print x / y


class TestB():
    def __int__(self):
        self.a = None

    def process(self):
        self.a.just_do_it(1, 0)


def main():
    a = TestA()
    b = TestB()
    b.a = a
    b.process()


class Trace

class FrameParse(object):
    def __init__(self, traceback_obj):
        self.frames = []
        self.obj = traceback_obj

    def _has_next(self, current):
        self.frames.append(current.tb_frame)
        if current.tb_next:
            self._has_next(current.tb_next)

    def parse(self):
        """
'f_builtins', 'f_code', 'f_exc_traceback', 'f_exc_type', 'f_exc_value', 'f_globals', 'f_lasti', 'f_lineno', 'f_locals', 'f_restricted', 'f_trace'
        """
        self._has_next(self.obj)

        for f in self.frames:
            print f.f_code.co_filename, f.f_code.co_name, '()', f.f_lineno, ',', f.f_locals
        return self


if __name__ == "__main__":
    try:
        main()
    except Exception as e:

        exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        print exc_type
        print exc_value
        FrameParse(exc_traceback_obj).parse()



