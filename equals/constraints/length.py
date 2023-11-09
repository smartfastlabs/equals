from .base import Base


class Length(Base):
    _description = "length: {}"

    def _check(self, value):
        return len(value) == self.value
