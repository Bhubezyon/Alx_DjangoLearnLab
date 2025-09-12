from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
	# Add your URL patterns here, e.g. path('some-url/', some_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)