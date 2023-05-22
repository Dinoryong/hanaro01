--주석 : CTRL + /
--실행 : CTRL + ENTER
--사원정보
DESC EMP;
--부서정보
DESC DEPT;
--급여등급 정보
DESC SALGRADE;
-- SQL 기본 문법
-- 전체 열 : *
SELECT * FROM  EMP;
-- 특정 열 : 열 이름
SELECT ENAME FROM EMP;
-- 특정 열 여러개 : 열 이름, 열 이름 쉼표로 구분
SELECT ENAME, EMPNO FROM EMP;
-- 특정 조건 : WHERE 절
SELECT * FROM EMP WHERE SAL > 3000;
-- 