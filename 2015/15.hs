type Ingredient = (Int, Int, Int, Int, Int)


score :: [(Int, Ingredient)] -> Int
score xs = product $ map (max 0) [cap, dur, fla, tex]
    where
        (cap, dur, fla, tex) = foldr add (0, 0, 0, 0) xs
        add :: (Int, Ingredient) -> (Int, Int, Int, Int) -> (Int, Int, Int, Int)
        add (qty, (c, d, f, t, _)) (ac, ad, af, at) = (ac + qty * c, ad + qty * d, af + qty * f, at + qty * t)

-- brute force should be fine since theres only (100 + 4 - 1) C (4 - 1) combinations
-- generate all distributions - i.e. all ways to place 3 fence posts among 100 items
distributions :: Int -> Int -> [[Int]]
distributions 1 total = [[total]]
distributions n total = [ x:rest | x <- [0..100], rest <- distributions (n - 1) (total - x)]

part1 :: [Ingredient] -> Int
part1 is = maximum [ score (zip amt is) | amt <- distributions (length is) 100]

cals :: [(Int, Ingredient)] -> Int
cals xs = sum [ amt * c | (amt, (_, _, _, _, c)) <- xs]

part2 :: [Ingredient] -> Int
part2 is = maximum [ score (zip amt is) | amt <- distributions (length is) 100, cals (zip amt is) == 500]

parseInput :: String -> [Ingredient]
parseInput input = map parseLine (lines input)
    where
        parseLine :: String -> Ingredient
        parseLine line = (cap, dura, flav, text, cal)
            where
                ws = words line

                clean s = if last s == ',' then init s else s
                readNum i = read (clean (ws !! i)) :: Int

                cap = readNum 2
                dura = readNum 4
                flav = readNum 6
                text = readNum 8
                cal = readNum 10

main :: IO ()
main = do
    input <- readFile "input.txt"
    let list = parseInput input
    print $ part1 list
    print $ part2 list