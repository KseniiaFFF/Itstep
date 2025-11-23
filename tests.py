from calc import input_calc

def test_str():
    assert input_calc('h', '+', 4) == 'no number'

def test_str2():
    assert input_calc('h', '+', 'd') == 'no number'    

def test_znak():
    assert input_calc(2, 9, 8) == 'Error'    

def test_znak2():
    assert input_calc(2, ')', 8) == 'Error'      

def test_zero():
    assert input_calc(5, '/', 0) == 'del 0'  

def test_pos_plus():
    assert input_calc(5, '+', 2) == 7

def test_pos_minus():
    assert input_calc(5, '-', 2) == 3

def test_pos_proiz():
    assert input_calc(5, '*', 2) == 10

def test_pos_del():
    assert input_calc(5, '/', 2) == 2.5            

def test_pos_st():
    assert input_calc(5, '**', 2) == 25