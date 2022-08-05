from django.urls import path
from rest_framework import routers

from .views import InnerRecommendationAPI, RecommendationViewSet
from .views import LikesViewSet, StrengthViewSet, WeaknessViewSet, ValueViewSet
from .views import SolveViewSet, CareerViewSet, LiteracyViewSet, LanguageViewSet, MBTIViewSet

router = routers.SimpleRouter()
## 내부 inner/
router.register('likes', LikesViewSet)
router.register('strength', StrengthViewSet)
router.register('weakness', WeaknessViewSet)
router.register('value', ValueViewSet)
## 외부, outer/
router.register('solve', SolveViewSet)
router.register('career', CareerViewSet)
router.register('literacy', LiteracyViewSet)
router.register('language', LanguageViewSet)
router.register('mbti', MBTIViewSet)
## recommendation/
router.register('crud', RecommendationViewSet)

## 프리즘, prism/
urlpatterns = router.urls + [
    path('inner/', InnerRecommendationAPI.as_view(), name='inner_recommendatioin_api')
]