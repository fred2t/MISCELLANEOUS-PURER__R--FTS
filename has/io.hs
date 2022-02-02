main :: IO ()
main = do
    i <- getLine
    if i /= 'quit' then do
        putStrLn("input: " ++ i)
     else
        return ()
