from ..base import Base


class GreaterThanOrEqual(Base):
    _description = "greater than or equal to {}"

    def _check(self, value):
        return value >= self.value
