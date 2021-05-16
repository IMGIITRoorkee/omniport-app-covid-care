from rest_framework import permissions


class IsPlasmaLeadUploaderOrSafeMethods(permissions.BasePermission):
    """
    Object-level permission to allow an authenticated user to upload a plasma - lead on the app.
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


class IsPlasmaLeadUploader(permissions.BasePermission):
    """
    Object-level permission to allow plasma lead uploader of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return request.person == obj.lead.uploader
