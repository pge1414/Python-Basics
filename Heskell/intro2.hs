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

lauflängenkodierung :: [Char] -> [(Int,Char)]
lauflängenkodierung [] = []
lauflängenkodierung(x:y:ys)
    | x == y = (2,x): lauflängenkodierung ys
    | otherwise = (1,x):(1,y): lauflängenkodierung ys
