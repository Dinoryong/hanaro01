--�׷�ȭ �Լ�
--�μ� ��ȣ ���� ��� �޿� �� ���
--�μ� ��ȣ Ȯ��
SELECT DISTINCT DEPTNO FROM EMP;
--�� �μ� ��ȣ���� �ٹ��ϴ� ���� ���
SELECT * FROM EMP WHERE DEPTNO = 10;
SELECT * FROM EMP WHERE DEPTNO = 20;
SELECT * FROM EMP WHERE DEPTNO = 30;
--�� �μ� ��ȣ���� �ٹ��ϴ� �������� ��� �޿� ���
SELECT AVG(SAL) FROM EMP WHERE DEPTNO = 10;
SELECT AVG(SAL) FROM EMP WHERE DEPTNO = 20;
SELECT AVG(SAL) FROM EMP WHERE DEPTNO = 30;
--���տ����� UNION / UNION ALL ����Ͽ� �Բ� ���
SELECT '10' AS DEPTNO, AVG(SAL) FROM EMP WHERE DEPTNO = 10
UNION
SELECT '20' AS DEPTNO, AVG(SAL) FROM EMP WHERE DEPTNO = 20
UNION
SELECT '30' AS DEPTNO, AVG(SAL) FROM EMP WHERE DEPTNO = 30;
--GROUP BY ���� �̿��Ͽ� ����
SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO;
SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO ORDER BY DEPTNO;
SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO ORDER BY DEPTNO ASC;
--2���� ���� �̿��Ͽ� GROUP BY
SELECT DEPTNO, JOB, AVG(SAL) FROM EMP GROUP BY DEPTNO, JOB;
SELECT DEPTNO, JOB, AVG(SAL) FROM EMP GROUP BY DEPTNO, JOB ORDER BY DEPTNO ASC, JOB ASC;
--GROUP BY �� ����ϴ� �� �̸��� SELECT �������� �����ϰ� ���
--GROUP BY �� ������� �ʴ� �� �̸��� SELECT ������ ����ϰ� �Ǹ� ���� �߻�
SELECT DEPTNO, ENAME, AVG(SAL) FROM EMP GROUP BY DEPTNO;
--GROUP BY ~ HAVING (����)
SELECT DEPTNO, JOB, AVG(SAL) FROM EMP GROUP BY DEPTNO, JOB ORDER BY DEPTNO ASC, JOB ASC;
--��� �޿� 2000 �̻� => ��ü ��� 14���� ������ �׷�ȭ
SELECT DEPTNO, JOB, AVG(SAL) FROM EMP 
    GROUP BY DEPTNO, JOB 
    HAVING AVG(SAL) >= 2000
    ORDER BY DEPTNO ASC, JOB ASC;
--��å�� CLERK �� ��� ���
SELECT DEPTNO, JOB, AVG(SAL) FROM EMP 
    GROUP BY DEPTNO, JOB 
    HAVING JOB = 'CLERK'
    ORDER BY DEPTNO ASC, JOB ASC;
--WHERE ���� ��  => ��� 6���� ������ �׷�ȭ
SELECT DEPTNO, JOB FROM EMP WHERE SAL >= 2000;
SELECT DEPTNO, JOB, AVG(SAL) FROM EMP WHERE SAL >= 2000
    GROUP BY DEPTNO, JOB 
    HAVING AVG(SAL) >= 2000
    ORDER BY DEPTNO ASC, JOB ASC;
--�׷�ȭ�� ���õ� �Լ� = GROUP BY �� �Բ� ����ϴ� �Լ�
--���� GROUP BY �� ��� ���
SELECT DEPTNO, JOB, COUNT(*), MAX(SAL), SUM(SAL), AVG(SAL) FROM EMP
    GROUP BY DEPTNO, JOB
    ORDER BY DEPTNO ASC, JOB ASC;
--ROLLUP: ���� ���� + 1 ���� ��� ���
--1) A + B = �μ���ȣ + ��å ���� GROUP BY
--2) A = �μ���ȣ �� GROUP BY
--3) ��ü
SELECT DEPTNO, JOB, COUNT(*), MAX(SAL), SUM(SAL), AVG(SAL) FROM EMP
    GROUP BY ROLLUP(DEPTNO, JOB);
