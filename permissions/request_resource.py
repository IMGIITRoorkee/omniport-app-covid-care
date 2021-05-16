from rest_framework import permissions


class IsRequestUploaderOrSafeMethods(permissions.BasePermission):
    """
    Object-level permission to allow an authenticated user to upload a request on the app.
    """
    def has_object_permission(self, request, view, obj):
        person = request.user.person
        if (
            request.method == 'POST' or
            request.method in permissions.SAFE_METHODS or
            person == obj.request.uploader
        ):
            return True
        return False


class IsRequestUploader(permissions.BasePermission):
    """
    Object-level permission to allow request uploader of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return request.person == obj.request.uploader
