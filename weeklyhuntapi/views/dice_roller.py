import random, logging
from django.http import JsonResponse
from django.core.cache import cache
from weeklyhuntapi.models import DiceRoll
from django.contrib.auth.decorators import login_required
from django.db import transaction

logger = logging.getLogger(__name__)

@login_required
def roll_2d6(request):
    cache_key = 'recent_2d6_rolls'
    recent_rolls = cache.get(cache_key)

    if recent_rolls:
        return JsonResponse(recent_rolls)

    try:
        modifier = int(request.GET.get('modifier', 0))
        result_1 = random.randint(1, 6)
        result_2 = random.randint(1, 6)
        total = result_1 + result_2 + modifier
        
        with transaction.atomic():
            DiceRoll.objects.create(result_1=result_1, result_2=result_2, modifier=modifier, total=total, roll_type='2d6')
        
        response_data = {
            'result_1': result_1,
            'result_2': result_2,
            'modifier': modifier,
            'total': total
        }
        
        # Cache the response for 1 hour
        cache.set(cache_key, response_data, timeout=3600)

        return JsonResponse(response_data)
    except Exception as e:
        logger.error(f"Failed to roll 2d6: {str(e)}")
        return JsonResponse({"error": "Error processing your dice roll"}, status=500)

@login_required
def roll_1d20(request):
    try:
        modifier = int(request.GET.get('modifier', 0))
        result = random.randint(1, 20)
        total = result + modifier
        
        with transaction.atomic():
            DiceRoll.objects.create(result_1=result, result_2=None, modifier=modifier, total=total, roll_type='1d20')
        
        return JsonResponse({
            'result': result,
            'modifier': modifier,
            'total': total
        })
    except Exception as e:
        logger.error(f"Failed to roll 1d20: {str(e)}")
        return JsonResponse({"error": "Error processing your dice roll"}, status=500)

@login_required
def flip_2sidedcoin(request):
    try:
        result = random.choice(['Heads', 'Tails'])
        
        with transaction.atomic():
            DiceRoll.objects.create(result_1=1 if result == 'Heads' else 0, result_2=None, modifier=0, total=1 if result == 'Heads' else 0, roll_type='coin')
        
        return JsonResponse({'result': result})
    except Exception as e:
        logger.error(f"Failed to flip a 2-sided coin: {str(e)}")
        return JsonResponse({"error": "Error processing your coin flip"}, status=500)
    