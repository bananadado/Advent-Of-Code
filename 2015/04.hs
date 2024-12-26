import System.IO
import Data.List (words, splitAt, nub, findIndex)
import Data.Hash.MD5 (md5s, Str(..))
import Data.Maybe (fromJust)

find :: String -> Int -> Int
find prefix count = (+) 1 $ fromJust $ findIndex (leadingZeroes . hash) [1 .. ]
    where
        hash :: Int -> String
        hash n = md5s (Str (prefix ++ show n))
        leadingZeroes :: String -> Bool
        leadingZeroes xs = take count xs == replicate count '0'

part1 :: String -> Int
part1 prefix = find prefix 5

part2 :: String -> Int
part2 prefix = find prefix 6

main :: IO ()
main = do
    inp <- readFile "input.txt"
    print $ part1 inp
    print $ part2 inp