from rest_framework.throttling import UserRateThrottle

class DiceRollThrottle(UserRateThrottle):
    scope = 'dice_roll'