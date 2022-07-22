from rest_framework import permissions


class IsBlogAdmin(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    # message = "You don't have access to view this page"

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
                (request.user.is_blogger and request.user.is_staff) or (
                request.user.is_superuser and request.user.is_staff)))


class IsBCSAdmin(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    # message = "You don't have access to view this page"

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
                (request.user.is_bcs_head and request.user.is_staff) or (
                request.user.is_superuser and request.user.is_staff)))


class IsPCSAdmin(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    # message = "You don't have access to view this page"

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
                (request.user.is_pcs_head and request.user.is_staff) or (
                request.user.is_superuser and request.user.is_staff)))


class IsMainAdmin(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    # message = "You don't have access to view this page"

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
            (request.user.is_superuser and request.user.is_staff)))


class IsTeamAdmin(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    # message = "You don't have access to view this page"

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and
            request.user.is_bcs and
            request.user.business_user.privilege != 'general_staff')
