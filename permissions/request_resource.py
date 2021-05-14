from rest_framework import permissions


class IsRequestUploaderOrSafeMethods(permissions.BasePermission):
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
    def has_object_permission(self, request, view, obj):
        return request.person == obj.request.uploader