--CUBE: 2�� ���� ���� ���� ���� ��� ���
--1) A + B = �μ���ȣ + ��å ���� GROUP BY
--2) A = �μ���ȣ �� GROUP BY
--3) B = ��å ���� GROUP BY
--4) ��ü
SELECT DEPTNO, JOB, COUNT(*), MAX(SAL), SUM(SAL), AVG(SAL) FROM EMP
    GROUP BY CUBE(DEPTNO, JOB);
--ROLLUP �� �Ϻ� ���� ������ ���
--1) A + B = �μ���ȣ + ��å ���� GROUP BY
--2) A = �μ���ȣ �� GROUP BY
--��ü�� ������ ����
SELECT DEPTNO, JOB, COUNT(*), MAX(SAL), SUM(SAL), AVG(SAL) FROM EMP
    GROUP BY DEPTNO, ROLLUP(JOB);
--1) A + B = �μ���ȣ + ��å ���� GROUP BY
--2) A = ��å ���� GROUP BY
--��ü�� ������ ����
SELECT DEPTNO, JOB, COUNT(*), MAX(SAL), SUM(SAL), AVG(SAL) FROM EMP
    GROUP BY JOB, ROLLUP(DEPTNO);
--GROUPING SETS
--1) A = �μ���ȣ �� GROUP BY
--2) B = ��å ���� GROUP BY
SELECT DEPTNO, JOB, COUNT(*), MAX(SAL), SUM(SAL), AVG(SAL) FROM EMP
    GROUP BY GROUPING SETS(DEPTNO, JOB);
--GROUPING
--1) A + B = �μ���ȣ + ��å ���� GROUP BY => 0 0
--2) A = �μ���ȣ �� GROUP BY => 0 1
--3) B = ��å ���� GROUP BY => 1 0
--4) ��ü => 1 1
SELECT DEPTNO, JOB, COUNT(*), MAX(SAL), SUM(SAL), AVG(SAL), 
       GROUPING(DEPTNO), GROUPING(JOB) 
    FROM EMP
    GROUP BY CUBE(DEPTNO, JOB);
--GROUPING_ID
--1) A + B = �μ���ȣ + ��å ���� GROUP BY => 0 0 => 0
--2) A = �μ���ȣ �� GROUP BY => 0 1 => 1
--3) B = ��å ���� GROUP BY => 1 0 => 2
--4) ��ü => 1 1 => 3
SELECT DEPTNO, JOB, COUNT(*), MAX(SAL), SUM(SAL), AVG(SAL), 
       GROUPING(DEPTNO), GROUPING(JOB), GROUPING_ID(DEPTNO, JOB)
    FROM EMP
    GROUP BY CUBE(DEPTNO, JOB);
--DECODE ������ ����ִ� ���� ä������
--����ִ� �� = �׷�ȭ�� ������ ���� = GROUPING �Լ� ��� 1
SELECT DECODE(GROUPING(DEPTNO), 1, 'ALL_DEPT', DEPTNO) AS DEPTNO, 
       DECODE(GROUPING(JOB), 1, 'ALL_JOB', JOB) AS JOB, 
       COUNT(*), MAX(SAL), SUM(SAL), AVG(SAL) FROM EMP
    GROUP BY CUBE(DEPTNO, JOB);
--LISTAGG
SELECT ENAME FROM EMP;
SELECT DEPTNO, ENAME FROM EMP GROUP BY DEPTNO, ENAME ORDER BY DEPTNO ASC, ENAME ASC;
--�μ� ���� ��� �̸��� ���ĺ� ������� ������ ���� �̸��� �̸� ���̿� ', ' �� ������� ��� 
SELECT DEPTNO, 
       LISTAGG(ENAME, ', ') WITHIN GROUP(ORDER BY ENAME ASC) AS ENAME
       FROM EMP GROUP BY DEPTNO;
--�μ� ���� ��� �̸��� �޿��� ���� ������� ������ ���� �̸��� �̸� ���̿� ', ' �� ������� ��� 
SELECT DEPTNO, 
       LISTAGG(ENAME, ', ') WITHIN GROUP(ORDER BY SAL DESC) AS ENAME
       FROM EMP GROUP BY DEPTNO;
--PIVOT: ���� ���� �ٲ�
SELECT DEPTNO, JOB, MAX(SAL) FROM EMP GROUP BY DEPTNO, JOB ORDER BY DEPTNO ASC, JOB ASC;
--�μ���ȣ�� �࿡�� ���� �ٲ�
SELECT * FROM (SELECT DEPTNO, JOB, SAL FROM EMP)
    PIVOT(MAX(SAL) FOR DEPTNO IN (10, 20, 30))
    ORDER BY JOB;
