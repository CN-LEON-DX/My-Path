SELECT 
    hk.hacker_id, 
    hk.name
FROM 
    Submissions AS s
JOIN 
    Challenges AS ch ON s.challenge_id = ch.challenge_id
JOIN 
    Difficulty AS diff ON ch.difficulty_level = diff.difficulty_level
JOIN 
    Hackers AS hk ON s.hacker_id = hk.hacker_id
WHERE 
    s.score = diff.score 
GROUP BY 
    hk.hacker_id, hk.name
HAVING 
    COUNT(DISTINCT s.challenge_id) > 1 
ORDER BY 
    COUNT(DISTINCT s.challenge_id) DESC, 
    hk.hacker_id;
