import os
import sys

class HousingException(Exception):
    
    def __init__(self, error_msg:Exception,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg=HousingException.get_detailed_error_msg(error_msg=error_msg,
                                                                       error_detail=error_detail
                                                                        )


    @staticmethod
    def get_detailed_error_msg(error_msg:Exception,error_detail:sys)->str:
        """
        error_msg: Exception object
        error_detail: object of sys module
        """
        exec_tb = error_detail.exc_info()[2]
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_msg = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{error_msg}]
        """
        return error_msg

    def __str__(self):
        return self.error_msg


    def __repr__(self) -> str:
        return HousingException.__name__.str()
