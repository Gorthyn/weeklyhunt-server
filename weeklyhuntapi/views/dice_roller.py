import random, logging
from django.http import JsonResponse
from weeklyhuntapi.models import DiceRoll

logger = logging.getLogger(__name__)

def roll_2d6(request):
    try:
        modifier = int(request.GET.get('modifier', 0))
        result_1 = random.randint(1, 6)
        result_2 = random.randint(1, 6)
        total = result_1 + result_2 + modifier
        
        DiceRoll.objects.create(result_1=result_1, result_2=result_2, modifier=modifier, total=total, roll_type='2d6')
        
        return JsonResponse({
            'result_1': result_1,
            'result_2': result_2,
            'modifier': modifier,
            'total': total
        })
    except Exception as e:
        logger.error(f"Failed to roll 2d6: {str(e)}")
        return JsonResponse({"error": "Error processing your dice roll"}, status=500)

def roll_1d20(request):
    try:
        modifier = int(request.GET.get('modifier', 0))
        result = random.randint(1, 20)
        total = result + modifier
        
        DiceRoll.objects.create(result_1=result, result_2=None, modifier=modifier, total=total, roll_type='1d20')
        
        return JsonResponse({
            'result': result,
            'modifier': modifier,
            'total': total
        })
    except Exception as e:
        logger.error(f"Failed to roll 1d20: {str(e)}")
        return JsonResponse({"error": "Error processing your dice roll"}, status=500)

def flip_2sidedcoin(request):
    try:
        result = random.choice(['Heads', 'Tails'])
        
        DiceRoll.objects.create(result_1=1 if result == 'Heads' else 0, result_2=None, modifier=0, total=1 if result == 'Heads' else 0, roll_type='coin')
        
        return JsonResponse({'result': result})
    except Exception as e:
        logger.error(f"Failed to flip a 2-sided coin: {str(e)}")
        return JsonResponse({"error": "Error processing your coin flip"}, status=500)
