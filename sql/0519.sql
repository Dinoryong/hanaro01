--�Լ�
--�����Լ�
--���ڿ� ���� �Լ�
--�빮��, �ҹ���, ù���ڸ� �빮�� ������ �ҹ��ڷ� ����
SELECT ENAME, UPPER(ENAME), LOWER(ENAME), INITCAP(ENAME) FROM EMP;
--����
SELECT * FROM EMP WHERE ENAME = 'SCOTT';
SELECT * FROM EMP WHERE UPPER(ENAME) = 'SCOTT';
SELECT * FROM EMP WHERE LOWER(ENAME) = 'scott';
SELECT * FROM EMP WHERE LOWER(ENAME) LIKE 's%';
--���ڿ� ����
SELECT ENAME, LENGTH(ENAME) FROM EMP;
SELECT ENAME, LENGTH(ENAME) FROM EMP WHERE LENGTH(ENAME) >= 5;
SELECT ENAME, LENGTH(ENAME) FROM EMP WHERE LENGTH(ENAME) < 5;
--���ڿ� ����Ʈ
--DUAL: ������ ���� SYS ���� ���̺�, �Լ� ����̳� ���� �� �׽�Ʈ �������� ����ϴ� ���� ���̺�
SELECT LENGTH('HELLO'), LENGTHB('HELLO') FROM DUAL;
SELECT LENGTH('�ȳ�'), LENGTHB('�ȳ�') FROM DUAL;
--���ڿ� �Ϻ� ����
--ù ��° ����: ���� ��ġ, �� ��° ����: ���� �� (�����ϸ� ������)
SELECT JOB, SUBSTR(JOB, 1, 2) FROM EMP; -- 2����
SELECT JOB, SUBSTR(JOB, 3, 5) FROM EMP; -- 5����
SELECT JOB, SUBSTR(JOB, 3) FROM EMP; -- ������ġ���� ������
--����, ���ڼ��� �����ϱ� ����� �� LENGTH()
--LENGTH('CLERK') : 1 ~ 5
SELECT JOB, LENGTH(JOB) FROM EMP;
--ó������ ������
---LENGTH('CLERK') : -5 ~ -1
SELECT JOB, SUBSTR(JOB, -LENGTH(JOB)) FROM EMP;
SELECT JOB, SUBSTR(JOB, -LENGTH(JOB), 2) FROM EMP;
--�ڿ��� ã�� ���� ��
SELECT JOB, SUBSTR(JOB, LENGTH(JOB)) FROM EMP; -- �ڿ������� 1����
SELECT JOB, SUBSTR(JOB, LENGTH(JOB)-1) FROM EMP; -- �ڿ������� 2����
SELECT JOB, SUBSTR(JOB, LENGTH(JOB)-2) FROM EMP; -- �ڿ������� 3����
SELECT JOB, SUBSTR(JOB, LENGTH(JOB)-3) FROM EMP; -- �ڿ������� 4����
--Ư�� ���� ��ġ
SELECT INSTR('HELLO, ORACLE!','L'), -- L ���ڰ� ó�� ��Ÿ���� ��ġ
       INSTR('HELLO, ORACLE!','L',5), -- 5��°���� L ���ڰ� ó�� ��Ÿ���� ��ġ
       INSTR('HELLO, ORACLE!','L',2,2) -- 2��°���� L ���ڰ� �ι�° ��Ÿ���� ��ġ
    FROM DUAL;
--�ٸ� ���ڷ� ��ü
SELECT '010-1234-5678',
       REPLACE('010-1234-5678', '-', ' '), -- ���(-) ��ȣ�� BLANK �� ��ü
       REPLACE('010-1234-5678', '-', '*'), -- ���(-) ��ȣ�� * �� ��ü
       REPLACE('010-1234-5678', '-') -- ���(-) ��ȣ�� ''�� ��ü = ����
    FROM DUAL;
