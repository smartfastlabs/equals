from ..base import Base


class Between(Base):
    @property
    def description(self):
        return "between {min} and {max}".format(
            min=self.min_val,
            max=self.max_val,
        )

    def _handle_args(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def _check(self, value):
        return self.min_val < value < self.max_val
