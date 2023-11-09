from ..base import Base


class LessThan(Base):
    _description = "less than {}"

    def _check(self, value):
        return value < self.value
