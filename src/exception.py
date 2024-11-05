import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    
    def __init__(self, error_message, error_detail:sys):
        """
        :param error_message: error message in string format
        :param error_detail: object of sys module having exc_info() which carries the exception information
        :return: None
        :rtype: None
        This Init method initializes the exception by accepting the error message and error detail extracted
        from sys module. The error detail is then used to get the file name and line number of the error and
        a formatted error message is created to be raised as the exception.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        :return: The string representation of error
        :rtype: str
        This method returns the string representation of error message which is used to represent the
        CustomException class objects as string.
        """
        return self.error_message    