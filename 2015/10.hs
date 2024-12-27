import System.IO
import Data.List

extend :: String -> Char -> Int -> String
extend [] prev count = show count ++ [prev]
extend (x : xs) prev count
    | x == prev = extend xs prev (count + 1)
    | otherwise = show count ++ [prev] ++ extend xs x 1

solve :: String -> Int -> Int
solve x 0 = length x
solve (x: xs) n = solve (extend xs x 1) (n - 1)

main :: IO ()
main = do
    inp <- readFile "input.txt"
    print $ solve inp 40
    print $ solve inp 50