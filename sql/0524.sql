--��ü
--����Ŭ �����ͺ��̽� ���̺�
--1) ����� ���̺�
--2) ������ ����
--scott �������� ����
SELECT * FROM DICTIONARY;
SELECT * FROM DICT;
--SCOTT ������ �����ϰ� �ִ� ���̺�
SELECT * FROM USER_TABLES;
--��� ����ڰ� �����ϰ� �ִ� ���̺� 
SELECT * FROM ALL_TABLES;
--������ ������ �־�� �� �� �ִ� ����
SELECT * FROM DBA_TABLES;
--�и��� �����ϴµ��� �ұ��ϰ� SCOTT �������� ���� �������� �ʴ´ٰ� �ߴ� ����
--������ ���� : ���� ���θ� �˷����� �ʾƾ� ����
--���������� ������ ���ٰ� �˷��ָ� ���̺��� �����Ѵٴ� ������ �˷��ִ� ��
--������ �������� �����ؼ� �ٽ� Ȯ���ϱ�
SELECT * FROM DBA_TABLES;
--������ �������� ����� ���� Ȯ��
SELECT * FROM DBA_USERS WHERE USERNAME = 'SCOTT';
--SCOTT �������� ����� ���� Ȯ��
--�ε���
--DB�� �ִ� �����͸� �� ������ ã���� �����ִ� ��ü
--�ε����� ������ ��ü�� �� ã��
--�ε��� ���� Ȯ��
SELECT * FROM USER_INDEXES;
--�ε��� �� ���� Ȯ��
SELECT * FROM USER_IND_COLUMNS;
--�ε��� ����
CREATE INDEX IDX_EMP_SAL ON EMP(SAL);
--�ε��� �� ���� Ȯ��
SELECT * FROM USER_IND_COLUMNS;
--�ε��� ����
DROP INDEX IDX_EMP_SAL;
--�ε��� �����¾����� Ȯ��
SELECT * FROM USER_IND_COLUMNS;
--�� - ���̺�ó�� ����� �� �ִ� ��ü
--��� ���� : 1) ����  2) ���ȼ�
--�� ���� ������ �ʿ�
--������ �������� ���� �ο�
--��� ������Ʈ ������ �������� ����
sqlplus system/oracle
--���� �ο� = GRANT ���� TO ����
GRANT CREATE VIEW TO SCOTT;
--SCOTT �������� �����ϱ�
SELECT * FROM EMP WHERE DEPTNO = 10;
CREATE VIEW VW_EMP10
    AS (SELECT * FROM EMP WHERE DEPTNO = 10);
--�� ���� Ȯ��
SELECT * FROM USER_VIEWS;
--sqlplus ���� �ٽ� Ȯ��
--sqlplus scott/tiger
SELECT VIEW_NAME TEXT FROM USER_VIEWS;
--�츮�� ���� �� ���
--SELECT * FROM EMP WHERE DEPTNO = 10; => VM_EMP10 �� ��ü�Ͽ� ���
SELECT * FROM EMP WHERE DEPTNO = 10;
SELECT * FROM VM_EMP10;
--�� ����
DROP VIEW VM_EMP10;
--������ �Ǿ����� Ȯ��
SELECT * FROM VM_EMP10;
SELECT * FROM USER_VIEWS;
--ROWNUM = ���̺��� ���� �ƴ� ������ ��
SELECT ROWNUM, A.* FROM EMP A;
--�޿��� ���� ������ ����
SELECT ROWNUM, A.* FROM EMP A ORDER BY SAL DESC;
--�޿��� ���� ������ �����ؼ� ROWNUM ���̷��� �並 ����ؾ� ��
SELECT * FROM EMP ORDER BY SAL DESC;
--�ζ��κ�
SELECT ROWNUM, A.* FROM (SELECT * FROM EMP ORDER BY SAL DESC) A;
--WITH  ���� ��ȯ
WITH A AS (SELECT * FROM EMP ORDER BY SAL DESC)
    SELECT ROWNUM, A.* FROM A;
