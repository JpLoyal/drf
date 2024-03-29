from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionsMixin():
    permission_classes = [permissions.IsAdminUser,
                          IsStaffEditorPermission]