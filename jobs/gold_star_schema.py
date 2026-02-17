def build_star_schema(df, gold_path):

    dim_customer = df.select(
        "customer_id", "customer_name", "city", "country"
    ).distinct()

    dim_call_type = df.select(
        "call_type"
    ).distinct()

    return fact_calls
