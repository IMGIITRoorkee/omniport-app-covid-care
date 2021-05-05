from rest_framework import permissions


class IsUploaderOrSafeMethods(permissions.BasePermission):
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
    def has_object_permission(self, request, view, obj):
        return request.person == obj.uploader
