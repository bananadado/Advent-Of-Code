using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Day9
{
    internal class Day09
    {
        static (int, int) mossa((int x, int y) currentCoordsH, (int x, int y) currentCoordsT)
        {
            if (currentCoordsH.y == currentCoordsT.y && currentCoordsH.x == currentCoordsT.x) { } //check if the same
            else if (currentCoordsH.y == currentCoordsT.y && (currentCoordsT.x - currentCoordsH.x == -1 || currentCoordsH.x - currentCoordsT.x == -1)) { } //check if next to each other, parallel to x axis
            else if (currentCoordsH.x == currentCoordsT.x && (currentCoordsT.y - currentCoordsH.y == -1 || currentCoordsH.y - currentCoordsT.y == -1)) { } //check if next to each other, parallel to y axis
            else if ((currentCoordsT.x - currentCoordsH.x == -1 || currentCoordsH.x - currentCoordsT.x == -1) && (currentCoordsT.y - currentCoordsH.y == -1 || currentCoordsH.y - currentCoordsT.y == -1)) { }//check for directly diagonal
            else
            {
                if (currentCoordsH.y == currentCoordsT.y)
                {
                    if (currentCoordsH.x > currentCoordsT.x)//move right
                    {
                        currentCoordsT.x++;
                    }
                    else//move left
                    {
                        currentCoordsT.x--;
                    }
                }
                else if (currentCoordsT.x == currentCoordsH.x)
                {
                    if (currentCoordsH.y > currentCoordsT.y)//move up
                    {
                        currentCoordsT.y++;
                    }
                    else//move down
                    {
                        currentCoordsT.y--;
                    }
                }
                else//move diagonally
                {
                    if (currentCoordsT.x < currentCoordsH.x)
                    {
                        currentCoordsT.x++;
                    }
                    else
                    {
                        currentCoordsT.x--;
                    }
                    if (currentCoordsT.y < currentCoordsH.y)
                    {
                        currentCoordsT.y++;
                    }
                    else
                    {
                        currentCoordsT.y--;
                    }
                }
            }
            return currentCoordsT;
        }


        static void Main(string[] args)
        {
            List<string> input = new List<string>();
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    input.Add(sr.ReadLine());
                }
            }


            List<(int, int)> coordsVisited = new List<(int, int)>();

            (int x, int y) currentCoordsH = (0, 0);
            List<(int, int)> through19 = new List<(int, int)>() { (0,0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0) };


            foreach (string move in input)
            {
                for (int i = 0; i < int.Parse(move.Split(' ')[1]); i++)
                {
                    switch (move.Split(' ')[0])
                    {
                        case "D":
                            currentCoordsH.y--;
                            break;
                        case "U":
                            currentCoordsH.y++;
                            break;
                        case "R":
                            currentCoordsH.x++;
                            break;
                        case "L":
                            currentCoordsH.x--;
                            break;
                    }

                    through19[0] =  mossa(currentCoordsH, through19[0]);


                    for (int j = 1; j < 9; j++)
                    {
                        through19[j] = mossa(through19[j - 1], through19[j]);
                    }


                    bool isBeenVisited = false;
                    foreach ((int x1, int y1) in coordsVisited)
                    {
                        (int x2, int y2) = through19[8];
                        if (x2 == x1 && y2 == y1)
                        {
                            isBeenVisited = true;
                        }
                    }
                    if (!isBeenVisited)
                    {
                        coordsVisited.Add(through19[8]);
                    }
                }
                    
            }

            //Part 1 is very similar except without the list of tuples, just accounting for a head and a tail
            Console.WriteLine("Part 2: "+coordsVisited.Count());
            
            Console.ReadKey();
        }
    }
}