--�޿��� ���� ���� 5�� ����
--�ζ��κ�
SELECT ROWNUM, A.*
    FROM (SELECT * FROM EMP ORDER BY SAL DESC) A
    WHERE ROWNUM <= 5;
--WITH  ���� ��ȯ
WITH A AS (SELECT * FROM EMP ORDER BY SAL DESC)
    SELECT ROWNUM, A.* FROM A WHERE ROWNUM <= 5;
--
--������ = �Ϸù�ȣ �����ϴ� ��ü = ��Ģ�� ����
--DEPT ���̺��� �� ������ �����ؼ� ���̺� ����
DROP TABLE DEPT_COPY;
CREATE TABLE DEPT_COPY
    AS SELECT * FROM DEPT WHERE 1 != 1;
SELECT * FROM DEPT_COPY;
--������ ����
CREATE SEQUENCE SEQ_DEPT
    INCREMENT BY 10
    START WITH 0
    MAXVALUE 90
    MINVALUE 0
    NOCYCLE
    CACHE 2;
--������ Ȯ��
SELECT * FROM USER_SEQUENCES;
--������ �̿��ؼ� ������ �߰�
INSERT INTO DEPT_COPY (DEPTNO, DNAME, LOC)
    VALUES (SEQ_DEPT.NEXTVAL, 'DA', 'SEOUL');
SELECT * FROM DEPT_COPY;
--���������� �ѹ� �� �غ��� �̹� �ִ밪�� �����߱� ������ �߰� �Ұ�
INSERT INTO DEPT_COPY (DEPTNO, DNAME, LOC)
    VALUES (SEQ_DEPT.NEXTVAL, 'DA', 'SEOUL');
--������ ��� ���
SELECT SEQ_DEPT.CURRVAL FROM DUAL;
SELECT SEQ_DEPT.NEXTVAL FROM DUAL;
--������ ����
ALTER SEQUENCE SEQ_DEPT
    INCREMENT BY 3
    MAXVALUE 99
    CYCLE;
--������ �Է� ���� ���� Ȯ��
SELECT * FROM DEPT_COPY;
--3�� ���� = �ִ밪 99�� ����
INSERT INTO DEPT_COPY (DEPTNO, DNAME, LOC)
    VALUES (SEQ_DEPT.NEXTVAL, 'DA', 'SEOUL');
SELECT * FROM DEPT_COPY;
--3�� ���� = CYCLE ���� = �ִ밪�� �����ص� �ּҰ����� �ٽ� ���ư�
INSERT INTO DEPT_COPY (DEPTNO, DNAME, LOC)
    VALUES (SEQ_DEPT.NEXTVAL, 'DA', 'SEOUL');
SELECT * FROM DEPT_COPY;
--������ ����
DROP SEQUENCE SEQ_DEPT;
--������  ���� Ȯ��
SELECT * FROM USER_SEQUENCES;
--�ó�� = �������� ��Ī = ��ȸ���� �ƴ� = �ó�� ��ü �����ϱ� ������ ����ؼ� ��� ����
--SELECT �� �̸� AS ��Ī => ��ȸ�� ��Ī�� �ٸ�
--�ó�� ���� ������ �ʿ�
--������ �������� ���� �ο�
--��� ������Ʈ���� ����
SQLPLUS SYSTEM/ORACLE
--���� �ο� = GRANT ���� TO ����
GRANT CREATE SYNONYM TO SCOTT;
GRANT CREATE PUBLIC SYNONYM TO SCOTT;
--SCOTT �������� �����ϱ�
CREATE SYNONYM E FOR EMP;
--SYNONYM ���
--EMP ��ſ� E �� ���̺� �̸����� ��� ����
SELECT * FROM EMP;
SELECT * FROM E;
--SYNONYM ����
DROP SYNONYM E;
--������ �Ǿ����� Ȯ��
SELECT * FROM E;
--���� �̸� EMP �� ��� ����
SELECT * FROM EMP;
--���� ����
--1) NOT NULL = �� ������� ���� = �� �Ұ�
CREATE TABLE TABLE_NOTNULL(
    LOG_ID VARCHAR(15) NOT NULL,
    LOG_PW VARCHAR(15) NOT NULL,
    CP VARCHAR(15)
);
SELECT * FROM TABLE_NOTNULL;
DESC TABLE_NOTNULL;
--�ΰ� �߰� => �ΰ� �Ұ� ������������ ���� �߰� �Ұ�
INSERT INTO TABLE_NOTNULL (LOG_ID, LOG_PW, CP)
    VALUES ('TEST_ID_1', NULL, '010-1234-5678');
