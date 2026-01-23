import os


TARGET_COLUME="class"
PIPELINE_NAME="sensor"
AERIFACT_DIR="artifact"
FILE_NAME="sensor.csv"
  
TRAIN_FILE_NAME:str="train.csv"
MODEL_FILE_NAME:str="model.pkl"

PREPROCESSING_OBJECT_FILE_NAME="preprocessing.pkl"
SCHEMA_FILE_PATH=os.path.join("config","schema.yaml")
SCHEMA_DROP_COLS="drop_columns"


"""
   data ingestion related constant values

"""
DATA_INGESTION_COLLECTION_NAME:str="sensor"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2
