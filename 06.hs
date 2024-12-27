-- Might be some of the worst code ever written.
-- Takes a full minute to run.
import System.IO
import Data.List

type Coord = (Int, Int)

part1 :: [(String, Coord, Coord)] -> Int
part1 xs = length [status |(_, status) <- go xs [((x, y), False) | x <- [0 .. 999], y <- [0 .. 999]], status]
    where
        go :: [(String, Coord, Coord)] -> [(Coord, Bool)] -> [(Coord, Bool)]
        go [] bulbs = bulbs
        go ((action, (x1, y1), (x2, y2)): xs) bulbs =
            case action of
                "on" -> go xs [((x, y), (x >= x1 && x <= x2 && y >= y1 && y <= y2) || status) | ((x, y), status) <- bulbs]
                "off" -> go xs [((x, y), (not (x >= x1 && x <= x2 && y >= y1 && y <= y2)) && status) | ((x, y), status) <- bulbs]
                "toggle" -> go xs [((x, y), (x >= x1 && x <= x2 && y >= y1 && y <= y2) /= status) | ((x, y), status) <- bulbs] -- XOR

part2 :: [(String, Coord, Coord)] -> Int
part2 xs = sum [brightness |(_, brightness) <- go xs [((x, y), 0) | x <- [0 .. 999], y <- [0 .. 999]]]
    where
        go :: [(String, Coord, Coord)] -> [(Coord, Int)] -> [(Coord, Int)]
        go [] bulbs = bulbs
        go ((action, (x1, y1), (x2, y2)): xs) bulbs =
            case action of
                "on" -> go xs [((x, y), bright + fromEnum (x >= x1 && x <= x2 && y >= y1 && y <= y2)) | ((x, y), bright) <- bulbs]
                "off" -> go xs [((x, y), bright - fromEnum ((x >= x1 && x <= x2 && y >= y1 && y <= y2) && bright > 0)) | ((x, y), bright) <- bulbs]
                "toggle" -> go xs [((x, y), bright + 2 * fromEnum (x >= x1 && x <= x2 && y >= y1 && y <= y2)) | ((x, y), bright) <- bulbs]


parseInput :: String -> [(String, Coord, Coord)]
parseInput inp = map parseLine (lines inp)
    where
        parseLine :: String -> (String, Coord, Coord)
        parseLine s =
            case words s of
                ("turn":"on":coords) -> parseCoords "on" coords
                ("turn":"off":coords) -> parseCoords "off" coords
                ("toggle":coords) -> parseCoords "toggle" coords
        
        parseCoords :: String -> [String] -> (String, Coord, Coord)
        parseCoords a [c1, "through", c2] = (a, parsePoint c1, parsePoint c2)
        
        parsePoint :: String -> Coord
        parsePoint p = let (x, y) = break (== ',') p in (read x, read (tail y))


main :: IO ()
main = do
    inp <- readFile "input.txt"
    let parsed = parseInput inp
    print $ part1 parsed
    print $ part2 parsed