--��ĭ�� Ư�� ���ڷ� ä���
--LPAD: LEFT ���� ä��
--RPAD: RIGHT ���� ä��
SELECT 'Oracle',
       LPAD('Oracle', 10, '#'), -- 10�ڸ�, Oracle ���ڸ� �����ʺ��� �ְ�, �����ڸ��� ���ʿ��� # ä��
       RPAD('Oracle', 10, '*'), -- 10�ڸ�, Oracle ���ڸ� ���ʺ��� �ְ�, �����ڸ��� �����ʿ��� # ä��
       LPAD('Oracle', 10), -- 10�ڸ�, Oracle ���ڸ� �����ʺ��� �ְ�, �����ڸ��� ���ʿ��� BLANK ä��
       RPAD('Oracle', 10) -- 10�ڸ�, Oracle ���ڸ� ���ʺ��� �ְ�, �����ڸ��� �����ʿ��� BLANK ä��
    FROM DUAL;
--���ڿ� ��ġ�� CONCAT
SELECT EMPNO, ENAME FROM EMP WHERE ENAME = 'SCOTT';
SELECT CONCAT(EMPNO, ENAME) FROM EMP WHERE ENAME = 'SCOTT';
SELECT CONCAT(':',ENAME), CONCAT(EMPNO, CONCAT(':',ENAME)) FROM EMP WHERE ENAME = 'SCOTT';
--|| �� ��ȯ
SELECT EMPNO || ENAME FROM EMP WHERE ENAME = 'SCOTT';
SELECT ':' || ENAME, EMPNO || ':' || ENAME FROM EMP WHERE ENAME = 'SCOTT';
--Ư�� ���ڸ� ����� �Լ�
--TRIM = �յ� = TRIM BOTH FROM
--LTRIM = �� = ���� = TRIM LEADING FROM
--RTRIM = �� = ������ = TRIM TRAILING FROM
--� ���ڸ� ������ ������ ������ ���� ����
SELECT '['||' _ _Oracle_ _ '||']',
       '['||TRIM(' _ _Oracle_ _ ')||']', -- = TRIM => [_ _Oracle_ _]
       '['||TRIM(BOTH FROM ' _ _Oracle_ _ ')||']', -- = TRIM => [_ _Oracle_ _]
       '['||TRIM(LEADING FROM ' _ _Oracle_ _ ')||']', -- = LTRIM => [_ _Oracle_ _ ]
       '['||TRIM(TRAILING FROM ' _ _Oracle_ _ ')||']' -- = RTRIM => [ _ _Oracle_ _]
    FROM DUAL;
--TRIM, LTRIM, RTRIM �Լ��� �ٲ㼭 �״�� ����
SELECT '['||' _ _Oracle_ _ '||']',
       '['||TRIM(' _ _Oracle_ _ ')||']', -- = TRIM => [_ _Oracle_ _]
       '['||LTRIM(' _ _Oracle_ _ ')||']', -- = LTRIM => [_ _Oracle_ _ ]
       '['||RTRIM(' _ _Oracle_ _ ')||']' -- = RTRIM => [ _ _Oracle_ _]
    FROM DUAL;
--����� ���� ���� �����ؼ� ���
SELECT '['||'_ _Oracle_ _'||']',
       '['||TRIM('_ _Oracle_ _')||']', -- = TRIM => [_ _Oracle_ _]
       '['||TRIM(BOTH '_' FROM '_ _Oracle_ _')||']', -- = TRIM => [ _Oracle_ ]
       '['||TRIM(LEADING '_' FROM '_ _Oracle_ _')||']', -- = LTRIM => [ _Oracle_ _ ]
       '['||TRIM(TRAILING '_' FROM '_ _Oracle_ _')||']' -- = RTRIM => [ _ _Oracle_ ]
    FROM DUAL;
--TRIM, LTRIM, RTRIM �Լ��� �ٲ㼭 �״�� ����
SELECT '['||'_ _Oracle_ _'||']',
       '['||TRIM('_ _Oracle_ _')||']', -- = TRIM => [_ _Oracle_ _]
       '['||LTRIM('_ _Oracle_ _', '_')||']', -- = LTRIM => [ _Oracle_ _ ]
       '['||RTRIM('_ _Oracle_ _', '_')||']' -- = RTRIM => [ _ _Oracle_ ]
    FROM DUAL;
