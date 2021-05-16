from rest_framework import permissions


class IsLeadUploaderOrSafeMethods(permissions.BasePermission):
    """
    Object-level permission to allow an authenticated user to upload a lead on the app.
    """

    def has_object_permission(self, request, view, obj):
        person = request.user.person
        if (
            request.method == 'POST' or
            request.method in permissions.SAFE_METHODS or
            person == obj.lead.uploader
        ):
            return True
        return False


class IsLeadUploader(permissions.BasePermission):
    """
    Object-level permission to allow lead uploader of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return request.person == obj.lead.uploader
