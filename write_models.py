from imicrobe_model import write_models


class FlaskModelWriter(write_models.ModelWriter):
    def __init__(self, db_uri):
        super().__init__(self, db_uri)

    def get_model_parent_class_name(self):
        return 'db.Model'

    def import_model_base(self):
        return """\
import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql

from app import db


"""

    def write_additional_methods(self, table, table_code):
        # write a json() method
        table_code.write("    def json(self):\n        return {\n")
        for column in table.columns:
            if column.primary_key:
                # do not include primary key in JSON
                pass
            else:
                table_code.write(
                    "            '{}': self.{},\n".format(
                        column.name, self.translate_column_name_to_py(column.name)))
        table_code.write("        }")
        table_code.write("\n\n")

        # write __repr__() if we know which fields to display
        table_name_to_representative_py_attr = {
            'app_data_type': ('name', ),
            'app_tag': ('value', ),
            'assembly': ('assembly_name', ),
            'centrifuge': ('name', ),
            'combined_assembly': ('assembly_name', ),
            'domain': ('domain_name', ),
            'investigator': ('investigator_first_name', 'investigator_last_name'),
            'ontology': ('label', ),
            'project': ('project_name', ),
            'project_group': ('group_name', ),
            'protocol': ('protocol_name', ),
            'sample': ('sample_name', ),
            'sample_attr': ('sample_attr_type', 'attr_value', ),
            'sample_attr_type': ('type_', ),
            'sample_file': ('file', ),
            'sample_file_type': ('type_', )
        }

        if table.name in table_name_to_representative_py_attr:
            table_code.write(
                "    def __repr__(self):\n"
                "        return " + ' + ":" + '.join([
                    "str(self.{})".format(a)
                    for a
                    in table_name_to_representative_py_attr[table.name]]))
            table_code.write('\n\n')


def main():
    FlaskModelWriter(db_uri=os.environ.get('MUSCOPE_DB_URI')).write_models('app/models.py')


if __name__ == '__main__':
    main()
