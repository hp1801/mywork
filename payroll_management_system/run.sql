-- Run this file in Oracle SQL Developer 

-- 1. Create tables
@schema/employees.sql
@schema/attendance.sql
@schema/salary.sql
@schema/audit_log.sql

-- 2. Create sequence
CREATE SEQUENCE salary_seq START WITH 1 INCREMENT BY 1;

-- 3. Insert sample data
@sample_data/insert_employees.sql
@sample_data/insert_attendance.sql

-- 4. Create procedure & trigger
@procedures/calculate_payroll.sql
@triggers/salary_audit_trigger.sql

-- 5. Execute payroll
EXEC calculate_payroll('JAN-2025');

-- 6. Verify results
SELECT * FROM salary;
SELECT * FROM audit_log;
