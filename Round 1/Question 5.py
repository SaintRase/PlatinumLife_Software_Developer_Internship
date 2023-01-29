from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_params(request):
    """
    """

    content = {
        'name': 'John', 
        'surname': 'Doe'
    }
    return Response(content, status=status.HTTP_200_OK)
