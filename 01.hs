import System.IO
import Data.List (words, splitAt, intercalate)

part1 :: String -> Int
part1 [] = 0
part1 (x:xs)
    | x == '('  = part1 xs + 1
    | otherwise = part1 xs - 1

part2 :: String -> Int
part2 ls = go ls 0
    where
        go :: String -> Int -> Int
        go (x: xs) n
            | n < 0     = 0
            | x == '('  = 1 + go xs (n + 1)
            | otherwise = 1 + go xs (n - 1)

main :: IO ()
main = do
    inp <- readFile "input.txt"
    putStrLn $ "Part 1: " ++ show (part1 inp)
    putStrLn $ "Part 2: " ++ show (part2 inp)