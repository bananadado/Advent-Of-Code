import Data.List

increment :: String -> String
increment s = reverse (increment' (reverse s))
    where
        increment' :: String -> String
        increment' [] = []
        increment' (x:xs)
            | x == 'z'  = 'a' : increment' xs
            | otherwise = succ x : xs


increasing :: String -> Bool
increasing (x:y:z:xs) = succ x == y && succ y == z || increasing (y:z:xs)
increasing _ = False

notforbidden :: String -> Bool
notforbidden s = not (any (`elem` "iol") s)

doubleDouble :: String -> Bool
doubleDouble s = length (filter (>= 2) (map length $ group s)) >= 2

valid :: String -> Bool
valid s = increasing s && notforbidden s && doubleDouble s

solve :: String -> String
solve s = head (filter valid (tail (iterate increment s)))

main :: IO()
main = do
    inp <- readFile "input.txt"
    let pt1 = solve inp
    putStrLn pt1
    putStrLn $ solve pt1
