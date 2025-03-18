from rest_framework import routers
from tech.views import ProjectViewSet

router = routers.DefaultRouter()

router.register("v1/projects", ProjectViewSet, "projects")


urlpatterns = router.urls