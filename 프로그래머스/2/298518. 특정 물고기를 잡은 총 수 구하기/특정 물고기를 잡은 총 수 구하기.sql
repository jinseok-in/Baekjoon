-- 코드를 작성해주세요
SELECT COUNT(fi.ID) as FISH_COUNT
FROM FISH_INFO as fi
JOIN (SELECT * FROM FISH_NAME_INFO WHERE FISH_NAME = "BASS" OR FISH_NAME = "SNAPPER") as fni
WHERE fi.FISH_TYPE = fni.FISH_TYPE;
