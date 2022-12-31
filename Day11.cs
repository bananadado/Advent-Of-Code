using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Runtime.InteropServices;

namespace Day11
{
    internal class Day11
    {
        static List<List<ulong>> monkeyItems = new List<List<ulong>>();
        static List<string> monkeyOperations = new List<string>();
        static List<int> monkeyTests = new List<int>();
        static List<int> throwIfTrue = new List<int>();
        static List<int> throwIfFalse = new List<int>();
        static List<int> Inspected = new List<int>();

        static void makeMoves(int monkey)
        {
            List<ulong> currentMonkeyItems = new List<ulong>();

            foreach (ulong i in monkeyItems[monkey])
            {
                currentMonkeyItems.Add(i);
            }

            monkeyItems[monkey].Clear();

            foreach (ulong i in currentMonkeyItems)
            {
                Inspected[monkey]++;
                ulong worry  = 0 ;

                switch(monkeyOperations[monkey].Split(' ')[1])
                {
                    case "*":
                        try
                        {
                            worry = i * ulong.Parse(monkeyOperations[monkey].Split(' ')[2]);
                        }
                        catch (Exception)
                        {
                            worry = i * i;
                        }
                        break;
                    case "+":
                        try
                        {
                            worry = i + ulong.Parse(monkeyOperations[monkey].Split(' ')[2]);
                        }
                        catch (Exception)
                        {
                            worry = i + i;
                        }
                        break;
                }
                worry = worry % (5*2*13*7*19*11*3*17); //unfortunately it is hardcoded
                if (worry % (ulong)monkeyTests[monkey] == 0)
                {
                    monkeyItems[throwIfTrue[monkey]].Add(worry);
                }
                else
                {
                    monkeyItems[throwIfFalse[monkey]].Add(worry);
                }
            }
        }

        static void Main(string[] args)
        {
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    string line = sr.ReadLine().Trim(' ');
                    string[] parts = line.Split(' ');

                    switch (parts[0])
                    {
                        case "Starting":
                            List<ulong> monkey = new List<ulong>();
                            for (int i = parts.Length - 1; i >= 0; i--)
                            {
                                try
                                {
                                    monkey.Add(ulong.Parse(parts[i].Trim(',')));
                                }
                                catch (Exception)
                                {
                                    break;
                                }
                            }
                            monkeyItems.Add(monkey);
                            break;
                        case "Operation:":
                            monkeyOperations.Add(parts[parts.Length - 3] + " " +parts[parts.Length - 2] + " " + parts[parts.Length-1]);
                            break;
                        case "Test:":
                            monkeyTests.Add(int.Parse(parts[parts.Length - 1]));
                            break;
                        case "If":
                            if (parts[1] == "true:")
                            {
                                throwIfTrue.Add(int.Parse(parts[parts.Length - 1]));
                            }
                            else
                            {
                                throwIfFalse.Add(int.Parse(parts[parts.Length - 1]));
                            }
                            break;
                    }
                }
            }

            for (int i = 0; i < monkeyOperations.Count; i++)
            {
                Inspected.Add(0);
            }

            //Part 1 is the exact same but 20 instead of 10000 and instead of %(5*2*13*7*19*11*3*17) it is /3
            for (int i = 1; i <= 10000; i++)
            {
                for (int j = 0; j < monkeyOperations.Count; j++)
                {
                    makeMoves(j);
                }
            }

            Inspected.Sort();
            Inspected.Reverse();

            Console.WriteLine($"Part 2: {Inspected[0]} * {Inspected[1]} = {(ulong)Inspected[0] * (ulong)Inspected[1]}");

            Console.ReadKey();
        }
    }
}
