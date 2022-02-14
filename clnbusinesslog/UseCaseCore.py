from abc import ABC, abstractmethod
from time import time


class UseCaseCore(ABC):
    """In UML, a complete task of a system that provides a measurable result of
    value for an actor 2. sequence of tasks that a system can perform,
    interacting with users of the system and providing a measurable result of
    value for the user [ISO/IEC 26513:2009 Systems and software
    engineering — Requirements for testers and reviewers of user documentation,
    3.43]3. description of the behavioral requirements of a system and its
    interaction with a user [ISO/IEC/IEEE 26515: 2011 Systems and software
    engineering: Developing user documentation in an agile environment, 4.15]

    Reference: https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:24765:ed-2:v1:en
    """
    def __init__(self, category=None):
        self._name = self.__class__.__name__.replace('UseCase', '')
        if category: assert isinstance(category, str)
        self._category = category

    @property
    def name(self): return self._name

    @property
    def category(self): return self._category

    @abstractmethod
    def __implementation__(self, *args, **kwargs): pass

    def __run__(self, *args, **kwargs):
        start = time()
        res = self.__implementation__(*args, **kwargs)
        ends = time()
        delay = ends - start
        print(f"Use case {self._name} executed in {delay:.10f} secs")
        return res

    use = __run__
    __call__ = __run__
