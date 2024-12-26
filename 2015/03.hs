import System.IO
import Data.List (words, splitAt, nub)

type Coord = (Int, Int)

calcPositions :: String -> [Coord]
calcPositions = scanl move (0, 0)
    where
        move :: Coord -> Char -> Coord
        move (x, y) '^' = (x, y + 1)
        move (x, y) '>' = (x + 1, y)
        move (x, y) 'v' = (x, y - 1)
        move (x, y) '<' = (x - 1, y)

part1 :: String -> Int
part1 = length . nub . calcPositions

splitList :: String -> (String, String)
splitList [] = ([],[])
splitList (x1:x2:xs) = (x1:y1, x2:y2)
    where (y1, y2) = splitList xs

part2 :: String -> Int
part2 xs = length $ nub $ (calcPositions y1) ++ (calcPositions y2)
    where (y1, y2) = splitList xs

main :: IO ()
main = do
    inp <- readFile "input.txt"
    print $ part1 inp
    print $ part2 inp