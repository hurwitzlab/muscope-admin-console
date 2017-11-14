from flask_admin.contrib.sqla import ModelView


class MuScopeModelView(ModelView):
    column_display_pk = True
    form_excluded_columns = []
