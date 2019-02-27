from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic


class View1(PermissionRequiredMixin, generic.TemplateView):
    template_name = 'view1.html'
    permission_required = 'custompermissions.can_view_view1'


class View2(PermissionRequiredMixin, generic.TemplateView):
    template_name = 'view2.html'
    permission_required = 'custompermissions.can_view_view2'
