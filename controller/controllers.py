from abc import ABC, abstractmethod
from view.views import View

class Controller(ABC):
    @abstractmethod
    def bind(view: View):
        raise NotImplementedError