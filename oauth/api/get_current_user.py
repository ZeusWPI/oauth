from rest_framework.response import Response
from rest_framework.decorators import api_view

from serializers import UserSerializer


@api_view(['GET'])
def current_user(request):
    serialized = UserSerializer(request.user)

    return Response(serialized.data)