INSERT INTO TABLE_NOTNULL (LOG_ID, CP)
    VALUES ('TEST_ID_1', '010-1234-5678');
--��ȭ��ȣ�� NULL �� �߰� => ���������� ���� ������ �Է� ����
INSERT INTO TABLE_NOTNULL (LOG_ID, LOG_PW)
    VALUES ('TEST_ID_1', 'TEST_PW_1');
SELECT * FROM TABLE_NOTNULL;
--�ΰ����� ���� => �ΰ� �Ұ� ������������ ���� ���� �Ұ�
UPDATE TABLE_NOTNULL
    SET LOG_PW = NULL
    WHERE LOG_ID = 'TEST_ID_1';
--���� ���� Ȯ�� (�����ͻ���)
--P = PRIMARY KEY
--R = REFERENCE ����Ű
--C = CHECK / NOT NULL
--U = UNIQUE 
SELECT * FROM USER_CONSTRAINTS;
--�������� �̸� ����
CREATE TABLE TABLE_NOTNULL1(
    LOG_ID VARCHAR(15) CONSTRAINT TBNN1_LOGID_NN NOT NULL,
    LOG_PW VARCHAR(15) CONSTRAINT TBNN1_LOGPW_NN NOT NULL,
    CP VARCHAR(15)
);
--���� ���� Ȯ��
SELECT * FROM USER_CONSTRAINTS;
--���� ���� ����(�߰�) => �̹� �ΰ��� �ֱ� ������ ���� �ȵ�
ALTER TABLE TABLE_NOTNULL
    MODIFY (CP NOT NULL);
--��ȭ ��ȣ NULL ���� �ٸ� ������ ����
SELECT * FROM TABLE_NOTNULL;
UPDATE TABLE_NOTNULL
    SET CP = '010-1234-5678'
    WHERE LOG_ID = 'TEST_ID_1';
SELECT * FROM TABLE_NOTNULL;
--���� ���� ����(�߰�) => NULL ���� ���� ������ ���� ����
ALTER TABLE TABLE_NOTNULL
    MODIFY (CP NOT NULL);
--Ȥ�� TABLE_NOTNULL1 ���̺� ��ȭ��ȣ ���������� ������� ��쿡�� ����� �ǽ�
SELECT * FROM USER_CONSTRAINTS;
ALTER TABLE TABLE_NOTNULL1 DROP CONSTRAINT SYS_C0011083;
ALTER TABLE TABLE_NOTNULL1 DROP CONSTRAINT SYS_C0011084;
--���� ���� ����(�߰�)
ALTER TABLE TABLE_NOTNULL1
    MODIFY (CP CONSTRAINT TBNN1_CP_NN NOT NULL);
--���� ���� Ȯ��
SELECT * FROM USER_CONSTRAINTS;
DESC TABLE_NOTNULL;
DESC TABLE_NOTNULL1;
--���� ���� �̸� ����
ALTER TABLE TABLE_NOTNULL1
    RENAME CONSTRAINT TBNNI_CP_NN TO TBNN1_CP_NN_AFTER;
