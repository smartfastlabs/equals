from equals.constraints.base import Base as _Base


class Base(_Base):
    def _handle_args(self, value):
        self.value = value
