--������ �������� (���)
--EXISTS ������ - ���������� ����� ������ TRUE ������ FALSE
SELECT DNAME FROM DEPT WHERE DEPTNO = 10;  -- ����� �ϳ� �����ϱ� ������ TRUE
--EXISTS �����ڿ��� TRUE�� ����� �Ǹ� �տ� SQL ���� ���������� ������ ��
SELECT * FROM EMP WHERE EXISTS (SELECT DNAME FROM DEPT WHERE DEPTNO = 10);
SELECT * FROM EMP;
SELECT DNAME FROM DEPT WHERE DEPTNO = 100;  -- ����� �������� �ʱ� ������ FALSE
--EXISTS �����ڿ��� FALSE�� ����� �Ǹ� �տ� SQL ���� ���������� ������ ���� ���� = ������ ��� ����
SELECT * FROM EMP WHERE EXISTS (SELECT DNAME FROM DEPT WHERE DEPTNO = 100);
--���߿� �������� = ���� ������ = ������ ��������
--�ǹ����� �� ���� ����ϹǷ� �� ���!
SELECT DEPTNO, MIN(SAL) FROM EMP GROUP BY DEPTNO;
SELECT * FROM EMP WHERE (DEPTNO, SAL) IN (SELECT DEPTNO, MIN(SAL) FROM EMP GROUP BY DEPTNO);
SELECT DEPTNO, MAX(SAL) FROM EMP GROUP BY DEPTNO;
SELECT * FROM EMP WHERE (DEPTNO, SAL) IN (SELECT DEPTNO, MAX(SAL) FROM EMP GROUP BY DEPTNO);
--FROM  �� �ڿ� ����ϴ� ��������
--�ζ��� �� = SQL �� ���� ����� ��ġ ���̺�ó�� ��� 
SELECT * FROM EMP WHERE DEPTNO = 30;
SELECT * FROM DEPT;
SELECT  E30.EMPNO, E30.ENAME, D.DEPTNO, D.DNAME 
    FROM (SELECT * FROM EMP WHERE DEPTNO = 30) E30,
         (SELECT * FROM DEPT) D
    WHERE E30.DEPTNO = D.DEPTNO;
--�ζ��κ信 ����ϴ� SQL���� ������ٸ� WITH �� ����ϸ� ��
--�������� ���̱� ���� ����
--WITH ������ �̸� ������ �ľ��� �� ���� => SELECT ���� ������ ������ ��
WITH E30 AS (SELECT * FROM EMP WHERE DEPTNO = 30),
     D AS (SELECT * FROM DEPT)
SELECT  E30.EMPNO, E30.ENAME, D.DEPTNO, D.DNAME 
    FROM () E30,
         () D
    WHERE E30.DEPTNO = D.DEPTNO;

