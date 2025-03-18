from rest_framework import routers
from tech.views import ProjectViewSet, ProjectListViewRaw, ProjectViewSetCursor

router = routers.DefaultRouter()

router.register("v1/projects", ProjectViewSet, "projects")
router.register("v1/projects-raw", ProjectListViewRaw, "projects-raw")
router.register("v1/projects-cursor", ProjectViewSetCursor, "projects-cursor")


urlpatterns = router.urls