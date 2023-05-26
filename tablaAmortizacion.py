totalHipoteca= 10000
mensualidad= 375
anualidad=500
tasa_interes_mensual=0.5
mes=1
i=1
deuda= totalHipoteca
interes=(deuda * tasa_interes_mensual)/100
cantidad_adeudada= deuda+ interes

while deuda <= 10000 and  deuda > 0:
    #mostramos los datos solicitados
    print("Month " + str(mes)+ ", Interest " + str(f"{interes:.2f}") + ", due: " + str(f"{deuda:.2f}")
            + " ,due + interest " + str(f"{cantidad_adeudada:.2f}") + ", to pay " + str(f"{mensualidad:.2f}")) 
    i= i + 1            
    mes = mes+1 
    deuda= cantidad_adeudada - mensualidad
    interes=(deuda * tasa_interes_mensual)/100
    cantidad_adeudada= deuda+ interes 

    #cada año pagamos una cuota anual           
    if  (mes % 12 == 0) :
        mensualidad = mensualidad + anualidad  
    elif(deuda<375):
        mensualidad= cantidad_adeudada
    else:
        mensualidad =375
    