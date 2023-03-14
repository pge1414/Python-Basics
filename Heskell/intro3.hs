folder :: (Int -> Int -> Int) -> Int -> [Int] -> Int
folder f b [] = b
folder f b [x] = f b x
folder f b (x:y:ys) = folder f b (ys ++ [f x y])

addiere :: Int-> Int -> Int
addiere a b = a + b

evenn :: [Int] -> [Int]
evenn [] = []
evenn [x] = [x]
evenn (x:xs)
    | mod x 2 == 0 = x : evenn xs
    | otherwise = 0 : evenn xs

flipper :: (a -> b -> c) -> (b -> a -> c)
flipper f x y = f y x

quicksort :: Ord a => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = quicksort (filter (<=x) xs) ++ [x] ++ quicksort (filter (>x) xs)

summe:: Int 
summe = folder addiere 0 (evenn [1..20000])

enthalten :: [a] -> a -> Bool
enthalten [] a = False
enthalten (x:xs)
    | filter x a == True = True
    | otherwise = enthalten (filter xs a)