--��å�� �࿡�� ���� �ٲ�
SELECT * FROM (SELECT DEPTNO, JOB, SAL FROM EMP)
    PIVOT(MAX(SAL) FOR JOB IN ('ANALYST' AS ANALYST, 
                               'CLERK' AS CLERK, 
                               'MANAGER' AS MANAGER, 
                               'PRESIDENT' AS PRESIDENT, 
                               'SALESMAN' AS SALESMAN))
    ORDER BY DEPTNO;
--DECODE ������ PIVOT ���̺� ����� ����
--��å�� �࿡�� ���� �ٲ�
SELECT DEPTNO, 
       MAX(DECODE(JOB, 'ANALYST', SAL)) AS ANALYST, 
       MAX(DECODE(JOB, 'CLERK', SAL)) AS CLERK, 
       MAX(DECODE(JOB, 'MANAGER', SAL)) AS MANAGER, 
       MAX(DECODE(JOB, 'PRESIDENT', SAL)) AS PRESIDENT, 
       MAX(DECODE(JOB, 'SALESMAN', SAL)) AS SALESMAN
    FROM EMP
    GROUP BY DEPTNO
    ORDER BY DEPTNO;
--UNPIVOT
--PIVOT ���̺��� �ٽ� UNPIVOT
SELECT * FROM(SELECT DEPTNO, 
       MAX(DECODE(JOB, 'ANALYST', SAL)) AS ANALYST, 
       MAX(DECODE(JOB, 'CLERK', SAL)) AS CLERK, 
       MAX(DECODE(JOB, 'MANAGER', SAL)) AS MANAGER, 
       MAX(DECODE(JOB, 'PRESIDENT', SAL)) AS PRESIDENT, 
       MAX(DECODE(JOB, 'SALESMAN', SAL)) AS SALESMAN
    FROM EMP
    GROUP BY DEPTNO
    ORDER BY DEPTNO)
    UNPIVOT (SAL FOR JOB IN (ANALYST, CLERK, MANAGER, PRESIDENT, SALESMAN))
    ORDER BY DEPTNO, JOB;
--
--����: ���� ���̺��� �ϳ��� ���̺�ó�� ����ϴ� ���
--�� 14��
SELECT * FROM EMP;
--�� 4��
SELECT * FROM DEPT;
--���� ���� = ũ�ν� ���� = ��� ���� ���� = 14 * 4 = 56
--���� ������ ��� ���� ����
SELECT * FROM EMP, DEPT;
SELECT * FROM EMP, DEPT ORDER BY EMP.EMPNO ASC, EMP.ENAME ASC, DEPT.DEPTNO ASC;
--����� = �������� = �ܼ�����
--���ٴ� �������� ����
SELECT * FROM EMP, DEPT WHERE EMP.DEPTNO = DEPT.DEPTNO;
--���̺� ��Ī ���
SELECT * FROM EMP A, DEPT B WHERE A.DEPTNO = B.DEPTNO;
--�� �̸��� ��üȭ�Ͽ� �ۼ��� ��!
--���̺� �̸� ���
SELECT * FROM EMP;
SELECT * FROM DEPT;
SELECT A.EMPNO, A.ENAME, A.JOB, A.MGR, A.HIREDATE, A.SAL, A.COMM,
       B.DEPTNO, B.DNAME, B.LOC
    FROM EMP A, DEPT B WHERE A.DEPTNO = B.DEPTNO;
--���̺��� ������ �ִ� ���� ��Ȯ�� ���� ���� ����
SELECT ENAME, DNAME FROM EMP A, DEPT B WHERE A.DEPTNO = B.DEPTNO;
--����Ǵ� �������� ���� �߻� => �ݵ�� ���̺� ��ó ���
SELECT ENAME, B.DEPTNO, DNAME FROM EMP A, DEPT B WHERE A.DEPTNO = B.DEPTNO;
--���� �߰�
--���ο��� �ּ� ���̺� ���� - 1 �� ��ŭ�� ������ �ʿ���
--������ �� �� ����ϰ� �ִ� ���̺� 2�� => ������ �ϳ��� �ʿ���
--������ �� �� ����ϰ� �ִ� ���̺� 3�� => ������ �� ���� �ʿ���
--��) A, B, C => A + B = ���� 1�� �ʿ�, A + B + C => ���� 1�� �ʿ� 
SELECT * FROM EMP A, DEPT B 
    WHERE A.DEPTNO = B.DEPTNO
      AND A.SAL >= 3000;
