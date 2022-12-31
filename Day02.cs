using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Day2._0
{
    internal class Day02
    {
        static void Main(string[] args)
        {
            //if statements galore (switches)
            //I know conversion to ascii would be faster
            //I can't be bothered to rewrite part 1 but it is basically the same idea
            int score = 0;
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    string input = sr.ReadLine();
                    string[] move = input.Split(' ');
                    switch (move[1])
                    {
                        case "Z":
                            switch (move[0])
                            {
                                case "A":
                                    move[1] = "B";
                                    break;
                                case "B":
                                    move[1] = "C";
                                    break;
                                case "C":
                                    move[1] ="A";
                                    break;
                            }
                            break;
                        case "Y":
                            move[1] = move[0];
                            break;
                        case "X":
                            switch (move[0])
                            {
                                case "A":
                                    move[1] = "C";
                                    break;
                                case "B":
                                    move[1] = "A";
                                    break;
                                case "C":
                                    move[1] = "B";
                                    break;
                            }
                            break;
                    }
                    switch (move[1])
                    {
                        case "A":
                            score++;
                            break;
                        case "B":
                            score += 2;
                            break;
                        case "C":
                            score += 3;
                            break;
                    }

                    if (move[0] == move[1])
                    {
                        score += 3;
                    }
                    else if ((move[0] == "A" && move[1] == "C") || (move[0] == "B" && move[1] == "A") || (move[0] == "C" && move[1] == "B"))
                    {
                        continue;
                    }
                    else
                    {
                        score += 6;
                    }
                    
                }
            }
            Console.WriteLine(score);
            Console.ReadKey();
        }
    }
}
