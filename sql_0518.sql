--�ּ� : CTRL + /
--���� : CTRL + ENTER
--�������
DESC EMP;
--�μ�����
DESC DEPT;
--�޿���� ����
DESC SALGRADE;
-- SQL �⺻ ����
-- ��ü �� : *
SELECT * FROM  EMP;
-- Ư�� �� : �� �̸�
SELECT ENAME FROM EMP;
-- Ư�� �� ������ : �� �̸�, �� �̸� ��ǥ�� ����
SELECT ENAME, EMPNO FROM EMP;
-- Ư�� ���� : WHERE ��
SELECT * FROM EMP WHERE SAL > 3000;
-- 