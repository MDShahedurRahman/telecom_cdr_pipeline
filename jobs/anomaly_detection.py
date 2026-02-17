from pyspark.sql.functions import col, when


def detect_anomalies(df, anomaly_path):

    anomaly_df = df.withColumn(
        when(col("duration_minutes") > 120, "LONG_CALL")
    )

    return anomaly_df
