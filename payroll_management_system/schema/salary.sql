CREATE TABLE salary (
    sal_id       NUMBER PRIMARY KEY,
    emp_id       NUMBER REFERENCES employees(emp_id),
    month_year   VARCHAR2(20),
    total_salary NUMBER(10,2),
    generated_on DATE
);
