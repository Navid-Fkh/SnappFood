from rest_framework import status
from rest_framework.response import Response
from django.db import connection


# Create your views here.

def create_tables(request):
    with connection.cursor() as cursor:
        try:
            query = ""
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as ex:
            error = str(ex)
    return Response(error, status=status.HTTP_200_OK)