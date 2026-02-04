CREATE OR REPLACE PROCEDURE calculate_payroll (
    p_month IN VARCHAR2
)
IS
    CURSOR emp_cursor IS
        SELECT e.emp_id, e.base_salary, a.work_days
        FROM employees e
        JOIN attendance a ON e.emp_id = a.emp_id
        WHERE e.status = 'ACTIVE';

    v_salary NUMBER(10,2);
BEGIN
    FOR emp_rec IN emp_cursor LOOP
        BEGIN
            v_salary := (emp_rec.base_salary / 22) * emp_rec.work_days;

            INSERT INTO salary (
                sal_id,
                emp_id,
                month_year,
                total_salary,
                generated_on
            )
            VALUES (
                salary_seq.NEXTVAL,
                emp_rec.emp_id,
                p_month,
                v_salary,
                SYSDATE
            );

        EXCEPTION
            WHEN OTHERS THEN
                DBMS_OUTPUT.PUT_LINE(
                    'Error processing employee ID: ' || emp_rec.emp_id
                );
        END;
    END LOOP;

    COMMIT;
END;
/
