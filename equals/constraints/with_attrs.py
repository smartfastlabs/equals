from .base import Base


class WithAttrs(Base):
    _description = 'with attrs: {}'

    def _check(self, value):
        for k in self.args:
            if not hasattr(value, k):
                return False

        for k, v in self.kwargs.items():
            if not hasattr(value, k):
                return False
            if getattr(value, k) != v:
                return False

        return True
