from src.logger import logging
import logger
import sys

def get_error_details(error_message,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in the python script name[{0}] and line no [{1}] the error[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error_message))
    return error_message
    


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_details(error_message,error_detail = error_detail)
        #Here we are overriding the error_message 

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
        try:
            a= 1/0
            print(a)
        except Exception as e:
            logging.info("before custom exception raise")
            raise CustomException(e,sys)
        


        