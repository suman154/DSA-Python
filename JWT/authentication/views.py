from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.

class WelcomeView(APIView):
    # Restrict access to authenticated users only
    permission_classes = (IsAuthenticated,) #AllowAny

    def get(self, request):
        # Response content
        content = {'message': 'Welcome to the Platform'}
        # Return the content as a JSON response
        return Response(content)