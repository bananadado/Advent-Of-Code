import Data.Bits (testBit, setBit, shiftL, bit, (.|.), popCount, Bits (..))
import Data.Maybe (fromMaybe)
import qualified Data.Map as Map
import Data.List (nub)

type HappinessMap = Map.Map (String, String) Int
type Guest = String

-- Get the happiness value for two guests
happiness :: HappinessMap -> Guest -> Guest -> Int
happiness happinessMap a b = fromMaybe 0 (Map.lookup (a, b) happinessMap) + fromMaybe 0 (Map.lookup (b, a) happinessMap)

-- bellman held-karp like dp approach
-- why was this so difficult
-- dp[S][i] = maximum happiness visiting subset S and ending at person i
-- we will use a bit mask to go through our sets
-- O(2^n * n^2) complexity :skull:
heldKarp :: [Guest] -> HappinessMap -> Int
heldKarp names w = maximum [dpFinal Map.! (maskAll, i) + happiness w first i | i <- others]
  where
    n = length names
    first = head names
    others = tail names
    idx = Map.fromList (zip names [0..])
    maskAll = (1 `shiftL` n) - 1

    -- Base cases:
    dp0 = Map.fromList [((bit (idx Map.! first) .|. bit (idx Map.! i), i), happiness w first i) | i <- others]

    -- dp table
    dpFinal = foldl step dp0 [3..n]

    step :: Map.Map (Int, Guest) Int -> Int -> Map.Map (Int, Guest) Int 
    step dp subsetSize = foldl (update subsetSize) dp subsets
      where
        subsets = [ s | s <- [0..maskAll]
                      , popCount s == subsetSize
                      , testBit s (idx Map.! first) ]
        update _ dp s = foldl (updateEnd s) dp others
        updateEnd s dp i
          | not (testBit s (idx Map.! i)) = dp
          | otherwise =
              let s' = clearBit s (idx Map.! i)
                  bestPrev = maximum [ dp Map.! (s', j) + happiness w j i
                                      | j <- others
                                      , testBit s' (idx Map.! j) ]
              in Map.insert (s, i) bestPrev dp


-- Parse input into guests and happiness map
parseInput :: [String] -> ([Guest], HappinessMap)
parseInput lines =
  let parseLine line =
        let wordsList = words line
            personA = head wordsList
            personB = init (last wordsList)
            sign = if wordsList !! 2 == "gain" then 1 else -1
            value = read (wordsList !! 3) :: Int
        in ((personA, personB), sign * value)
      happinessPairs = map parseLine lines
      happinessMap = Map.fromList happinessPairs
      guests = nub $ concatMap (\(a,b) -> [a,b]) (Map.keys happinessMap)
  in (guests, happinessMap)

main :: IO ()
main = do
  input <- readFile "input.txt"
  let (guests, happinessMap) = parseInput (lines input)

  -- part 1
  print $ heldKarp guests happinessMap

  -- part 2 - literally took 2 seconds
  print $ heldKarp ("me" : guests) happinessMap
