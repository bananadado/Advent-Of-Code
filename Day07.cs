using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Day7._2
{
    internal class Day07
    {
        static List<string> directories = new List<string>();
        static List<int> directoryVal = new List<int>();

        static List<List<string>> pastPaths = new List<List<string>>();


        static void store(int numToStore, List<string> path)
        {
            pastPaths.Add(path);

            foreach(string s in path)
            {
                int whereInDirectory = 0;
                bool isInDirectory = false;
                for (int i = 0; i < directories.Count(); i++)
                {
                    if (s == directories[i])
                    {
                        isInDirectory = true;
                        whereInDirectory = i;
                    }
                }

                if (isInDirectory)
                {
                    directoryVal[whereInDirectory] += numToStore;
                }
                else
                {
                    directories.Add(s);
                    directoryVal.Add(numToStore);
                }
            }
        }

        static void Main(string[] args)
        {
            List<List<string>> input = new List<List<string>>();
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    input.Add(sr.ReadLine().Split(' ').ToList());
                }
            }

            List<string> currentPath = new List<string>();
            int cPathValue = 0;
            int count = 0;

            foreach (List<string> command in input)
            {
                count++;
                if (command[1] == "cd")
                {
                    if (command[2] == "..")
                    {
                        store(cPathValue, currentPath);

                        cPathValue = 0;
                        currentPath.RemoveAt(currentPath.Count()-1);
                    }
                    else
                    {
                        store(cPathValue, currentPath);
                        
                        cPathValue = 0;
                        currentPath.Add(command[2] + count); //the +count makes a new, unique directory to avoid indexing errors
                    }
                }
                else if (command[1] == "ls" || command[0] == "dir")
                {
                    continue;
                }
                else
                {
                    cPathValue += int.Parse(command[0]);
                }
            }
            store(cPathValue, currentPath); //stores the final set because my loop doesn't account for that

            int total = 0;
            foreach (int item in directoryVal)
            {
                if (item <= 100000)
                {
                    total += item;
                }
            }
            Console.WriteLine("Part 1: " + total);


            int tofind = directoryVal[0] - (70000000 - 30000000);
            int current = 1000000000; //no inf in c# :'(
            string currentdirect = " ";

            for (int i = 0; i < directories.Count(); i++)
            {
                if ( directoryVal[i] -  tofind < current - tofind && directoryVal[i] - tofind >= 0)
                {
                    currentdirect = directories[i];
                    current = directoryVal[i];
                }
            }
            
            Console.WriteLine("Part 2: (Directory: "+currentdirect +") "+ current);
            Console.ReadKey();
        }
    }
}