--
--�����Լ�
--�ݿø�, �Ҽ��� ���Ͽ��� ǥ���� �ڸ���
SELECT ROUND(1234.5678),
       ROUND(1234.5678, 0),
       ROUND(1234.5678, 1),
       ROUND(1234.5678, 2),
       ROUND(1234.5678, -1),
       ROUND(1234.5678, -2)
    FROM DUAL;
--������
SELECT TRUNC(1234.5678),
       TRUNC(1234.5678, 0),
       TRUNC(1234.5678, 1),
       TRUNC(1234.5678, 2),
       TRUNC(1234.5678, -1),
       TRUNC(1234.5678, -2)
    FROM DUAL;
--���� ��ȯ �Լ�
--CEIL = õ�� = ���� ������, 3 < 3.14 < 4
--FLOOR = �ٴ� = ���� ������, 3 < 3.14 < 4
--CEIL = õ�� = ���� ������, -4 < -3.14 < -3
--FLOOR = �ٴ� = ���� ������, -4 < -3.14 < -3
SELECT CEIL(3.14),
       FLOOR(3.14),
       CEIL(-3.14),
       FLOOR(-3.14)
    FROM DUAL;
--������
SELECT MOD(15, 6), --15/6 = �� 2 ������ 3
       MOD(10, 2), --10/2 = �� 5 ������ 0
       MOD(11, 2) --11/2 = �� 5 ������ 1
    FROM DUAL;
--��¥�Լ�
--���� ��¥
SELECT SYSDATE FROM DUAL;
SELECT SYSDATE - 1 FROM DUAL;
SELECT SYSDATE + 1 FROM DUAL;
SELECT SYSDATE + 100 FROM DUAL;
--Ư�� ���� ���� ��¥
SELECT SYSDATE, ADD_MONTHS(SYSDATE, 3) FROM DUAL;
SELECT SYSDATE, ADD_MONTHS(SYSDATE, 120) FROM DUAL;
--�Ի� 10�ֳ�
SELECT ENAME, HIREDATE, ADD_MONTHS(HIREDATE, 120) FROM EMP;
--���� ��¥ ���� ��
--�̷���¥ ū ��
--������ ���ú��� ū ��
--�Ի� 41�ֳ� �̸� = �Ի��� 41�ֳ� > ���糯¥ = �̷���¥ > ���糯¥
SELECT ENAME, HIREDATE, ADD_MONTHS(HIREDATE, 492), SYSDATE 
    FROM EMP 
   WHERE ADD_MONTHS(HIREDATE, 492) > SYSDATE;
--�Ի� 41�ֳ� �ʰ� = �Ի��� 41�ֳ� < ���糯¥ = ���ų�¥ < ���糯¥
SELECT ENAME, HIREDATE, ADD_MONTHS(HIREDATE, 492), SYSDATE 
    FROM EMP 
   WHERE ADD_MONTHS(HIREDATE, 492) < SYSDATE;
--������ ����
SELECT EMPNO, ENAME, HIREDATE, SYSDATE,
       MONTHS_BETWEEN(HIREDATE, SYSDATE), --���ų�¥ - ���糯¥ = ������ - ū�� = ����(�츮�� ���ϴ� ��� �ƴ�)
       MONTHS_BETWEEN(SYSDATE, HIREDATE), --���糯¥ - ���ų�¥ = ū�� - ������ = ���(�츮�� ���ϴ� ���)
       TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE)) -- �Ҽ��� ù°�ڸ� ���� ���� = ���� ����
    FROM EMP;
