from datetime import date

def apply_scd2(dim_table: list, customer_id: str, changed_att: dict, change_date: date):
    # find records with natural key and is_current and expire old records
    for row in dim_table:
        if row['customer_id'] == 'customer_id' and row['is_current'] == True:
            row['end_date'] = change_date
            row['is_current'] = False
            break
    
    new_key = max(row['customer_key'] for row in dim_table) + 1
    new_row = {
        'customer_key' = new_key,
        'customer_id' = customer_id,
        **changed_att,
        'effective_date' = change_date,
        NULL,
        'is_current' = True
    }

    dim_table.append(new_row)
    return dim_table