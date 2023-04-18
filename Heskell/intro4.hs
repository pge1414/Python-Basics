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

quadrat :: Num a => Eq a => Fractional a => a -> a -> a
quadrat n q
    | q*q == n = q
    | otherwise = quadrat n ((q + n/q) / 2)

eratosthenes :: Num a x => Eq a => n -> [a]
eratosthenes 0 = 0
eratosthenes a
    |  mod a 2 == 0 = a && filter 1 (\mod x a /= 0) [1..n]
    | otherwise = eratosthenes a