--���ƿ��� ������ ��¥
--�ش� ���� ������ ��¥
SELECT SYSDATE, NEXT_DAY(SYSDATE, '������'), LAST_DAY(SYSDATE) FROM DUAL;
--��¥ �ݿø� = �߾Ӱ��� ã�ƶ�
SELECT SYSDATE,
       ROUND(SYSDATE, 'CC'), --����(100��)�� �߾Ӱ� 51�� �̻� �ݿø� 2001
       ROUND(SYSDATE, 'YYYY'), --����(1��)�� �߾Ӱ� 7�� 1�Ϻ��� �ݿø� 23-01-01
       ROUND(SYSDATE, 'Q'), --�б�(3����)�� �߾Ӱ��� �߾ӿ� �ִ� ���� 16�Ϻ��� 23-07-01
       ROUND(SYSDATE, 'DDD'), --��(�Ϸ�)�� �߾Ӱ��� 12�ú��� 23-05-20
       ROUND(SYSDATE, 'HH') --�ð�(60��)�� �߾Ӱ��� 31�к��� 23-05-19
    FROM DUAL;
--��¥ ������
SELECT SYSDATE,
       TRUNC(SYSDATE, 'CC'),
       TRUNC(SYSDATE, 'YYYY'),
       TRUNC(SYSDATE, 'Q'),
       TRUNC(SYSDATE, 'DDD'),
       TRUNC(SYSDATE, 'HH')
    FROM DUAL;
--�� ��ȯ �Լ�
--�Ͻ��� �� ��ȯ = ���� => ���ڷ� �ڵ����� �ٲ���
SELECT EMPNO, EMPNO + '1000' FROM EMP;
--1,000 �� ���� = ���� ��ȯ �Ұ� = ���� �߻�
SELECT EMPNO, EMPNO + '1,000' FROM EMP;
--����� �� ��ȯ
--���� �� ��ȯ
--��¥�� ���ڷ� ��ȯ
SELECT SYSDATE FROM EMP;
--��¥ �ð� ���� �Է��ؾ� ��
--�������� / �� ����
--�ú��ʴ� : ���� ����
SELECT SYSDATE, TO_CHAR(SYSDATE, 'YYYY/MM/DD HH24:MI:SS') FROM EMP;
--�� �� ����
SELECT SYSDATE,
       TO_CHAR(SYSDATE, 'MM'), --���� ��
       TO_CHAR(SYSDATE, 'MON'), --�̸� ��, ����
       TO_CHAR(SYSDATE, 'MONTH'), --�̸� ��, FULL NAME
       TO_CHAR(SYSDATE, 'DD'), -- ���� ��
       TO_CHAR(SYSDATE, 'DY'), -- �̸� ����, ����
       TO_CHAR(SYSDATE, 'DAY') -- �̸� ����, FULL NAME
    FROM DUAL;
--
SELECT SYSDATE,
       TO_CHAR(SYSDATE, 'MM'),
       TO_CHAR(SYSDATE, 'MON', 'NLS_DATE_LANGUAGE = KOREAN'),
       TO_CHAR(SYSDATE, 'MON', 'NLS_DATE_LANGUAGE = JAPANESE'),
       TO_CHAR(SYSDATE, 'MON', 'NLS_DATE_LANGUAGE = ENGLISH'),
       TO_CHAR(SYSDATE, 'MONTH', 'NLS_DATE_LANGUAGE = KOREAN'),
       TO_CHAR(SYSDATE, 'MONTH', 'NLS_DATE_LANGUAGE = JAPANESE'),
       TO_CHAR(SYSDATE, 'MONTH', 'NLS_DATE_LANGUAGE = ENGLISH')
    FROM DUAL;
SELECT SYSDATE,
       TO_CHAR(SYSDATE, 'DD'),
       TO_CHAR(SYSDATE, 'DY', 'NLS_DATE_LANGUAGE = KOREAN'),
       TO_CHAR(SYSDATE, 'DY', 'NLS_DATE_LANGUAGE = JAPANESE'),
       TO_CHAR(SYSDATE, 'DY', 'NLS_DATE_LANGUAGE = ENGLISH'),
       TO_CHAR(SYSDATE, 'DAY', 'NLS_DATE_LANGUAGE = KOREAN'),
       TO_CHAR(SYSDATE, 'DAY', 'NLS_DATE_LANGUAGE = JAPANESE'),
       TO_CHAR(SYSDATE, 'DAY', 'NLS_DATE_LANGUAGE = ENGLISH')
    FROM DUAL;
