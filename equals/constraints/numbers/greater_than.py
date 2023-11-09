from ..base import Base


class GreaterThan(Base):
    _description = "greater than {}"

    def _check(self, value):
        return value > self.value
