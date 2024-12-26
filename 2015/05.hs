import System.IO
import Data.List

threeVowels :: String -> Bool
threeVowels s = (length $ filter (`elem` "aeiou") s) >= 3

doubleLetter :: String -> Bool
doubleLetter [x] = False
doubleLetter (x:y:xs)
    | x == y    = True
    | otherwise = doubleLetter (y:xs)

notForbidden :: String -> Bool
notForbidden s = not $ any (`isInfixOf` s) ["ab", "cd", "pq", "xy"]

isNice1 :: String -> Bool
isNice1 s = threeVowels s && doubleLetter s && notForbidden s

part1 :: [String] -> Int
part1 xs = length $ filter isNice1 xs

doubleLetterSpace :: String -> Bool
doubleLetterSpace [x,y] = False
doubleLetterSpace (x:y:z:xs)
    | x == z    = True
    | otherwise = doubleLetterSpace (y:z:xs)

hasRepeatingPair :: String -> Bool
hasRepeatingPair s = any (\(x, rest) -> x `isInfixOf` rest) pairs
  where pairs = [(take 2 t, drop 2 t) | t <- init $ tails s, length t >= 2]

isNice2 :: String -> Bool
isNice2 s = doubleLetterSpace s && hasRepeatingPair s

part2 :: [String] -> Int
part2 xs = length $ filter isNice2 xs


main :: IO ()
main = do
    inp <- readFile "input.txt"
    let inp' = lines inp
    print $ part1 inp'
    print $ part2 inp'
