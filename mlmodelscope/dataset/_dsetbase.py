import abc
from abc import ABC


class DataSet(ABC):
    """ An abstract base class for dataset classes. """
    __name__ = None

    @property
    @abc.abstractmethod
    def foo(self):
        pass

    @classmethod
    def bar():
        pass

    @staticmethod
    def foobar():
        pass
