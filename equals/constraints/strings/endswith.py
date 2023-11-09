from ..base import Base


class EndsWith(Base):
    _description = "ending with {}"

    def _check(self, value):
        return value.endswith(self.value)
