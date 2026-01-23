from sensor.exception import sensorException
from sensor.logger import logging
import os
import sys
from sensor.utils import dump_csv_file_to_mongodb_collection 

# def test_exception():
#     try:
#         a=1/0
#     except Exception as e:
#         raise sensorException(e,sys)
    

if __name__=="__main__":
    # try:
    #     logging.info("error handle")
    #     test_exception()   
    # except Exception as e:
    #     print(e)
    file_path="D:/sensorlive/aps_failure_training_set1.csv"
    databse_name="ineuron"
    collection_name="sensor"
    dump_csv_file_to_mongodb_collection(file_path,databse_name,collection_name)
    