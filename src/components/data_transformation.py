import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from src.components.data_ingestion import DataIngestion


from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info("Data Transformation Initiated")

            categorical_columns = ['ProtocolType', 'Service', 'Flag']
            numerical_columns = ['Duration', 'SourceBytes', 'DestinationBytes', 'Land', 'WrongFragment',
                                'Urgent', 'Hot', 'NumFailedLogins', 'LoggedIn', 'NumCompromised',
                                'RootShell', 'SuAttempted', 'NumRoot', 'NumFileCreations', 'NumShells',
                                'NumAccessFiles', 'NumOutboundCmds', 'IsHostLogin', 'IsGuestLogin',
                                'Count', 'SrvCount', 'SerrorRate', 'SrvSerrorRate', 'RerrorRate',
                                'SrvRerrorRate', 'SameSrvRate', 'DiffSrvRate', 'SrvDiffHostRate',
                                'DstHostCount', 'DstHostSrvCount', 'DstHostSameSrvRate',
                                'DstHostDiffSrvRate', 'DstHostSameSrcPortRate',
                                'DstHostSrvDiffHostRate', 'DstHostSerrorRate', 'DstHostSrvSerrorRate',
                                'DstHostRerrorRate', 'DstHostSrvRerrorRate']
            
            #Define custom ranking for data of each ordinal columns
            Protocol= ['tcp', 'udp', 'icmp']

            Services= ['ftp_data', 'other', 'private', 'http', 'remote_job', 'name',
                        'netbios_ns', 'eco_i', 'mtp', 'telnet', 'finger', 'domain_u',
                        'supdup', 'uucp_path', 'Z39_50', 'smtp', 'csnet_ns', 'uucp',
                        'netbios_dgm', 'urp_i', 'auth', 'domain', 'ftp', 'bgp', 'ldap',
                        'ecr_i', 'gopher', 'vmnet', 'systat', 'http_443', 'efs', 'whois',
                        'imap4', 'iso_tsap', 'echo', 'klogin', 'link', 'sunrpc', 'login',
                        'kshell', 'sql_net', 'time', 'hostnames', 'exec', 'ntp_u',
                        'discard', 'nntp', 'courier', 'ctf', 'ssh', 'daytime', 'shell',
                        'netstat', 'pop_3', 'nnsp', 'IRC', 'pop_2', 'printer', 'tim_i',
                        'pm_dump', 'red_i', 'netbios_ssn', 'rje', 'X11', 'urh_i',
                        'http_8001', 'aol', 'http_2784', 'tftp_u', 'harvest']

            Flag= ['SF', 'S0', 'REJ', 'RSTR', 'SH', 'RSTO', 'S1', 'RSTOS0', 'S3','S2', 'OTH']

            num_pipeline = Pipeline(
                steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder', OrdinalEncoder(categories=[Protocol,Services,Flag])),
                ('scaler', StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_columns),
                ('cat_pipeline', cat_pipeline, categorical_columns)
            ])

            return preprocessor


        except Exception as error:
            logging.info("Error Occured in Data Transformation")
            raise CustomException(error, sys)
        
    def initiate_data_transformation(self,train_path, test_path):
        try:
            logging.info("Data transformation initiated")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read the train and test data")
            logging.info(f"Train Dataframe head: \n{train_df.head().to_string()}")
            logging.info(f"Test Dataframe head: \n{test_df.head().to_string()}")

            logging.info("Getting processing object")

            preprocessor_obj = self.get_data_transformation_object()

            #target_column = 'AttackType'
            #drop_columns = [target_column]

            input_column_train_df = train_df.drop(columns=['AttackType','DifficultyLevel'])
            logging.info(f"Train Dataframe head: \n{input_column_train_df.head().to_string()}")
            target_column_train_df = train_df['AttackType']

            input_column_test_df = test_df.drop(columns=['AttackType','DifficultyLevel'])
            logging.info(f"Train Dataframe head: \n{input_column_test_df.head().to_string()}")
            logging.info(f"Train Dataframe datatype: \n{input_column_test_df.info()}")
            target_column_test_df = test_df['AttackType']

            input_column_train_arr = preprocessor_obj.fit_transform(input_column_train_df)
            input_column_test_arr = preprocessor_obj.transform(input_column_test_df)

            train_arr = np.c_[input_column_train_arr, np.array(target_column_train_df)]
            test_arr = np.c_[input_column_test_arr, np.array(target_column_test_df)]


            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )
            logging.info("Data transformation completed")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as error:
            logging.info("Exception occured at initiation of data transformation")
            raise CustomException(error, sys)



if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)