--���� ���� Ȯ��
SELECT * FROM USER_CONSTRAINTS;
--���� ���� ���� 
ALTER TABLE TABLE_NOTNULL1
    DROP CONSTRAINT TBNN1_CP_NN_AFTER;
--���� ���� ����
SELECT * FROM USER_CONSTRAINTS;

--UNIQUE = �ߺ��Ұ�
CREATE TABLE TB_UNQ (
    LOG_ID VARCHAR(15) CONSTRAINT TBUNQ_LOGID_UNQ UNIQUE;
    LOG_ID VARCHAR(15) CONSTRAINT TBUNQ_LOGID_UNQ UNIQUE;    
    CP     VARCHAR(15)
);
--���� ���� Ȯ��
SELECT * FROM USER_CONSTRAINTS WHERE CONSTRAINT_NAME LIKE 'TBUNQ';
--������ �߰�
INSERT INTO TB_UNQ (LOG_ID, LOG_PW, CP)
    VALUES ('TEST_ID_1', 'TEST_PW_1', '010-1234-5678');
--�ѹ� �� ���� => ID�� PW�� �ߺ� �Ұ���� ������������ ���� �߰� �Ұ�
INSERT INTO TB_UNQ (LOG_ID, LOG_PW, CP)
    VALUES ('TEST_ID_1', 'TEST_PW_1', '010-1234-5678');
--��ȭ��ȣ�� ���������� ���� ������ �ߺ� �Է� ����
INSERT INTO TB_UNQ (LOG_ID, LOG_PW, CP)


--NULL �� �߰� => UNIQUE�� �ߺ� �Ұ����� NULL �� �Ұ��� �ƴ� = NULL �� �Է� ����
INSERT INTO TB_UNQ (LOG_ID, LOG_PW, CP)
    VALUES (NULL, 'TEST_PW_3', '010-1234-5678');
SELECT * FROM TB_UNQ;
--NULL ���� �ߺ� ��� �ƴ� & UNIQUE �� �ߺ� �Ұ����� NULL �� �Ұ� �ƴ� = NULL �� �Է� ����
INSERT INTO TB_UNQ (LOG_PW, CP)
    VALUES (NULL, 'TEST_PW_4', '010-1234-5678');
SELECT * FROM TB_UNQ;
--������ ���� => �ߺ� �Ұ� ���� �������� ���� �ߺ� ������ ���� �Ұ�
UPDATE TB_UNQ
    SET LOG_ID = 'TEST_ID_1'
    WHERE LOG_PW = 'TEST_PW_3';
--�ߺ� �Ұ� ���� ������ �ֱ� ������ �ߺ� �����Ͱ� �ƴ� ������ ����
UPDATE TB_UNQ
    SET LOG_ID = 'TEST_ID_3'
    WHERE LOG_PW = 'TEST_PW_3';
SELECT * FROM TB_UNQ;
--�⺻Ű = PRIMARY KEY = NOT NULL + UNIQUE
CREATE TABLE TB_PK(
    LOG_ID VARCHAR2(15) CONSTRAINT TBPK_LOGID_PK PRIMARY KEY,
    LOG_PW VARCHAR2(15) CONSTRAINT TBPK_LOGPW_NN NOT NULL,
    CP VARCHAR2(15)
);
--������ �߰�
INSERT INTO TB_PK (LOG_ID, LOG_PW, CP)
    VALUES ('TEST_ID_1', 'TEST_PW_1', '010-1234-5678');
SELECT * FROM TB_PK;
--�ѹ� �� ���� = �ߺ� ������ �Է� �ȵ� => ID�� PK = �ߺ� �Ұ� + NULL �� �Ұ�
INSERT INTO TB_PK (LOG_ID, LOG_PW, CP)
    VALUES ('TEST_ID_1', 'TEST_PW_1', '010-1234-5678');
