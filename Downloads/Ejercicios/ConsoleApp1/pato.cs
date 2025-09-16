using System;

class Pato : Animal, IVolar
{
    public override void Comer()
    {
        Console.WriteLine("El pato está comiendo semillas");
    }

    public void Volar()
    {
        Console.WriteLine("El pato está volando.");
    }
    
    public void Graznar()
    {
        Console.WriteLine("El pato está graznando.");
    }
}