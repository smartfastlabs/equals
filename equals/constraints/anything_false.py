from .base import Base


class AnythingFalse(Base):
    _description = 'that is false'

    def _check(self, value):
        return not bool(value)
