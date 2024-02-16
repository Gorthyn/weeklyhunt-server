"""
URL configuration for weeklyhunt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from weeklyhuntapi.views import login_user, register_user, BasicMoveView, dice_roller, AdvancedImprovementsView, AgencyGoalsView, AgencyView, BackgroundView, ChosenBusinessEndView, ChosenFormView, ChosenMaterialView, ChosenWeaponView, CombatEffectView, CombatMagicBaseView, CurseView, DarkSideView, DoomView, FateView, GearView, HavenView, HeatView, HeroicView, HistoryView, ImprovementView, LookView, MissionView, MonsterBreedsView, MoveView, NaturalAttacksView, PlaybookView, RatingView, ReasonView, RedTapeView, ResourcesView, SectView, UnderworldView, WhoYouLostView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'basicmoves', BasicMoveView, 'basicmove')
router.register(r'advancedimprovements', AdvancedImprovementsView, 'advancedimprovement')
router.register(r'agencygoals', AgencyGoalsView, 'agencygoal')
router.register(r'agencies', AgencyView, 'agency')
router.register(r'backgrounds', BackgroundView, 'background')
router.register(r'chosenbusinessends', ChosenBusinessEndView, 'chosenbusinessend')
router.register(r'chosenforms', ChosenFormView, 'chosenform')
router.register(r'chosenmaterials', ChosenMaterialView, 'chosenmaterial')
router.register(r'chosenweapons', ChosenWeaponView, 'chosenweapon')
router.register(r'combateffects', CombatEffectView, 'combateffect')
router.register(r'combatmagicbases', CombatMagicBaseView, 'combatmagicbase')
router.register(r'curses', CurseView, 'curse')
router.register(r'darksides', DarkSideView, 'darkside')
router.register(r'dooms', DoomView, 'doom')
router.register(r'fates', FateView, 'fate')
router.register(r'gears', GearView, 'gear')
router.register(r'havens', HavenView, 'haven')
router.register(r'heats', HeatView, 'heat')
router.register(r'heroics', HeroicView, 'heroic')
router.register(r'histories', HistoryView, 'history')
router.register(r'improvements', ImprovementView, 'improvement')
router.register(r'looks', LookView, 'look')
router.register(r'missions', MissionView, 'mission')
router.register(r'monsterbreeds', MonsterBreedsView, 'monsterbreed')
router.register(r'moves', MoveView, 'move')
router.register(r'naturalattacks', NaturalAttacksView, 'naturalattack')
router.register(r'playbooks', PlaybookView, 'playbook')
router.register(r'ratings', RatingView, 'rating')
router.register(r'reasons', ReasonView, 'reason')
router.register(r'redtapes', RedTapeView, 'redtape')
router.register(r'resources', ResourcesView, 'resource')
router.register(r'sects', SectView, 'sect')
router.register(r'underworlds', UnderworldView, 'underworld')
router.register(r'whoyoulosts', WhoYouLostView, 'whoyoulost')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('roll/', dice_roller, name='roll_2d6'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
]
