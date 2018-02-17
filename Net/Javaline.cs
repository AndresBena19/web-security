using System;
using System.Threading;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Threads
{
    //Clase singleton 
    public sealed class Singleton
    {
        //Usamos un diccionario para almacenar el nombre del jugador y el mejor de 3  lanzamientos 
        public Dictionary<string, int> Positions = new Dictionary<string, int>();

        // Almacenamos el nombre de los jugadores en una lista, Inicialmente son 30
        public List<String> Competitors_name = new List<String>() {"Andres","Pedro","jose","veinte","jair","jaime","jairo","zuñiga","ivan","juan",
                                                  "danilo","cunladue","pablo","victor","daniel","mateo","estefa","margarita","josue","felipe",
                                                   "edgar","medina","wilmer","pianeta","francisco","almanza","david","curso","gustavo","cuadrado"};


        /* Creamos un metodo que nos permitira invocar la misma instancia si importar el hilo que la invoque, ademas 
           Ademas la  implementación permite que solo un subproceso ingrese al área crítica, identificada por el bloque de bloqueo, 
           cuando aún no se ha creado ninguna instancia de Singleton */

        private static volatile Singleton instance;
        private static object syncRoot = new Object();

        private Singleton() { }

        public static Singleton Get_Instance
        {
            get
            {
                if (instance == null)
                {
                    lock (syncRoot)
                    {
                        if (instance == null)
                            instance = new Singleton();
                    }
                }

                return instance;
            }


        }

    }




    class Program
    {

        //Clase principal 
        private static void Main(string[] args)
        {

            /*Inicializamos una lista que contendra los valores,del numero de jugardores que se seleccionaran por ronda, 
             Inicialmente son 30 jugadores, del los cuales solo derivan 10 y finalmente 3*/
            List<int> Rounds = new List<int>() {10,3};


           
            foreach (int number in Rounds)
            {
                Console.Write("----------JAVALIN THROW-------------" + "\n");
                Go(number);
                Console.Write("\n");
            }
       
            Console.Read();

         
        
        }


        public static void Go(int number) {

            //Instanciamos una lista que almacenara los hilos
            List<Thread> Threads_competitor = new List<Thread>();

            //Instanciamos un objeto de la clase singleton
            Singleton Score = Singleton.Get_Instance;

            //Pasamos como parametro el nombre de los jugardores  y la lista que almacenara los hilos, para la creacion de los procesos
            Create_thread(Score.Competitors_name, Threads_competitor);


           //Imprimimos el mejor puntaje de cada jugador
            foreach (string key in Score.Positions.Keys)
            {

                    Console.Write(key + " -> " + Score.Positions[key] + " <- MEJOR DE 3 LANZAMIENTOS " +"\n");
            }

            // Order by values.
            // ... Use LINQ to specify sorting by value.

            //Una vez terminado cada round ordenamos de forma descendente los valores de cada jugador en condigo su llave
            var items = from pair in Score.Positions
                        orderby pair.Value descending
                        select pair;


            //Declaramos un diccionario que almacenara estos nuevos valores ordenados de mayor a menor
            Dictionary<string, int> New_Dict = items.ToDictionary(r => r.Key, r => r.Value);


            //Almacenamos los mejore n jugadores de cada round en este caso, inicialmente son 10 y 3
            List<String> Best_ten = new List<String>(New_Dict.Keys);

            //Una vez terminado un round, limpiamos la lista que almacena los nombres en la clase singleton, para asi poder almacenar los nombre de los nuevos
            Score.Competitors_name.Clear();

            //Ingresamos los nombres de los nuevos jugadores
            for (int i=0;i<number;i++)
            {
                Score.Competitors_name.Add(Best_ten[i]);
            }
            Console.Write("\n" + "-------------MEJORES  " + number +" POSICIONES ----------" + "\n");

            //Imprimimos los nombre de los mejores jugadores de cada roun
            for(int i =0; i<number;i++)
            {
                Console.Write("jUGADOR  -> " + Score.Competitors_name[i]+ " POSICION -> " + (i+1) + "\n");
            }

            //Una vez terminado un round, limpiamos el diccionario que almancena el nombre y el puntaje de cada jugador, para almacenar los nuevos 
            Score.Positions.Clear();

        }

        //Este metodo Creara los proceso a ejecutar
        public static void Create_thread(List<string> Competitors_name, List<Thread> Threads_competitor)
        {
             //Creamos por cada jugador en la lista un hilo, el cual es nombrado con el nombre del jugador, y almacenado en la lista
            foreach (String C_Name in Competitors_name)
            {
                Thread newThread = new Thread(Throw);
                newThread.Name = C_Name;
                Threads_competitor.Add(newThread);
            }

            //Iniciamos en paralelo cada de uno de los procesos almacenados en al lista
            foreach (Thread Competitor in Threads_competitor)
            {

                Competitor.Start();
            }

            //Esperamos a que todos los hilos finalicen la tarea, para continuar
            foreach (Thread Competitor in Threads_competitor)
            {
               Competitor.Join();
            }

        }

        //Esta sera la rutina que sera ejecutada por cada hilo
        public static void  Throw()
            {   
                //Cada hilo instanciara un objecto de la clase singleton
                Singleton Score = Singleton.Get_Instance;

                //Instanciamos un objecto de la clase ramdon 
                Random random = new Random();

                //Instanciamos un lista donde se almacenaran los 3 tiros de cada jugador (hilo)
                List<int> shots = new List<int>();

                
                for (int i = 0; i < 3; i++)
                {   //Generamos un valor aleatorio entre 0 y 100
                    int value = random.Next(0, 100);
                    //Almacenamos en valor en la lista 
                    shots.Add(value);
                } 
            
            //Bloqueamos el acceso a cualquier atributo de la clase singleton si otro hilo se encuentra modificandolo
            lock ((object)Score)
            {   //Agreamos el nombre del jugador y su mejor puntaje al diccionario de la clase singleton
                Score.Positions.Add(Thread.CurrentThread.Name, shots.Max());

            }



        }

    }
    }






