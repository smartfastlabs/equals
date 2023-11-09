from ..base import Base


class LessThanOrEqual(Base):
    _description = "less than or equal to {}"

    def _check(self, value):
        return value <= self.value
