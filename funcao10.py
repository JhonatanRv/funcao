def f_para_c(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c
    
temp_f = 75
temp_c = f_para_c(temp_f)
print(temp_f, "Graus para Fahrenheit equlivalem a", temp_c, "Graus Celsius")
temp_c_arrendondado = round(temp_c, 1)
print(temp_f, "Graus para Fahrenheit equlivalem a", temp_c_arrendondado, "Graus Celsius")