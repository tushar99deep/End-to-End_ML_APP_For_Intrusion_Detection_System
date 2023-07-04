import os
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
import pandas as pd




## Intitialize the Data Ingetion Configuration

@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

## create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods Starts')
        try:
            cloud_config= {'secure_connect_bundle': 'secure-connect-network-project.zip'}
            auth_provider = PlainTextAuthProvider('vbThZfyFKuOrkzDwvhIeGrdk', 'oDe-9IZ3dJr54qKC3Mmk5MbZH,LWqQzZhJGeSEFubtzggh9U.BAIZ8HrSK2bvn5rczWDh-yI9CwU0P262ONJ2f0pYT,p7MW4u3aTuTt1+u9ZWII9HGU3_Odnp42_jDrq')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()

            session.set_keyspace('project')
            # Read table from Cassandra
            query = "SELECT * FROM data1"
            result = session.execute(query)

            # Extract column names from the result metadata
            columns = result.column_names
 
            # Create a pandas DataFrame from the result
            df = pd.DataFrame(result, columns=columns)
            
            
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
  
            
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)