--�ú���
SELECT SYSDATE, TO_CHAR(SYSDATE, 'HH24:MI:SS'), --24�ð�
                TO_CHAR(SYSDATE, 'HH12:MI:SS'), --12�ð�
                TO_CHAR(SYSDATE, 'HH12:MI:SS PM'), --12�ð�, ����/����
                TO_CHAR(SYSDATE, 'HH:MI:SS PM') --12�ð�, ����/����
    FROM DUAL;
--���� ����
--���ڸ� ���ڷ� ��ȯ
SELECT SAL, --���� ����
       TO_CHAR(SAL, '$999,999'), --$ & õ���� , ����
       TO_CHAR(SAL, 'L999,999'), --LOCAL ��ȭ�� = �ѱ� �� & õ���� , ����
       TO_CHAR(SAL, '999,999.00'), --�Ҽ��� ���ڸ� & ���ڷθ� ǥ��
       --�� 11�ڸ� = ���� 9�ڸ��� & �Ҽ��� ���ڸ�, & õ���� , ����, ���� ä��� ���� �ڸ��� 0���� ä��
       TO_CHAR(SAL, '000,999,999.00'), 
       TO_CHAR(SAL, '000999999.99'), --�� 11�ڸ� = ���� 9�ڸ��� & �Ҽ��� ���ڸ�
       TO_CHAR(SAL, '999,999,00')
    FROM EMP;
--���� �� ��ȯ
--�Ͻ��� �� ��ȯ = ���ڸ� ���ڷ� ��ȯ = TO_NUMBER �Լ� ������� ����
SELECT 1300 - '1500', '1300' + 1500 FROM DUAL;
--����� �� ��ȯ
SELECT 1300 - TO_NUMBER('1500'), TO_NUMBER('1300') + 1500 FROM DUAL;
--TO_NUMBER �Լ��� ����Ͽ� ���� �ذ�
SELECT '1,300' - '1,500' FROM DUAL;
SELECT TO_NUMBER('1,300', '999,999') - TO_NUMBER('1,500', '999,999') FROM DUAL;
--��¥ �� ��ȯ
SELECT TO_DATE('2023-05-19', 'YYYY/MM/DD') FROM DUAL;
SELECT TO_DATE('20230519', 'YYYY/MM/DD') FROM DUAL;
SELECT TO_DATE('2023-05-19', 'YYYY-MM-DD') FROM DUAL;
SELECT TO_DATE('20230519', 'YYYY-MM-DD') FROM DUAL;
SELECT TO_DATE('2023/05/19', 'YYYY-MM-DD') FROM DUAL;
SELECT TO_DATE('2023/05/19', 'YYYY/MM/DD') FROM DUAL;
--��� �����Ϳ��� 81�� 7�� 1�� ���Ŀ� �Ի��� ���
SELECT * FROM EMP WHERE HIREDATE > TO_DATE('1981-07-01', 'YYYY-MM-DD');
--��� �����Ϳ��� 81�� 7�� 1�� ������ �Ի��� ���
SELECT * FROM EMP WHERE HIREDATE < TO_DATE('1981-07-01', 'YYYY-MM-DD');
--RR: 1950~2049
SELECT TO_DATE('49/12/10', 'YY/MM/DD') AS Y1, --2049
       TO_DATE('49/12/10', 'RR/MM/DD') AS Y2, --2049
       TO_DATE('50/12/10', 'YY/MM/DD') AS Y3, --2050
       TO_DATE('50/12/10', 'RR/MM/DD') AS Y4, --1950
       TO_DATE('51/12/10', 'YY/MM/DD') AS Y5, --2051
       TO_DATE('51/12/10', 'RR/MM/DD') AS Y6 --1951
    FROM DUAL;
