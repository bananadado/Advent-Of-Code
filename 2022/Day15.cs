using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Day15
{
    internal class Day15
    {
        static List<(int x, int y)> sensors = new List<(int x, int y)>();
        static List<(int x, int y)> beacons = new List<(int x, int y)>();
        static List<int> row2000000 = new List<int>();
        static List<(int x1, int x2)> ranges = new List<(int x1, int x2)>();

        static void part1(int input)
        {
            List<int> BeaconsInRow = new List<int>();
            for (int i = 0; i < beacons.Count; i++)
            {
                if (beacons[i].y == 10)
                {
                    BeaconsInRow.Add(beacons[i].x);
                }
            }

            for (int i = 0; i < sensors.Count; i++)
            {
                int distanceX = Math.Abs(sensors[i].x - beacons[i].x);
                int distanceY = Math.Abs(sensors[i].y - beacons[i].y);

                int absoluteDistance = Math.Abs(sensors[i].y - input);


                if (distanceY + distanceX < absoluteDistance)
                {
                    continue;
                }
                else
                {
                    for (int j = 0; j <= Math.Abs(absoluteDistance - (distanceX + distanceY)); j++)
                    {


                        if (!BeaconsInRow.Contains(sensors[i].x + j))
                        {
                            row2000000.Add(sensors[i].x + j);
                        }
                        if (!BeaconsInRow.Contains(sensors[i].x - j))
                        {
                            row2000000.Add(sensors[i].x - j);

                        }
                    }
                }
            }
        }

        static void part2(int input)
        {

            for (int i = 0; i < sensors.Count; i++)
            {
                int distanceX = Math.Abs(sensors[i].x - beacons[i].x);
                int distanceY = Math.Abs(sensors[i].y - beacons[i].y);

                int absoluteDistance = Math.Abs(sensors[i].y - input);

                if (distanceY + distanceX < absoluteDistance)
                {
                    continue;
                }
                else
                {
                    ranges.Add((sensors[i].x + (absoluteDistance - (distanceX + distanceY)), sensors[i].x - (absoluteDistance - (distanceX + distanceY))));
                }
            }
        }


        static void Main(string[] args)
        {
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    string[] line = sr.ReadLine().Split(' ');


                    sensors.Add((int.Parse(line[2].Split('=')[1].Trim(',')), int.Parse(line[3].Split('=')[1].Trim(':'))));
                    beacons.Add((int.Parse(line[8].Split('=')[1].Trim(',')), int.Parse(line[9].Split('=')[1].Trim(':'))));
                }
            }

            //part 1 my part 1 was 1 too high as didn't account for sensor on the line - proceed with caution
            part1(2000000);
            List<int> list = row2000000.Distinct().ToList();
            Console.WriteLine("part 1: "+list.Count());

            //part 2
            //BRUTE FORCE
            for (int j = 0; j < 4000001; j++)
            {
                part2(j);

                bool overlap = true;

                while (ranges.Count() > 1)
                {
                    for (int k = 1; k < ranges.Count(); k++)
                    {
                        if (((ranges[k].x1 <= ranges[0].x1 && ranges[0].x1 <= ranges[k].x2) || (ranges[0].x1 <= ranges[k].x1 && ranges[k].x1 <= ranges[0].x2) || ranges[0].x1 - ranges[k].x2 == 1 || ranges[k].x1 - ranges[0].x2 == 1) )
                        {
                            (int x, int y) bob;
                            if (ranges[k].x1 < ranges[0].x1)
                            {
                                bob.x = ranges[k].x1;
                            }
                            else
                            {
                                bob.x = ranges[0].x1;
                            }
                            if (ranges[k].x2 > ranges[0].x2)
                            {
                                bob.y = ranges[k].x2;
                            }
                            else
                            {
                                bob.y = ranges[0].x2;
                            }
                            ranges.Add(bob);
                            ranges.RemoveAt(k);
                            ranges.RemoveAt(0);
                            break;
                        }
                    }

                    if (ranges.Count() == 2 && !(ranges[1].x1 <= ranges[0].x1 && ranges[0].x1 <= ranges[1].x2 || (ranges[0].x1 <= ranges[1].x1 && ranges[1].x1 <= ranges[0].x2) || ranges[0].x1 - ranges[1].x2 == 1 || ranges[1].x1 - ranges[0].x2 == 1))
                    {
                        overlap = false;
                        break;
                    }

                }
                
                if (!overlap)
                {
                    Console.WriteLine("processing..\npart 2: ");
                    ranges.Sort((a, b) => a.Item1.CompareTo(b.Item1));
                    ulong multiplied =  ((ulong)ranges[0].x2 + 1) * 4000000;
                    Console.WriteLine(multiplied + (ulong)j);
                    break;
                }

                ranges.Clear();
            }

            Console.WriteLine("Done!");
            Console.ReadKey();
        }
    }
}
