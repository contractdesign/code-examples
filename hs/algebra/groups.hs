

-- see 4299319
data Elem = E | A | B | C | D deriving (Show, Eq, Enum, Bounded)

group = enumFromTo E B

--type Binop = Elem -> Elem -> Elem

binop :: Elem -> Elem -> Elem
binop E x = x
binop x E = x
binop A B = E
binop B A = E
binop A A = A
binop B B = B


--lookup :: Elem -> Elem -> Elem
--lookup



multByLeft  :: Elem -> (Elem -> Elem -> Elem) -> [Elem] -> [Elem]
multByLeft elem f group = map (\x -> f elem x) group

multByRight :: Elem -> (Elem -> Elem -> Elem) -> [Elem] -> [Elem]
multByRight elem f group = map (\x -> f x elem) group



left_inverse :: Elem -> [Elem] -> [Elem]
left_inverse elem group = filter (==E) $ map (\x -> binop elem x) group

right_inverse :: Elem -> [Elem] -> [Elem]
right_inverse elem group = filter (==E) $ map (\x -> binop x elem) group



-- compute successive powers of an element
powers :: (Elem -> Elem -> Elem) -> Elem-> [Elem]
powers f = iterate (\x -> f x x)


--order = length $ takeWhile (/= E) $ powers f E