--�� ó�� �Լ�
--NVL �Լ�: �ΰ��� �� ���� ���ϴ� ������ ����, �������� �״��
SELECT EMPNO, ENAME, SAL, COMM, SAL+COMM, NVL(COMM, 0), SAL+NVL(COMM, 0) FROM EMP;
--NVL2 �Լ�
--ù��° �Ű�����-�ΰ��� �ƴ� �� ���� ���ϴ� ������ ����
--�ι�° �Ű�����-�ΰ��� �� ���� ���ϴ� ������ ����
SELECT EMPNO, ENAME, SAL, COMM, NVL2(COMM, 'O', 'X'), NVL2(COMM, SAL*12+COMM, SAL*12) FROM EMP;
--��Ȳ�� ���� �ٸ� ������ ��ȯ
--DECODE: ���ٴ� ���Ǹ� ����
SELECT DISTINCT JOB FROM EMP;
SELECT EMPNO, ENAME, JOB, SAL,
       DECODE(JOB,
              'MANAGER', SAL*1.1,
              'SALESMAN', SAL*1.05,
              'ANALYST', SAL,
              SAL*1.03) AS UPSAL
    FROM EMP;
--CASE: ���ٴ� ���� ���� ����
--���� DECODE ���� CASE ������ ����
SELECT EMPNO, ENAME, JOB, SAL,
       CASE JOB
        WHEN 'MANAGER' THEN SAL*1.1
        WHEN 'SALESMAN' THEN SAL*1.05
        WHEN 'ANALYST' THEN SAL
        ELSE SAL*1.03
       END AS UPSAL
    FROM EMP;
--���ٴ� ���� ���� ���
SELECT EMPNO, ENAME, COMM,
       CASE 
        WHEN COMM IS NULL THEN '�ش� ���� ����'
        WHEN COMM = 0 THEN '���� ����'
        WHEN COMM > 0 THEN '����: ' || COMM
       END AS COMM_CMT
    FROM EMP;
--������ �Լ� = ����� �ϳ� = �ϳ��� ������ ���
SELECT SAL FROM EMP;
SELECT SUM(SAL) FROM EMP;
--�� ���� ����Ϸ��� ������ ���� ������ ���ƾ� ��
SELECT ENAME, SUM(SAL) FROM EMP;
--NULL ���� �ڵ����� �����ϰ� ���
SELECT SUM(COMM) FROM EMP;
--���� ������ �����Ƿ� ���� ����� ����
SELECT SUM(DISTINCT SAL), --�ߺ� �����Ͽ� ��
       SUM(ALL SAL), --ALL ���� �ʾƵ� ��� ����
       SUM(SAL) --ALL ���� �ʾƵ� ��� ����
    FROM EMP;
--������ ���� ����ϸ� ��
SELECT SUM(SAL), SUM(COMM) FROM EMP;
--����
SELECT COUNT(*) FROM EMP;
SELECT COUNT(*) FROM EMP WHERE DEPTNO = 30;
SELECT COUNT(DISTINCT SAL), --�ߺ� �����Ͽ� ī���
       COUNT(ALL SAL), --ALL ���� �ʾƵ� ��� ����
       COUNT(SAL) --ALL ���� �ʾƵ� ��� ����
    FROM EMP;
--NULL ���� �ڵ����� �����ϰ� ���
SELECT COUNT(COMM) FROM EMP;
--���� ��� ������
SELECT COUNT(COMM) FROM EMP WHERE COMM IS NOT NULL;
--�ִ밪
SELECT MAX(SAL) FROM EMP;
SELECT MAX(SAL) FROM EMP WHERE DEPTNO = 30;
--���� �ֱٿ� (�ʰ�) �Ի��� �Ի���
SELECT MAX(HIREDATE) FROM EMP;
--�ּҰ�
SELECT MIN(SAL) FROM EMP;
SELECT MIN(SAL) FROM EMP WHERE DEPTNO = 30;
--���� ���� ���� (����) �Ի��� �Ի���
SELECT MIN(HIREDATE) FROM EMP;
--���
SELECT AVG(SAL) FROM EMP;
SELECT AVG(SAL) FROM EMP WHERE DEPTNO = 30;
--NULL ���� �ڵ����� �����ϰ� ���
SELECT AVG(COMM) FROM EMP;
SELECT AVG(COMM) FROM EMP WHERE DEPTNO = 30;
--
