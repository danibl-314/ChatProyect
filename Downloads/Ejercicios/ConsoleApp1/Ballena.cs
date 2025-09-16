using System;

class Ballena : Animal
{
    public override void Comer()
    {
        Console.WriteLine("La ballena está comiendo plancton");
    }

    public void Nadar()
    {
        Console.WriteLine("La ballena está nadando.");
    }
}