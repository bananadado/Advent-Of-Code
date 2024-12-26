import System.IO
import Data.List (words, splitAt, intercalate)
import Text.Read
import Data.List.Split (splitOn)

part1 :: [(Int, Int, Int)] -> Int
part1 = sum . map surfaceArea
  where
    surfaceArea (l, w, h) = 
        let s1 = l * w
            s2 = l * h
            s3 = w * h
        in 2 * (s1 + s2 + s3) + minimum [s1, s2, s3]

part2 :: [(Int, Int, Int)] -> Int
part2 = sum . map ribbon
    where ribbon (l, w, h) = l * w * h + 2 * (l + w + h) - 2 * maximum [l, w, h]

parseInput :: String -> [(Int, Int, Int)]
parseInput = map parseLine . lines
  where parseLine line = let [x, y, z] = map read (splitOn "x" line) in (x, y, z)

main :: IO ()
main = do
    inp <- readFile "input.txt"
    let inp' = parseInput inp
    print $ part1 inp'
    print $ part2 inp'