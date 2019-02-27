from django.db import models


class ViewPermissions(models.Model):
    class Meta:
        permissions = (
            ('can_view_view1', 'Can view View 1'),
            ('can_view_view2', 'Can view View 2'),
        )
