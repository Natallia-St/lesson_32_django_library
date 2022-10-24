from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('books.urls')),
    # path('projects/', include('project.urls')),
    # path('blog/', include('blog.urls')),

    ]
