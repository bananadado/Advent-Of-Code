import Data.List (permutations)
import qualified Data.Map as M
import Data.Maybe (mapMaybe)
import qualified Data.Set as S


type DistanceMap = M.Map (String, String) Int

parseInput :: String -> DistanceMap
parseInput = M.fromList . concatMap parseLine . lines
  where parseLine l = let [loc1, _, loc2, _, dist] = words l
                  in [((loc1, loc2), read dist), ((loc2, loc1), read dist)]

calculateDistances :: DistanceMap -> [String] -> [Int]
calculateDistances distMap = mapMaybe (traverseRoute distMap) . permutations
  where
    traverseRoute :: DistanceMap -> [String] -> Maybe Int
    traverseRoute m (x:y:xs) = (+) <$> M.lookup (x, y) m <*> traverseRoute m (y:xs)
    traverseRoute _ _ = Just 0

solve :: DistanceMap -> [Int]
solve distMap = calculateDistances distMap locations
  where locations = S.toList (M.keysSet (M.mapKeys fst distMap))


main :: IO ()
main = do
  inp <- readFile "input.txt"
  let inp' = parseInput inp
  let paths = solve inp'
  print $ minimum paths
  print $ maximum paths