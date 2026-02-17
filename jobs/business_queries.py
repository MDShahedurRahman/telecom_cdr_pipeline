from pyspark.sql.functions import sum, count, desc


def top_customers_by_call_cost(df):
    return df.groupBy("customer_name") \
        .agg(sum("call_cost").alias("total_spent")) \
        .orderBy(desc("total_spent"))
