CREATE TABLE attendance (
    att_id      NUMBER PRIMARY KEY,
    emp_id      NUMBER REFERENCES employees(emp_id),
    work_days   NUMBER
);
