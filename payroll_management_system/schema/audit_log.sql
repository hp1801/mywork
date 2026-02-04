CREATE TABLE audit_log (
    log_id      NUMBER GENERATED ALWAYS AS IDENTITY,
    action      VARCHAR2(50),
    emp_id      NUMBER,
    action_date DATE
);
