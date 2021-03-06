from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MyModel


model = MyModel()


@permission_classes([AllowAny])
class MyModelAPIView(APIView):
    def post(self, request):
        result = model.predict(request.data['payload'])
        return Response(result)
