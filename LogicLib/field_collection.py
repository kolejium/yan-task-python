from field_info import FieldInfo
from field import Field

class FieldCollection:
    def __init__(self):
        self.fields = []

    def add_field(self, name, position, data_type, extra_info, editable):
        field_info = FieldInfo(name, position, data_type, extra_info, editable)
        self.fields.append(Field(field_info))