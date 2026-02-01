from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('subjects/', include('subjects.urls')),
    path('attendance/', include('attendance.urls')),
    path('marks/', include('marks.urls')),
]
