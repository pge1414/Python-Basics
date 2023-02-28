index:: [Int] -> Int -> Int
index [] _ = error "leer"
index (x:xs) n
    |x == n = 0
    |otherwise = 1+ index xs n

--anzahl :: [Int] -> Int -> Int
--anzahl [] _ = 0
--anzahl (x:xs) n
--    |x == n = 1+ anzahl xs n
--    |otherwise = anzahl xs n

sortiert :: [Int] -> Bool
sortiert [] = error "leer"
sortiert [x] = True
sortiert (x:y:ys)
    |x <= y = sortiert (y:ys)
    |otherwise = False

ersteN :: Int -> [Int]
ersteN 0 = []
ersteN n = ersteN(n-1) ++ [n]

länge :: [Char] -> Int
länge [] = 0
länge [x] = 1
länge (x:xs) = länge xs +1

anzahlen :: [Char] -> [Int]
anzahlen [] = []
anzahlen [x] = [1]
anzahlen(x:y:ys)
    | x == y = head anzahlenTail +1 : tail anzahlenTail
    | otherwise = 1: anzahlen (y:ys)
    where anzahlenTail = anzahlen (y:ys)

--packen :: [Char] -> [[Char]]
--packen [] = []
--packen [x] = [[x]]
--packen(x:y:ys) 
--    | x == y = x:head packenTail:tail packenTail
--    | otherwise = [x]:packenTail
--    where packenTail = packen (y:ys)

flipper :: (a -> b -> c) -> (b -> a -> c)
flipper f x y = f y x

