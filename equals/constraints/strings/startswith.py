from ..base import Base


class StartsWith(Base):
    _description = "starting with {}"

    def _check(self, value):
        return value.startswith(self.value)
