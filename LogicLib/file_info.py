from .field_collection import FieldCollection

class FileInfo:
    def __init__(self, meta_file_path):
        self.header_fields_desc = FieldCollection()
        self.content_fields_desc = FieldCollection()
        self.footer_fields_desc = FieldCollection()
        self.load_meta_info(meta_file_path)

    def load_meta_info(self, meta_file_path):
        with open(meta_file_path, 'r') as meta_file:
            lines = meta_file.readlines()

        current_collection = None
        for line in lines:
            line = line.strip()
            if line == "HeaderFieldsDesc":
                current_collection = self.header_fields_desc
            elif line == "ContentFieldsDesc":
                current_collection = self.content_fields_desc
            elif line == "FooterFieldsDesc":
                current_collection = self.footer_fields_desc
            elif line:
                info = line.split(',')
                name = info[0]
                position = tuple(map(int, info[1].split('-')))
                data_type = info[2]
                extra_info = info[3]
                editable = info[4] == "editable"
                current_collection.add_field(name, position, data_type, extra_info, editable)
