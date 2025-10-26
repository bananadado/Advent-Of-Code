{-
Bin packing!
If only lists were easier to use...
Appears to be 20 lines of input and 2^20 is brute forceable...
so i'll just generate all sets
-}

powerSet :: [a] -> [[a]]
powerSet [] = [[]]
powerSet (x:xs) = let ps = powerSet xs in ps ++ map (x:) ps

part1 :: [Int] -> Int
part1 xs = length . filter ((==150) . sum) $ powerSet xs

part2 :: [Int] -> Int
part2 xs = length . filter (==minl) $ xs'
    where
        xs' = [length s | s <- powerSet xs, sum s == 150]
        minl = minimum xs'

main :: IO ()
main = do
    input <- readFile "input.txt"
    let list = map (\x -> read x :: Int) $ lines input
    print $ part1 list
    print $ part2 list