--������ = ����� �̿��� ���
--BETWEEN A AND B �������� ����
SELECT * FROM EMP;
SELECT * FROM SALGRADE;
--����
SELECT * FROM EMP A, SALGRADE B WHERE A.SAL BETWEEN B.LOSAL AND B.HISAL;
--��ü ���� = ���� ���̺� ���� �ϴ� ����
SELECT * FROM EMP;
SELECT A.EMPNO, A.ENAME, A.MGR AS MGR_EMPNO, B.ENAME AS MGR_ENAME 
    FROM EMP A, EMP B WHERE A.MGR = B.EMPNO;
--�ܺ�����
--������ �Ǵ� ���̺��� ���� ��� �� ���;� �� & ������ ���� �ʴ� ���̺��� �����ո� ����
--LEFT OUTER JOIN
--���ʿ� �ִ� ���̺��� ����
--���������� �����ʿ� �ִ� ���̺� �̸�.���̸� �ڿ� (+)
--���ӻ�� + ���ӻ���� ���� ����� ����
SELECT A.EMPNO, A.ENAME, A.MGR AS MGR_EMPNO, B.ENAME AS MGR_ENAME 
    FROM EMP A, EMP B WHERE A.MGR = B.EMPNO (+);
--RIGHT OUTER JOIN
--�����ʿ� �ִ� ���̺��� ����
--���������� ���ʿ� �ִ� ���̺� �̸�.���̸� �ڿ� (+)
--�������� + ���������� ���� ����� ����
SELECT A.EMPNO, A.ENAME, A.MGR AS MGR_EMPNO, B.ENAME AS MGR_ENAME 
    FROM EMP A, EMP B WHERE A.MGR (+) = B.EMPNO;
--SQL-99�������� ����
--����ΰ� ����� ����
--1) NATURAL JOIN
-- ���ٴ� ���� X & ����� �� �̸��� ���̺� �̸� X
SELECT A.EMPNO, A.ENAME, A.JOB, A.MGR, A.HIREDATE, A.SAL, A.COMM,
       DEPTNO, B.DNAME, B.LOC
    FROM EMP A NATURAL JOIN DEPT B;
--2) JOIN USING
-- ���ٴ� ���� => USING ����� �� ��� & ����� �� �̸��� ���̺� �̸� X
SELECT A.EMPNO, A.ENAME, A.JOB, A.MGR, A.HIREDATE, A.SAL, A.COMM,
       DEPTNO, B.DNAME, B.LOC
    FROM EMP A JOIN DEPT B USING (DEPTNO);
--3) JOIN ON
-- ���ٴ� ���� O & ����� �� �̸��� ���̺� �̸� O => �츮�� ��� ������ ���� ����
SELECT A.EMPNO, A.ENAME, A.JOB, A.MGR, A.HIREDATE, A.SAL, A.COMM,
       B.DEPTNO, B.DNAME, B.LOC
    FROM EMP A JOIN DEPT B ON (A.DEPTNO = B.DEPTNO);
--�ܺ�����
--LEFT OUTER JOIN ON
SELECT A.EMPNO, A.ENAME, A.MGR AS MGR_EMPNO, B.ENAME AS MGR_ENAME 
    FROM EMP A LEFT OUTER JOIN EMP B ON (A.MGR = B.EMPNO);
--RIGHT OUTER JOIN ON
SELECT A.EMPNO, A.ENAME, A.MGR AS MGR_EMPNO, B.ENAME AS MGR_ENAME 
    FROM EMP A RIGHT OUTER JOIN EMP B ON (A.MGR = B.EMPNO);
--FULL OUTER JOIN ON
SELECT A.EMPNO, A.ENAME, A.MGR AS MGR_EMPNO, B.ENAME AS MGR_ENAME 
    FROM EMP A FULL OUTER JOIN EMP B ON (A.MGR = B.EMPNO);
