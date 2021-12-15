from ward import fixture, test
from assertpy import assert_that

from src.horario import Horario
from datetime import time, date

@fixture
def good_horario():
    '''This Horario is correct'''
    day = date(2021, 12, 13)
    tabla = {
        'L': [(time(9, 0), 8)],
        'M': [(time(9, 0), 8)],
        'X': [(time(9, 0), 8)],
        'J': [(time(9, 0), 8)],
        'V': [(time(9, 0), 8)]
    }
    
    try:
        return Horario(day, tabla)
    except:
        return None

@fixture
def bad_horario():
    '''This Horario is not correct'''
    day = date(2021, 12, 14)
    tabla = {
        'L': [(time(9, 0), 25)],
        'M': [(time(9, 0), 8), (time(10, 0), 3)],
        'X': [(time(9, 0), 8)],
        'J': [(time(9, 0), 8)],
        'V': [(time(9, 0), 8)],
        'S': [(time(9, 0), 8)],
        'D': [(time(9, 0), 8)],
        'Not a valid key': [(time(9, 0), 8)]
    }

    try:
        return Horario(day, tabla)
    except:
        return None

@fixture
def empty():
    day = date(2021, 12, 13)
    return Horario(day)

@test('Horario is initialized')
def _(horario=good_horario()):
    '''Test if a correctly initialized Horario is a correct object'''
    assert_that(horario).is_not_none()
    assert_that(horario.fecha_inicio).is_not_none()
    assert_that(horario.dias).is_not_none()

@test('Validate Horario')
def _(horario=bad_horario()):
    '''Test if a badly initialized horario raises an Exception'''
    assert_that(horario).is_none()

@test('Count hours')
def _(horario=good_horario()):
    '''Test get_horas_trabajadas'''
    assert_that(Horario.get_horas_trabajadas(horario.dias)).is_equal_to(40)

@test('Add days')
def _(horario=empty()):
    '''Test adding a day to an horario'''
    days = { 'M': [(time(9), 8)] }
    horario.add_days(days)

    assert_that(len(horario.dias.keys())).is_equal_to(1)
    assert_that('M' in horario.dias).is_true()
    assert_that(horario.dias.values()).contains([(time(9), 8)])
