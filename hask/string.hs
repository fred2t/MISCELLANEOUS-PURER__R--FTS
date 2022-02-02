import Data.List
import Data.Char
import System.IO

lower :: String -> String
lower = map toLower

findStrings :: [String] -> String -> [String]
findStrings sws text = [ w | w <- sws, (lower w) `elem` txtwords ]
    where
        ftext = filter (\x -> isLetter x || isSpace x) text
        txtwords = map lower $ words ftext 
