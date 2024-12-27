import System.IO
import Data.List

eval :: String -> Int
eval [] = 0
eval ('\\':'\\':xs) = 1 + eval xs
eval ('\\':'\"':xs) = 1 + eval xs
eval ('\\':'x':_:_:xs) = 1 + eval xs
eval (_:xs) = 1 + eval xs

part1 :: [String] -> Int
part1 xs = sum [length x | x <- xs] - sum (map (eval . init . tail) xs)

encode :: String -> Int
encode [] = 0
encode ('\\':xs) = 2 + encode xs
encode ('\"':xs) = 2 + encode xs
encode (_:xs) = 1 + encode xs
 
part2 :: [String] -> Int
part2 xs = sum (map encode xs) - sum [length x | x <- xs] + 2 * length xs

main :: IO ()
main = do
    inp <- readFile "input.txt"
    let inp' = lines inp
    print $ part1 inp'
    print $ part2 inp'