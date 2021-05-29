from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FirstModel


@permission_classes([AllowAny])
class FirstModelAPIView(APIView):
    def post(self, request):
        model = FirstModel()
        result = model.predict(request.data['payload'])
        return Response(result)
