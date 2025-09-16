using System;

class Program
{
    static void Main(string[] args)
    {
        Pato lucas = new Pato();
        Ballena willy = new Ballena();

        Console.WriteLine("--- Pruebas con la Ballena ---");
        willy.Comer(); 
        willy.Nadar(); 
        Console.WriteLine(); 

        Console.WriteLine("--- Pruebas con el Pato ---");
        lucas.Comer(); 
        lucas.Volar(); 
        lucas.Graznar(); 
    }
}