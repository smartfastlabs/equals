from .base import Base


class AnythingTrue(Base):
    _description = 'that is true'

    def _check(self, value):
        return bool(value)
