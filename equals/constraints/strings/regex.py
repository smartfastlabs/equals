import re

from ..base import Base


class Regex(Base):
    _description = "matching {}"

    def _check(self, value):
        return bool(re.search(self.value, value))
