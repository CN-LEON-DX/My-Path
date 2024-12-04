SELECT 
    CASE
        WHEN g.grade < 8 THEN NULL
        ELSE s.name
    END,
    g.grade,
    s.marks
FROM Students as s 
JOIN Grades as g
ON g.min_mark <= s.marks and g.max_mark>= s.marks
ORDER BY grade DESC, s.name


// My optimize solution 
SELECT 
    CASE
        WHEN FLOOR(s.marks/10) + 1 < 8 THEN NULL
        ELSE s.name
    END,
    CASE
        WHEN s.marks = 100 then 10
        ELSE FLOOR(s.marks/10) + 1 
    END as grade,
    s.marks
FROM Students as s 
ORDER BY grade DESC, s.name
