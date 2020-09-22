from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="nlp_tasks_api",
        default_version='v1',
        description="None",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="costaguila@gmail.com"),
        license=openapi.License(name="closed source"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
