select COUNT(*) as count from ECOLI_DATA
where  (GENOTYPE & 2) = 0
and (GENOTYPE & 5) != 0;