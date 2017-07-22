# Usando miranda para detectar S.0 #


Miranda es una herramienta de administración de UPnP escrita en Python.


# Pero primero ¿Que es UPnP ? #

UPnP (Universal Plug-N-Play) es un protocolo que permite que varios dispositivos de red se autoconfiguren por si mismos. 

En pocas palabras este protocolo es capaz de autoconfigurar los puertos de un dispositivo que soporte UPnP para evitar la tediosa tarea de abrir y cerrar puertos
para la correcta utilizacion de un sofware

Usualmente lo utilizamos en la consola de videojuegos, cuando intentamos conectar el chat de voz y video
, Por ejemplo Sony por ejemplo utiliza  el puerto TCP 80, 443, 3478, 3479, 3480, 8080 y UDP  3478, 3479 entre otros


Por lo tanto Sony nos recomiendo que si nuestro router soporta UPnp lo usemos, ya que este configurara automaticamente la apertura de estos puertos


# Funcionamient de UPnp #

Los router que soporta UPnp utilizan dirección multicast (multidifusión) 239.255.255.250 y el puerto TCP 1900 para comunicar a otros dispotivos que ofrece el servicio UPnp
esto lo hace mediante una peticion SSDP NOTIFIY, la cual se envia periodicamente y en caso de que un dispisitivo en la redes quisiera tomar el servicio enviaria una peticion SSDP RESPONDE

![alt-text](img/notify.png)

Tambien cuandoo nuestro dispositivo quiere encontrar a otro dispositivo UPnp este o hace enviando una peticion SSDP MSEARCH 

![alt-text](img/msearch.png)


# ¿Como detecto el sistemas opetativo mediante UPnp? #

Dado a que nuestro sistemas emite estas comunicaciones automaticamente de forma multicast por el puerto 1900
podemos interceptar estas peticiones y analizarlas, para eso usaremos miranda


# Descubriendo hosts UPnP con Miranda # 

Primero ejecutamos en nuestra shell, el comando miranda el cual nos brindara un shell interactiva

 Para descubrir los host, utilizamos el comando pcap, o msearch

  * Cuando es ejecutado el comando ‘pcap’, Miranda se pondrá en escucha (modo pasivo) buscando mensajes SSDP NOTIFY.
  * Cuando es ejecutado el comando ‘msearch’ consultará los dispositivos UPnP usando un mensaje M-SEARCH. Por defecto, ‘msearch’ buscará todos los dispositivos UPnP.

![alt-text](img/kali.png)

Como podemos ver aquellos dispositivos compatibles con UPnp se encuentran emitienco peticiones msearch o notify  y gracias a esto, tenemos un indicio del S.0 que utiliza
se preguntaran ese link a que sitio redirigue, UPnp utiliza SOAP para el intercambio   y transmision de paquetes donde describre y especifica
las configuracion y dispositivos soportados, esta informacion viaja junto a los paquetes msearch y notify con el que podremos obtener mucha mas informacion acerca de nuestro objetivo, pero por lo que esta face concierne, solo la utilizamos para intentar descubrir el tipo y version de sistemas operativo de nuestra victima


Si desea leer mas acerca de este herramienta e informacion que puede brindar acerca de un objetivo, puede visitar la siguiente pagina:
 
https://www.dragonjar.org/hacking-de-redes-upnp-parte-i.xhtml
