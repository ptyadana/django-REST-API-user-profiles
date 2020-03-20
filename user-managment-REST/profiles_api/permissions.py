from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        #check request method whether this is only to reterive or other
        #if for only reading (safe), then ok
        if request.method in permissions.SAFE_METHODS:
            return True

        #otherwise, check user is same as the person object that he is trying to update,etc
        return obj.id == request.user.id