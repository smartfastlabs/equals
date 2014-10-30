from .base import Base


class Containing(Base):
    _description = 'containing: {}'

    def _check(self, value):
        # This will check list like objects
        for v in self.args:
            if v not in value:
                return False

        # This will check dictionary like objects
        for k, v in self.kwargs.items():
            if k not in value or not value[k] == v:
                return False
        return True
