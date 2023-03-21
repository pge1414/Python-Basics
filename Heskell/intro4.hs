mapper :: (a -> b) -> [a] -> [b]
mapper _ [] = []
mapper f (x:xs) = f x : mapper f xs

--aufsummieren :: [Int] -> [Int]
--aufsummieren (x:xs) = x: map (+) foldl (sum [x..]) xs

fibonaccim :: [Int]
fibonaccim = 0:1:(zipWith (+) fibonaccim (tail fibonaccim))