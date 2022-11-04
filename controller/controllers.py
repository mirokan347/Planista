from abc import ABC, abstractmethod
from view.views import View

class Controller(ABC):
    @abstractmethod
    def bind(self: View):
        raise NotImplementedError