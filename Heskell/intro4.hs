--mapper :: (a -> b) -> [a] -> [b]
--mapper _ [] = []
--mapper f (x:xs) = f x : mapper f xs

--aufsummieren :: [Int] -> [Int]
--aufsummieren (x:xs) = x: map (+) foldl (sum [x..]) xs

fibonaccim :: [Int]
fibonaccim = 0:1:(zipWith (+) fibonaccim (tail fibonaccim))

enthalten :: (Eq a) => a -> [a] -> Bool
enthalten _ [] = False
enthalten f (x:xs)
    | filter (==f) (x:xs) == [f] = True 
    | otherwise = False

quadrat :: Eq a => Fractional a => a -> a -> a
quadrat n q
    | n/q == q = q
    | otherwise = quadrat n ((q + n/q) / 2)

sieb :: [Int]-> [Int]
sieb (x:xs) = filter (\y -> mod y x /= 0) xs

prime :: [Int]
prime = map head (iterate sieb [2..])