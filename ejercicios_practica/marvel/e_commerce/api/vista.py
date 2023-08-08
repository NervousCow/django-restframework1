from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from django.http import HttpResponse

# NOTE: Ejemplo de hello world con método GET
@api_view(['GET'])
def hello_world(request):
    template = '<h1>Prueba copiado el ejemplo de clase</h1>' 
    return HttpResponse(template)

# NOTE: Ejemplo de hello world con método POST
@api_view(['GET', 'POST'])
@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def return_request_data(request):
    '''
    Esta función nos permite realizar una petición de tipo POST,
    Retorna el valor del parámetro "mi_parametro" enviada en la petición.
    '''
    template = f'<h1>{request.GET.get("mi_parametro")}</h1>'
    # Tambien podemos llamar al método dentro de request, haciendo:
    # request.POST.get('alguna_key')
    print(template)
    return HttpResponse(template)


@api_view(['GET'])
def ejemplo_get(request):
    data = {
        'mensaje': 'Ejemplo de un GET request.'
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def ejemplo_post(request):
    if request.method == 'POST':
        data = request.data
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def ejemplo_post_dos(request):
    if request.method == 'POST':
        data = request.data
        response_data = {
            'received_data': data,
            'message': 'Data received successfully.'
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)