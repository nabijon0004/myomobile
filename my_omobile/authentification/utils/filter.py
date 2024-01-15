from rest_framework.response import Response
from rest_framework import status
from django.db import connections

def filtering(res):
    closeAllConnections()
    if (
        res != None
        and
        'un_authorized' in res.keys()):
        return Response({"message":"Not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    elif (
        'status' in res.keys()
        and
        res['status'] == 'error'
        ):
        print("[ERROR]", res["message"])
        return Response({"message":"Server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(res, status=status.HTTP_200_OK)

def closeAllConnections():
    for connection_name in connections.databases:
        connections[connection_name].close()
