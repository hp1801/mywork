CREATE OR REPLACE TRIGGER trg_salary_audit
AFTER INSERT ON salary
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (
        action,
        emp_id,
        action_date
    )
    VALUES (
        'SALARY_GENERATED',
        :NEW.emp_id,
        SYSDATE
    );
END;
/
