import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled= preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                    Duration : int,
                    Count : int,
                    DestinationBytes : int,
                    DiffSrvRate : float,
                    DstHostCount : int,
                    DstHostDiffSrvRate : float,
                    DstHostRerrorRate : float,
                    DstHostSameSrcPortRate : float,
                    DstHostSameSrvRate : float,
                    DstHostSerrorRate : float,
                    DstHostSrvCount : int,
                    DstHostSrvDiffHostRate : float,
                    DstHostSrvRerrorRate : float,
                    DstHostSrvSerrorRate : float,
                    Flag : str,
                    Hot : int,
                    IsGuestLogin : int,
                    IsHostLogin : int,
                    Land : int,
                    LoggedIn : int,
                    NumAccessFiles : int,
                    NumCompromised : int,
                    NumFailedLogins : int,
                    NumFileCreations : int,
                    NumOutboundCmds : int,
                    NumRoot : int,
                    NumShells : int,
                    ProtocolType : str,
                    RerrorRate : float,
                    RootShell : int,
                    SameSrvRate : float,
                    SerrorRate : float,
                    Service : str,
                    SourceBytes : int,
                    SrvCount : int,
                    SrvDiffHostRate : float,
                    SrvRerrorRate : float,
                    SrvSerrorRate : float,
                    SuAttempted : int,
                    Urgent : int,
                    WrongFragment : int):
            
            self.Duration = Duration
            self.Count = Count
            self.DestinationBytes = DestinationBytes
            self.DiffSrvRate = DiffSrvRate
            self.DstHostCount = DstHostCount
            self.DstHostDiffSrvRate = DstHostDiffSrvRate
            self.DstHostRerrorRate = DstHostRerrorRate
            self.DstHostSameSrcPortRate = DstHostSameSrcPortRate
            self.DstHostSameSrvRate = DstHostSameSrvRate
            self.DstHostSerrorRate = DstHostSerrorRate
            self.DstHostSrvCount = DstHostSrvCount
            self.DstHostSrvDiffHostRate = DstHostSrvDiffHostRate
            self.DstHostSrvRerrorRate = DstHostSrvRerrorRate
            self.DstHostSrvSerrorRate = DstHostSrvSerrorRate
            self.Flag = Flag
            self.Hot = Hot
            self.IsGuestLogin = IsGuestLogin
            self.IsHostLogin = IsHostLogin
            self.Land = Land
            self.LoggedIn = LoggedIn
            self.NumAccessFiles = NumAccessFiles
            self.NumCompromised = NumCompromised
            self.NumFailedLogins = NumFailedLogins
            self.NumFileCreations = NumFileCreations
            self.NumOutboundCmds = NumOutboundCmds
            self.NumRoot = NumRoot
            self.NumShells = NumShells
            self.ProtocolType = ProtocolType
            self.RerrorRate = RerrorRate
            self.RootShell = RootShell
            self.SameSrvRate = SameSrvRate
            self.SerrorRate = SerrorRate
            self.Service = Service
            self.SourceBytes = SourceBytes
            self.SrvCount = SrvCount
            self.SrvDiffHostRate = SrvDiffHostRate
            self.SrvRerrorRate = SrvRerrorRate
            self.SrvSerrorRate = SrvSerrorRate
            self.SuAttempted = SuAttempted
            self.Urgent = Urgent
            self.WrongFragment = WrongFragment

        
        

                

        
                




    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Duration' : [self.Duration],
                'Count' : [self.Count],
                'DestinationBytes' : [self.DestinationBytes],
                'DiffSrvRate' : [self.DiffSrvRate],
                'DstHostCount' : [self.DstHostCount],
                'DstHostDiffSrvRate' : [self.DstHostDiffSrvRate],
                'DstHostRerrorRate' : [self.DstHostRerrorRate],
                'DstHostSameSrcPortRate' : [self.DstHostSameSrcPortRate],
                'DstHostSameSrvRate' : [self.DstHostSameSrvRate],
                'DstHostSerrorRate' : [self.DstHostSerrorRate],
                'DstHostSrvCount' : [self.DstHostSrvCount],
                'DstHostSrvDiffHostRate' : [self.DstHostSrvDiffHostRate],
                'DstHostSrvRerrorRate' : [self.DstHostSrvRerrorRate],
                'DstHostSrvSerrorRate' : [self.DstHostSrvSerrorRate],
                'Flag' : [self.Flag],
                'Hot' : [self.Hot],
                'IsGuestLogin' : [self.IsGuestLogin],
                'IsHostLogin' : [self.IsHostLogin],
                'Land' : [self.Land],
                'LoggedIn' : [self.LoggedIn],
                'NumAccessFiles' : [self.NumAccessFiles],
                'NumCompromised' : [self.NumCompromised],
                'NumFailedLogins' : [self.NumFailedLogins],
                'NumFileCreations' : [self.NumFileCreations],
                'NumOutboundCmds' : [self.NumOutboundCmds],
                'NumRoot' : [self.NumRoot],
                'NumShells' : [self.NumShells],
                'ProtocolType' : [self.ProtocolType],
                'RerrorRate' : [self.RerrorRate],
                'RootShell' : [self.RootShell],
                'SameSrvRate' : [self.SameSrvRate],
                'SerrorRate' : [self.SerrorRate],
                'Service' : [self.Service],
                'SourceBytes' : [self.SourceBytes],
                'SrvCount' : [self.SrvCount],
                'SrvDiffHostRate' : [self.SrvDiffHostRate],
                'SrvRerrorRate' : [self.SrvRerrorRate],
                'SrvSerrorRate' : [self.SrvSerrorRate],
                'SuAttempted' : [self.SuAttempted],
                'Urgent' : [self.Urgent],
                'WrongFragment' : [self.WrongFragment],
                                
                }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
