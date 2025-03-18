from django.db import connection
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tech.models import Project
from tech.serializers import ProjectSerializer

# orm django
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


# .raw
class ProjectListViewRaw(ViewSet):
    def list(self, request):

        # Ejecutar consulta SQL con .raw()
        project = Project.objects.raw("SELECT * FROM public.tech_project ORDER BY id ASC")

        # Convertir a lista para serializar correctamente
        projects_list = list(project)  # Agregamos esta línea
        
        # Serializar los datos
        serializer = ProjectSerializer(projects_list, many=True)  # Ahora serializa correctamente
        
        return Response(serializer.data)

# cursor
class ProjectViewSetCursor(ViewSet):
    def list(self, request):  # En ViewSet se usa list(), no get()
        query = "SELECT * FROM public.tech_project ORDER BY id ASC"
        
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]  # Obtener nombres de columnas
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]  # Convertir a diccionario
        
        return Response(results)  # Enviar JSON con los datos