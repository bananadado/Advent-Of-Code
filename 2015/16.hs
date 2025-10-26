import Data.Maybe (fromJust)

{-
we need to iterate through every sue and see which ones can be plausibly matched
in theory there is only one possible sue
this should be insanely easy but im in haskell so we'll see - its probably faster to just have a look through manually

CONCLUSION: IT IS FASTER TO JUFST LOOK AT THE SUES AGH
-}

type Compound = (String, Int)

-- wow was this annoying to input
msg :: String
msg = "children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1"
msg' :: [Compound]
msg' = parseCompounds $ words msg

-- found on stack overflow
removePunc :: String -> String
removePunc xs = [ x | x <- xs, x `notElem` ",.?!-:;\"\' " ]

-- lookup is guaranteed so we can just
lookUpCmp :: String -> Int
lookUpCmp s = fromJust $ lookup s msg'

{-
Takes in a list of [a, b, a, b ..] and parses a's into compounds and b's into quantities
-}
parseCompounds :: [String] -> [Compound]
parseCompounds [] = []
parseCompounds (a:b:xs) = (a', b') : parseCompounds xs
    where
        a' = removePunc a
        b' = read (removePunc b) :: Int

parseInput :: String -> [(Int, [Compound])]
parseInput input = map parseLine $ lines input
    where
        parseLine :: String -> (Int, [Compound])
        parseLine line = (num, parseCompounds ws)
            where
                (_:n:ws) = words line
                num = read (init n) :: Int

-- just need to check whether this is possible
match :: [Compound] -> Bool
match [] = True
match ((name, qty):cs) = qty == lookUpCmp name && match cs

part1 :: [(Int, [Compound])] -> Int
part1 xs = head [n | (n, ys) <- xs, match ys]

-- > cats, trees, < pomeranians, goldfish
match' :: [Compound] -> Bool
match' [] = True
match' (("cats", qty):cs) = qty > lookUpCmp "cats" && match cs
match' (("trees", qty):cs) = qty > lookUpCmp "trees" && match cs
match' (("pomeranians", qty):cs) = qty < lookUpCmp "pomeranians" && match cs
match' (("goldfish", qty):cs) = qty < lookUpCmp "goldfish" && match cs
match' ((name, qty):cs) = qty == lookUpCmp name && match cs


part2 :: [(Int, [Compound])] -> Int
part2 xs = head [n | (n, ys) <- xs, match' ys]

main :: IO ()
main = do
    input <- readFile "input.txt"
    let list = parseInput input
    print $ part1 list
    print $ part2 list