-- icl i am beyond confused
-- memoization is quite difficult in haskell
-- for part 2 i just went into the text file and replace the value -> b with the output of the program and then ran again
import System.IO
import Data.List hiding (insert)
import Data.List.Split (splitOn)
import Data.Bits
import Data.Word (Word16)
import Data.Map 
import Text.Read (readMaybe)
import qualified Data.Map as Map

solve :: Map String [String] -> Map String Word16 -> String -> (Word16, Map String Word16)
solve circuit memo wire
    | member wire memo = (memo ! wire, memo)
    | otherwise = (res, insert wire res memo')
    where
        (res, memo') = case circuit ! wire of 
            [n] -> val n memo
            [x, "AND", y] -> binOp (.&.) x y memo
            [x, "OR", y]  -> binOp (.|.) x y memo
            [x, "LSHIFT", n] -> shiftOp shiftL x n memo
            [x, "RSHIFT", n] -> shiftOp shiftR x n memo
            ["NOT", x]     -> let (v, m) = val x memo in (complement v, m)
            
        val :: String -> Map String Word16 -> (Word16, Map String Word16)
        val x m = case readMaybe x of
            Just n -> (n, m)
            Nothing -> solve circuit m x
        
        binOp :: (Word16 -> Word16 -> Word16) -> String -> String -> Map String Word16 -> (Word16, Map String Word16)
        binOp op x y m = let (vx, mx) = val x m
                             (vy, my) = val y mx
                         in (op vx vy, my)
        
        shiftOp :: (Word16 -> Int -> Word16) -> String -> String -> Map String Word16 -> (Word16, Map String Word16)
        shiftOp op x n m = let (vx, mx) = val x m
                       in (vx `op` read n, mx)


parseInput :: String -> [(String, [String])]
parseInput inp = Data.List.map go (lines inp)
    where
        go :: String -> (String, [String])
        go line = let (x:y:_) = splitOn " -> " line in (y, words x)


main :: IO ()
main = do
    inp <- readFile "input.txt"
    let parsed = parseInput inp
    let (x, _) = solve (fromList parsed) Data.Map.empty "a"
    print x