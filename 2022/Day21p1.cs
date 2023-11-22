using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day21
{
    internal class Program
    {
        static List<string> monkeys = new List<string>();
        static List<List<string>> monkeyOp = new List<List<string>>();
        static ulong part1(int monkeyIndex)
        {
            if (monkeyOp[monkeyIndex].Count() == 1)
            {
                return ulong.Parse(monkeyOp[monkeyIndex][0]);
            }
            switch (monkeyOp[monkeyIndex][1])
            {
                case "*":
                    return part1(monkeys.IndexOf(monkeyOp[monkeyIndex][0])) * part1(monkeys.IndexOf(monkeyOp[monkeyIndex][2]));
                case "+":
                    return part1(monkeys.IndexOf(monkeyOp[monkeyIndex][0])) + part1(monkeys.IndexOf(monkeyOp[monkeyIndex][2]));                   
                case "-":
                    return part1(monkeys.IndexOf(monkeyOp[monkeyIndex][0])) - part1(monkeys.IndexOf(monkeyOp[monkeyIndex][2]));                    ;
                case "/":
                    return part1(monkeys.IndexOf(monkeyOp[monkeyIndex][0])) / part1(monkeys.IndexOf(monkeyOp[monkeyIndex][2]));                    
            }
            return 1;
        }
        static void Main(string[] args)
        {
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    string line = sr.ReadLine();
                    monkeys.Add(line.Split()[0].Trim(':'));
                    List<string> list = new List<string>();
                    for (int i = 1; i < line.Split().Length; i++)
                    {
                        list.Add(line.Split()[i]);
                    }
                    monkeyOp.Add(list);
                }
            }

            Console.WriteLine(part1(monkeys.IndexOf("root")));

            //part 2 in python because you cannot actually store a big enough number

            //ulong target = part1(monkeys.IndexOf(monkeyOp[monkeys.IndexOf("root")][2]));
            //Console.WriteLine(target); 
            //ulong high = 200000000;
            //ulong low = 0;
            //ulong midpoint;
            //while (true)
            //{
            //    midpoint = ((high + low) / 2);
            //    monkeyOp[monkeys.IndexOf("humn")][0] = (midpoint).ToString();

            //    ulong score = target - part1(monkeys.IndexOf(monkeyOp[monkeys.IndexOf("root")][0]));
            //    Console.WriteLine(score.ToString());
            //    if (score == 0)
            //    {
            //        Console.WriteLine(midpoint.ToString());
            //        break;
            //    }
            //    if (score < 0)
            //    {
            //        low = midpoint;
            //    }
            //    if (score > 0)
            //    {
            //        high = midpoint;
            //    }

            //}
            Console.ReadKey();
        }
    }
}
