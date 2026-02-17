from pyspark.sql.functions import col, to_date


def clean_call_data(df, silver_path):

    cleaned_df = df.dropDuplicates() \
        .dropna()

    return cleaned_df
