import random
from django.http import JsonResponse
from weeklyhuntapi.models import DiceRoll

def roll_2d6(request):
    modifier = int(request.GET.get('modifier', 0))  # Optional modifier
    result_1 = random.randint(1, 6)
    result_2 = random.randint(1, 6)
    total = result_1 + result_2 + modifier
    
    # Save the result to the database
    DiceRoll.objects.create(result_1=result_1, result_2=result_2, modifier=modifier, total=total, roll_type='2d6')
    
    return JsonResponse({
        'result_1': result_1,
        'result_2': result_2,
        'modifier': modifier,
        'total': total
    })

def roll_1d20(request):
    modifier = int(request.GET.get('modifier', 0))  # Optional modifier
    result = random.randint(1, 20)
    total = result + modifier
    
    # Save the result to the database
    DiceRoll.objects.create(result_1=result, result_2=None, modifier=modifier, total=total, roll_type='1d20')
    
    return JsonResponse({
        'result': result,
        'modifier': modifier,
        'total': total
    })
