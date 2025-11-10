from rest_framework.routers import DefaultRouter
from .views import DoctorView, PatientView, ResultView

router = DefaultRouter()
router.register(r'doctor',DoctorView)
router.register(r'patient',PatientView)
router.register(r'result',ResultView)

urlpatterns = router.urls
