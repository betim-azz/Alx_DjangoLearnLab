from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    # Get all notifications for the current user, newest first
    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by('-timestamp')

    data = [
        {
            "id": n.id,
            "actor": n.actor.username,
            "verb": n.verb,
            "timestamp": n.timestamp,
            "is_read": n.is_read,
        }
        for n in notifications
    ]

    return Response(data)