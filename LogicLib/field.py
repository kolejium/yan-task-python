from .field_info import FieldInfo

class Field:
    def __init__(self, field_info : dict[int, object], value=None):
        self.field_info = field_info
        self.value = value