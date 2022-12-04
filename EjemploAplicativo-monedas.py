#EJEMPLO APLICATIVO
#Supongamos que estás cavando en tu patio trasero y descubres una bolsa de 20 monedas de oro. 
#Al día siguiente, te escabullas al sótano y encuentras una máquina replicadora que tu abuelo 
#tenía escondido y donde afortunadamente puedes meter las 20 monedas de oro. 
#Entonces, metes las 20 monedas y luego de unas rato escuchas un zumbido y ves como de la máquina salen 
#10 monedas de oro más aparte de las 20 que metiste inicialmente.
#¿Cuántas monedas tendrías si hicieras ese mismo procedimiento todos los días durante un año?
#Realizando
#Primero creamos nuestras variables y datos del ejemplos; año ->365 dias;
Inicio_monedas = 20 #Al inicio tengo 20 monedas y al cabo de 1 dia me devuelven la mitad
#Entonces mi cantidad de monedas que tendre al final sera lo que tenia al inicio mas lo que se creo Creo 
#por la maquina 
Creado_por_la_maquina=10
#1 dia
#Final_monedas=Inicio_monedas=20 + Creado_porla_Maquina=10 --> Final_monedas = 30
#2 dia
#Final_monedas=Inicio_monedas=20 + Creado_porla_Maquina(dia1)=10 + Creado_porla_Maquina(dia2)=10 --> Final_monedas = 40
#3 dia
#Final_monedas=Inicio_monedas=20 + Creado_porla_Maquina(dia1)=10 + Creado_porla_Maquina(dia2)=10 +Creado_porla_Maquina(dia3)=10 --> Final_monedas = 50
#364 dia
#Final_monedas=Inicio_monedas=20 + Creado_porla_Maquina(dia1)=10 + Creado_porla_Maquina(dia2)=10 +.....+Creado_porla_Maquina(dia363)=10 + Creado_porla_Maquina(dia364)=10 + --> Final_monedas = 3660
#365 dia
#Final_monedas=Inicio_monedas=20 + Creado_porla_Maquina(dia1)=10 + Creado_porla_Maquina(dia2)=10 +.....+Creado_porla_Maquina(dia364)=10 + Creado_porla_Maquina(dia365)=10 + --> Final_monedas = 3670
#Modelandolo en forma general tenemos que el total de monedas que tendre dentro de un año es 
#cantidad de monedas del inicio + (cantidad de monedas creadas por la maquina)*dia
print("**************************************************************")
Final_monedas = Inicio_monedas + Creado_por_la_maquina*365
print(f"Al final de un año tendremos {Final_monedas} monedas")
#Ahora viendolo de una manera mas de programacion tenemos que
print("**************************************************************")
for dia in range(365):
   Final_monedas = Inicio_monedas+Creado_por_la_maquina
   Creado_por_la_maquina = Creado_por_la_maquina+10
   print(f"Dia {dia+1} tendremos {Final_monedas} monedas creadas")
print("**************************************************************")
print(f"Al final de un año tendremos {Final_monedas} monedas")
print("**************************************************************")
