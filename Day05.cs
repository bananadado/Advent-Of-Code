using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day5
{
    internal class Day05
    {
        static void Main(string[] args)
        {
            List<List<string>> crates = new List<List<string>>();
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                //The 9s and 8 are hardcoded in unfortunately but I did my best parsing straight from the file
                for (int j = 0; j < 9; j++)
                {
                    crates.Add(new List<string>());
                }
                for (int i = 0; i <8; i++)
                {
                    string line = sr.ReadLine();
                    for (int j = 0; j < 9; j++)
                    {
                        int pos = j * 4 + 1;
                        string crate = line.Substring(pos, 1);
                        if (crate != " ")
                        {
                            crates[j].Add(crate);
                        }
                    }
                }
                foreach (List<string> no in crates)
                {
                    no.Reverse();
                }
                
                sr.ReadLine();
                sr.ReadLine();
                while (!sr.EndOfStream)
                {
                    string move = sr.ReadLine();
                    string[] wheretogo = move.Split(' ');
                    List<string> tempList = new List<string>();
                    for (int i= 0; i < int.Parse(wheretogo[1]); i++)
                    {
                        
                        string temp = crates[int.Parse(wheretogo[3]) - 1].Last();
                        crates[int.Parse(wheretogo[3]) - 1].RemoveAt(crates[int.Parse(wheretogo[3]) - 1].Count - 1);
                        
                        //part 1 is the same but instead of adding to this temporary list, you add straight to the destination sublist
                        tempList.Add(temp);

                    }
                    for  (int i= int.Parse(wheretogo[1])-1; i >= 0; i--)
                    {
                        crates[int.Parse(wheretogo[5]) - 1].Add(tempList[i]);
                    }
                }
            }

            Console.WriteLine("Part 2: (read the last letter in each row)");
            foreach (List<string> no in crates)
            {
                foreach (string s in no)
                {
                    Console.Write(s);
                }
                Console.WriteLine();
            }
            Console.ReadKey();
        }
    }
}
