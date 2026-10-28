select * from ventes;
-- a
SELECT Sum(c3 * c4) FROM ventes;

-- b
select c2, Sum(c4) from ventes group BY c2;

-- c
select c5, Sum(c4) from ventes group BY c5;