--PW�� NULL �� �Ұ��̱� �빮�� �ߺ� �����ʹ� �Է� ����
INSERT INTO TB_PK (LOG_ID, LOG_PW, CP)
    VALUES ('TEST_ID_2', 'TEST_PW_1', '010-1234-5678');
SELECT * FROM TB_PK;
--NULL �� �߰� = NULL �� �Է� �ȵ� => ID�� FK = �ߺ� �Ұ� + NULL �� �Ұ�
INSERT INTO TB_PK (LOG_ID, LOG_PW, CP)
    VALUES (NULL, 'TEST_PW_1', '010-1234-5678');
--�ܷ�Ű = foreign key = ����Ű = �ٸ� ���̺��� �⺻Ű�� ����
--EMP, DEPT���̺��� ������ �ִ� �������� Ȯ��
SELECT * FROM USER_CONSTRAINTS WHERE TABLE_NAME IN ('EMP', 'DEPT');
--EMP �����̺� DEPT ���̺� ���� �μ� ��ȣ�� �Է�
SELECT * FROM EMP;
SELECT * FROM DEPT;
--������ �� �ִ� ���� ���� ������ �Է� �ȵ� = �μ� ���̺� 90�� �μ� �����Ͱ� ����
--�μ� ���̺� 90�� ������ ���� �Է��� ������ ��� ���� �Է��ؾ� ���������� �߰� ����
INSERT INTO EMP
    VALUES (9999, 'QUEEN', 'VICE', 7839, '2023-05-23', 5000, NULL, 90);
--���̺� ����
CREATE TABLE DEPT_FK (
    DEPTNO NUMBER(2) CONSTRAINT DEPTFK_DEPTNO_FK PRIMARY KEY,
    DNAME VARCHAR2(15)
);
CREATE TABLE EMP_FK(
    EMPNO NUMBER(4) CONSTRAINT EMPFK_EMPNO_PK PRIMARY KEY,
    ENAME VARCHAR2(10),
    DEPTNO NUMBER(2) CONSTRAINT EMPFK_DEPTNO_FK REFERENCES DEPT_FK(DEPTNO)
);
--��� �߰� => ������ �� �ִ� ���� ���� ������ �߰� �Ұ�
--������ �� �ִ� ���� ���� ������ �� = �μ� �߰�
INSERT INTO EMP_FK
    VALUES(9999, 'QUEEN', 10);
SELECT * FROM DEPT_FK;
--�μ� �߰�
INSERT INTO DEPT_FK
    VALUES (10, 'DA');
SELECT * FROM DEPT_FK;
--�ٽ� ��� �߰� = ������ �� �ִ� ���� �ֱ� ������ �߰� ����
INSERT INTO EMP_FK
    VALUES(9999, 'QUEEN', 10);
--�ܷ�Ű�� ���� �� ������ �Է� ����
--1) �ܷ�Ű ����
--2) ������ ������ �Է�(��, �μ� 10��)
--3) ������ �Է� ���� (��, ��� QUEEN)
--
--�μ� ����
SELECT * FROM DEPT_FK;
SELECT * FROM EMP_FK;
--10�� �μ��� �����ϰ� �ִ� ������ �ֱ� ������ ���� �Ұ�
--����� ���� ����
DELETE DEPT_FK WHERE DEPTNO = 10;
--��� ����
DELETE EMP_FK WHERE EMPNO = 9999;
SELECT * FROM EMP_FK;
--�ٽ� �μ� ���� => �� �̻� 10�� �μ���ȣ�� ������ �ִ� ����� ���� ������
DELETE DEPT_FK WHERE DEPTNO = 10;
SELECT * FROM DEPT_FK;
--�ܷ�Ű�� ���� �� ������ ���� ����
--1) �����ϰ� �ִ� ������ = 10�� �μ� ��ȣ�� �����ϰ� �ִ� ���� ������ ����
--2) �μ� ������ ����
--