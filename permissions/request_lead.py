from rest_framework import permissions


class IsUploaderOrSafeMethods(permissions.BasePermission):
    """
    Object-level permission to allow an authenticated user to upload an object on the app.
    """
    def has_object_permission(self, request, view, obj):
        person = request.user.person
        if (
            request.method == 'POST' or
            request.method in permissions.SAFE_METHODS
        ):
            return True
        else:
            print(request.method, person, obj.uploader)
            return person == obj.uploader


class IsUploader(permissions.BasePermission):
    """
    Object-level permission to allow uploader of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return request.person == obj.uploader
