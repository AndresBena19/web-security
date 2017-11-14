import numpy
import scipy.stats as stats

#Para las llegadas se generaran numeros aleatorios que se comporten con una distribucion Poisson con lambda 5

chairs = 10
horas = 9
def getArrivals():
    data = []
    for i in range(9):
        data.append(numpy.random.poisson(5))

    return data


print("llegadas")
data = getArrivals()

print(data)


def getServices():
    data2 = []

    for i in range(horas):
        data2.append(numpy.random.exponential(15))

    return data2

print("Servicios: ")
data2 = getServices()
print(data2)




def checkChairs(array):
    count1 = 0
    count2 = 0
    #Ciclo para recorrer cada hora del sistema
    for i in range(len(array)):

        if(array[i] >= 4):

            count1+= array[i]-4
            if(count1 > chairs):
                count2 = count1 - chairs

    return count2, count1 - count2


def meanGetter(array):
    sum = 0.0
    for i in range(len(array)):
        sum = sum + array[i]

    return sum/len(array)



#-------------------------------------------------------------------------------------------------------------

promDelay = []
promServices = []
promWaits = []
promInter = []

for i in range(1000):


    a = [] #Arreglo de llegadas para usar en el algoritmo
    s = [] #Arreglo de servicios para usar en el algoritmo
    c = [] #arreglo de partida de las personas
    d = [] #arreglo de delays
    r = [] #arreglo de interarrivals


    si = 0.0 #Variable that collects services sum
    di = 0.0 #Variable that collects delays sum
    w = 0.0 #Variable that collects wait sum
    ri = 0.0 #Variable that collects r sum


    c.append(0.0)


    for i in range(horas):

        if (data[i] < c[i-1]):
            d.append(c[i-1] - data[i])
        else:
            d.append(0.0)

        s.append(data2[i])
        c.append(data[i] + d[i]+s[i]) #Cn = an+dn+sn

        si += s[i]#sum of services
        di += d[i] #sum of delays
        w += d[i] + s[i] # wait = delay + service
        r.append(data[i] - data[i-1])
        ri += r[i]
        #print(ri)

    #promedio de delays
    promDelay.append(di/9)

    #promedio de servicios
    promServices.append(si/9)

    #Promedio de esperas
    promWaits.append(w/9)

    #Promedio de tiempo entre llegadas
    promInter.append(ri/9)

#delays
print("Retrasos (di)")
print(d)
#interrivals
print("Tiempo entre llegadas (r)")
print(r)

print("Promedio de delays", meanGetter(promDelay))
print("Promedio de servicios", meanGetter(promServices))
print("Promedio de Espera", meanGetter(promWaits))
print("Promedio de Interr", meanGetter(promInter))

respuestas = checkChairs(data)

print("Customers lost during the course of the day: ", respuestas[0])
print("Customers that remain in the shop at closing time", respuestas[1])


#Promedio de llegadas para concluir la ultima parte

print("Promedio de llegadas:",meanGetter(data))