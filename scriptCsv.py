#Generar archivo csv
import csv
totalHipoteca= 10000
mensualidad= 375
anualidad=500
tasa_interes_mensual=0.5
mes=1
i=1
deuda= totalHipoteca
interes=(deuda * tasa_interes_mensual)/100
cantidad_adeudada= deuda+ interes
with open('tabla.csv', 'w', newline='') as csvFile:
    columnas = ['Month', 'Interest', 'Due', 'Due + interest', 'To pay']         
    writer=csv.writer(csvFile,delimiter=',')
    writer.writerow(columnas)
    while deuda <= 10000 and  deuda > 0: 
            
        datos= [mes,round(interes,2), round(deuda,2), round(cantidad_adeudada,2),mensualidad]          
        i= i + 1            
        mes = mes+1 
        deuda= cantidad_adeudada - mensualidad
        interes=(deuda * tasa_interes_mensual)/100
        cantidad_adeudada= deuda+ interes 
        
        #cada año pagamos una cuota anual           
        if  (mes % 12 == 0) :
            mensualidad = mensualidad + anualidad
        elif(deuda<375):
            mensualidad= round(cantidad_adeudada,2)       
        else:
            mensualidad =375
        
        writer.writerow(datos)
csvFile.close()        