--
--��������
--WHERE �� �ڿ��� ����ϴ� ��������
--������ �������� = ����� �ϳ� = ���� 1��
SELECT SAL FROM EMP WHERE ENAME = 'JONES';
SELECT * FROM EMP WHERE SAL > 2975;
SELECT * FROM EMP WHERE SAL > (SELECT SAL FROM EMP WHERE ENAME = 'JONES');
--��¥ �����Ϳ� �Բ� ���
SELECT * FROM EMP WHERE ENAME = 'SCOTT';
SELECT HIREDATE FROM EMP WHERE ENAME = 'SCOTT';
--SCOTT ���� ���� �Ի��� ���� = SCOTT �Ի��Ϻ��� ���� ��¥ = ���� ��
SELECT * FROM EMP WHERE HIREDATE < (SELECT HIREDATE FROM EMP WHERE ENAME = 'SCOTT');
--SCOTT ���� �ʰ� �Ի��� ���� = SCOTT �Ի��Ϻ��� �̷� ��¥ = ū ��
SELECT * FROM EMP WHERE HIREDATE > (SELECT HIREDATE FROM EMP WHERE ENAME = 'SCOTT');
--������ �Լ��� �Բ� ��� = ����� �ϳ�
--��ü �������� ��� �޿�
SELECT AVG(SAL) FROM EMP;
--��ü �������� ��� �޿����� ���� �޴� ����
SELECT * FROM EMP WHERE SAL > (SELECT AVG(SAL) FROM EMP);
--������ ��������
SELECT DISTINCT DEPTNO FROM EMP;
--IN ������ = ���ٴ� OR ���� ���� �� = ������
SELECT * FROM EMP WHERE DEPTNO IN (10,20,30);
SELECT * FROM EMP WHERE DEPTNO IN (SELECT DISTINCT DEPTNO FROM EMP);
--ANY / SOME = ���� ��� �߿� �ϳ��� �����ϸ� TRUE
-- = ���� => ���ٴ� OR ���� ���� �� = ������
SELECT MAX(SAL) FROM EMP GROUP BY DEPTNO;
SELECT * FROM EMP WHERE SAL = ANY (SELECT MAX(SAL) FROM EMP GROUP BY DEPTNO);
SELECT * FROM EMP WHERE SAL = SOME (SELECT MAX(SAL) FROM EMP GROUP BY DEPTNO);
--�۴ٴ� (<) ���� = OR ���� ���� ��
--800 < 1100 < 2975 < 3000
--�ִ밪���� ���� �޿� ���� ����
SELECT SAL FROM EMP WHERE DEPTNO = 20;
SELECT * FROM EMP WHERE SAL < ANY (SELECT SAL FROM EMP WHERE DEPTNO = 20);
SELECT * FROM EMP WHERE SAL < SOME (SELECT SAL FROM EMP WHERE DEPTNO = 20);
--������ ���������� ���� = ��� ����
SELECT * FROM EMP WHERE SAL < (SELECT MAX(SAL) FROM EMP WHERE DEPTNO = 20);
--ũ�ٴ� (>) ���� = OR ���� ���� ��
--�ּҰ����� ū �޿� ���� ����
SELECT * FROM EMP WHERE SAL > ANY (SELECT SAL FROM EMP WHERE DEPTNO = 20);
SELECT * FROM EMP WHERE SAL > SOME (SELECT SAL FROM EMP WHERE DEPTNO = 20);
--������ ���������� ���� = ��� ����
SELECT * FROM EMP WHERE SAL > (SELECT MIN(SAL) FROM EMP WHERE DEPTNO = 20);
--ALL = ���� ��� �߿��� ��� �����ؾ� TRUE
-- = ���� => ���ٴ� AND ���� ���� �� �̹Ƿ� ��� �Ұ�, ��) �� ����� �ϳ��� �޿��� ������ ����
--�μ����� �ִ� �޿� 3�� ���� �� ����� �޿��� ��� ���ٴ� ������ ������ �� ����
--�۴ٴ� (<) ���� = AND ���� ���� ��
--950 < 1250 < 1500 < 1600 < 2850
--�ּҰ����� ���� �޿� ���� ����
SELECT SAL FROM EMP WHERE DEPTNO = 30;
SELECT * FROM EMP WHERE SAL < ALL (SELECT SAL FROM EMP WHERE DEPTNO = 30);
--������ ���������� ���� = ��� ����
SELECT * FROM EMP WHERE SAL < (SELECT MIN(SAL) FROM EMP WHERE DEPTNO = 30);
--ũ�ٴ� (>) ���� = AND ���� ���� ��
--�ִ밪���� ū �޿� ���� ����
SELECT * FROM EMP WHERE SAL > ALL (SELECT SAL FROM EMP WHERE DEPTNO = 30);
--������ ���������� ���� = ��� ����
SELECT * FROM EMP WHERE SAL > (SELECT MAX(SAL) FROM EMP WHERE DEPTNO = 30);
--