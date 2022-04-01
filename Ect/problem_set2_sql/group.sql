-- lv2 고양이와 개는 몇 마리 있을가
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS COUNT FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE

-- lv2 동명 동물 수 찾기
SELECT TMP.NAME, TMP.COUNT FROM (SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME) AS TMP WHERE TMP.COUNT > 1 ORDER BY TMP.NAME

-- lv2 입양 시각 구하기 1
SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR(DATETIME)) AS COUNT FROM ANIMAL_OUTS WHERE HOUR(DATETIME) BETWEEN 9 AND 19 GROUP BY HOUR ORDER BY HOUR

-- lv4 입양 시각 구하기 2
WITH RECURSIVE TMP AS(SELECT 0 AS HOUR UNION ALL SELECT HOUR + 1 FROM TMP WHERE HOUR < 23)
SELECT T.HOUR, COUNT(HOUR(A.DATETIME)) FROM TMP AS T LEFT OUTER JOIN ANIMAL_OUTS AS A ON T.HOUR = HOUR(A.DATETIME) GROUP BY T.HOUR ORDER BY T.HOUR