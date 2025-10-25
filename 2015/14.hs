type Reindeer = (Int, Int, Int)

distance :: Reindeer -> Int -> Int
distance (speed, time, rest) seconds = total
    where
        dist = speed * time
        combo = time + rest
        (goes, extra) = divMod seconds combo
        total = dist * goes + min extra time * speed

part1 :: [Reindeer] -> Int -> Int
part1 deers seconds = maximum (map (`distance` seconds) deers)

-- brute force should be fine for part two since its only O(n * 2503)
part2 :: [Reindeer] -> Int -> Int
part2 deers seconds = maximum finalScores
    where
        step :: [Int] -> Int -> [Int]
        step scores t = newScores
            where
                dists = map (`distance` t) deers
                lead = maximum dists
                newScores = zipWith (+) scores [if d == lead then 1 else 0 | d <- dists]
        
        n = length deers
        finalScores = foldl step (replicate n 0) [1 .. seconds]

parseInput :: String -> [Reindeer]
parseInput input = map parseLine (lines input)
    where
        parseLine :: String -> Reindeer
        parseLine line = (speed, time, rest)
            where
                wordsList = words line
                speed = read (wordsList !! 3) :: Int
                time = read (wordsList !! 6) :: Int
                rest = read (wordsList !! 13) :: Int

main :: IO ()
main = do
    input <- readFile "input.txt"
    let list = parseInput input
    print $ part1 list 2503
    print $ part2 list 2503
