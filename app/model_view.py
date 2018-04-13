from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm

from app import models


class MuScopeModelView(ModelView):
    form_base_class = SecureForm
    column_display_pk = True
    form_excluded_columns = []


class SampleView(MuScopeModelView):
    column_searchable_list = ['sample_name', ]
    column_filters = ['sample_id', ]

    form_ajax_refs = {
        'sample_attr_list': {
            'fields': (models.Sample_attr.value, )
        },
        'sample_file_list': {
            'fields': (models.Sample_file.file_, )
        }
    }


class SampleFileView(MuScopeModelView):
    column_searchable_list = ['file_', 'sample.sample_name', ]
    column_filters = ['sample_file_id', 'file_', 'sample.sample_name', 'sample_file_type.type_']
