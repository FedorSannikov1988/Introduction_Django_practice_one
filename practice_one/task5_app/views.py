import random
import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def heads_or_tails(request):
    coin: list = ["heads", "tails"]
    resalt: str = random.choice(coin)
    logger.info(f'heads_or_tails page accessed, get message: {resalt}')
    return HttpResponse(resalt)


def playing_dice(request):
    start: int = 1
    stop: int = 6
    resalt: int = get_random_number(start=start, stop=stop)
    logger.info(f'playing_dice page accessed, get message: {resalt}')
    return HttpResponse(resalt)


def random_number(request):
    start: int = 0
    stop: int = 100
    resalt: int = get_random_number(start=start, stop=stop)
    logger.info(f'playing_dice page accessed, get message: {resalt}')
    return HttpResponse(resalt)


def get_random_number(start: int, stop: int) -> int:
    return random.randint(start, stop)
