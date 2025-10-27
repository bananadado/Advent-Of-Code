{-
my first thought is how on earth do I do this?
2D array manipulation...

we will make an (n+2) * (n+2) grid and store as a map

after implementation - it'd have been quicker to directly work with map and just ignore '.' 's entirely
 - wouldve been faster not to convert to string and back, however, the principles are exactly the same
-}
import Data.Map as M (Map, lookup, fromList, elems, insert)
import Data.Maybe (fromJust)
import Data.List (intercalate)

type State = Char
type Cell = (Int, Int)
type Grid = M.Map Cell State

-- need the cell and the count of the on neighbours
updateState :: State -> Int -> State
updateState _ 3   = '#'
updateState '#' 2 = '#'
updateState _ _   = '.'

neighbourLocs :: Cell -> [Cell]
neighbourLocs (x, y) = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]

getNeighbours :: Grid -> Cell -> Int
getNeighbours grid c = length . filter (=='#') $ Prelude.map (fromJust . (\(x, y) -> M.lookup (x, y) grid)) $ neighbourLocs c

updateGrid :: Grid -> Int -> Grid
updateGrid grid n = g'
    where (g', _) = parseInput $ intercalate "\n" [[updateState (fromJust $ M.lookup (x, y) grid) (getNeighbours grid (x, y)) | x <- [1..n]] | y <- [1..n]]

part1 :: Grid -> Int -> Int -> Int
part1 g _ 0 = length . filter (=='#') $ M.elems g
part1 g n i = part1 g' n (i - 1)
    where g' = updateGrid g n

forceCorners :: Grid -> Int -> Grid
forceCorners g n = foldr (`M.insert` '#') g corners
  where corners = [(1,1),(1,n),(n,1),(n,n)]

part2 :: Grid -> Int -> Int -> Int
part2 g _ 0 = length . filter (=='#') $ M.elems g
part2 g n i = part2 g'' n (i - 1)
    where
        g' = updateGrid g n
        g'' = forceCorners g' n

parseInput :: String -> (Grid, Int)
parseInput input = (M.fromList $ concatMap parseLine $ (zipWith (\x s -> (x, '.' : s ++ "."))  [0..] . (border :) . (++ [border]) . lines) input, n)
    where
        n = length (lines input)
        border = replicate n '.'
        parseLine :: (Int, String) -> [(Cell, State)]
        parseLine (x, states) = zipWith (\y e -> ((x, y), e)) [0..] states

main :: IO ()
main = do
  input <- readFile "input.txt"
  let (grid, n) = parseInput input

  print $ part1 grid n 100
  print $ part2 (forceCorners grid n) n 100
