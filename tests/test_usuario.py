from ward import fixture, test
from assertpy import assert_that

from src.usuario import Usuario
from src.horario import Horario
from datetime import time, date

@fixture
def first():
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

def second():
    day = date(2021, 12, 27)
    tabla = {
        'L': [(time(9, 0), 8)],
        'M': [(time(9, 0), 8)],
        'X': [(time(9, 0), 8)],
        'J': [(time(9, 0), 8)],
        'V': [(time(9, 0), 8)],
    }
    
    try:
        return Horario(day, tabla)
    except Exception as e:
        print(e)
        return None

@fixture
def user():
    return Usuario('Edu', [first(), second()])

@test('User initialization')
def _(u=user()):
    '''Test if a correctly initialized User is a correct object'''
    assert_that(u).is_not_none()
    assert_that(u.name).is_not_none()
    assert_that(u.horarios).is_not_none()
    assert_that(len(u.horarios)).is_equal_to(2)

@test('Search and find horario')
def _(u=user, first=first(), second=second()):
    '''Test that searching for a monday on user's horarios'''
    # search for first and it has to be found 
    found = u.search_horario(date(2021,12,13))
    assert_that(found.fecha_inicio).is_equal_to(first.fecha_inicio)
    assert_that(found.dias).is_equal_to(first.dias)

    # search for second and it has to be found 
    found = u.search_horario(date(2021,12,27))
    assert_that(found.fecha_inicio).is_equal_to(second.fecha_inicio)
    assert_that(found.dias).is_equal_to(second.dias)

@test('Use last if not found')
def _(u=user(), first=first(), second=second()):
    '''Test that searching for a monday that is not on user's horarios a new
    horario with the given date is generated
    '''

    # must return an horario similar to first
    found = u.search_horario(date(2021,12,6))
    assert_that(found.dias).is_equal_to(first.dias)

    # must return an horario similar to first
    found = u.search_horario(date(2021,12,20))
    assert_that(found.dias).is_equal_to(first.dias)

    # must return an horario similar to second
    found = u.search_horario(date(2022,1,17))
    assert_that(found.dias).is_equal_to(second.dias)

@test('Get horarios between 2 dates')
def _(u=user(), first=first(), second=second()):
    '''Test that searching for horarios between 2 dates results on a list of 
    true and generated horarios
    '''
    # initalize dates to search between a ... b
    a = date(2021, 12, 6)
    b = date(2022,  1, 3)

    # search for horarios but dates are inverted must return an empty list
    arr = u.get_horarios_between(b, a)
    assert_that(len(arr)).is_equal_to(0)

    # search for horarios must return an list of size 5, containing
    # horarios equal or similar to [first, first, first, second, second]
    arr = u.get_horarios_between(a, b)

    # test size
    assert_that(len(arr)).is_equal_to(5)

    # test first date 
    assert_that(arr[0].fecha_inicio).is_equal_to(a)

    # test horarios 
    assert_that(arr[0].dias).is_equal_to(first.dias)
    assert_that(arr[1].dias).is_equal_to(first.dias)
    assert_that(arr[2].dias).is_equal_to(first.dias)
    assert_that(arr[3].dias).is_equal_to(second.dias)
    assert_that(arr[4].dias).is_equal_to(second.dias)

    # test last date 
    assert_that(arr[4].fecha_inicio).is_equal_to(b)
