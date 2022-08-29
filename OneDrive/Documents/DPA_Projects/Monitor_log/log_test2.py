import logging
import os, sys, time


#Set local path
initial_path = 'C:/Users/Bhavesh Sondagar/OneDrive/Documents/DPA_Projects/Monitor_log'
code_name = "log_error"
code_name1 = 'log_run'
log_folder_path =initial_path + "/Meta_Logs/"

if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path)

#set name of the file    
filePath = log_folder_path + code_name + time.strftime("_%Y%m%d")+".log"
filePath1 = log_folder_path + code_name1 + time.strftime("_%Y%m%d")+".log"

# set a LOG_FORMAT
LOG_FORMAT = ('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')

# Create a custom errorlog
errorlog = logging.getLogger(__name__)
log_formatter = logging.Formatter(LOG_FORMAT)

# Create handlers
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
errorlog.addHandler(stream_handler)

# Create a custom infolog
infolog = logging.getLogger('infolog')

# Create formatters and add it to handlers
file_handler_info = logging.FileHandler(filePath1, mode='a+')    
file_handler_info.setFormatter(log_formatter)
file_handler_info.setLevel(logging.INFO)

# Add handlers to the infolog
infolog.addHandler(file_handler_info)

# Create formatters and add it to handlers
file_handler_error = logging.FileHandler(filePath, mode='a+')
file_handler_error.setFormatter(log_formatter)

# set handlers to log error
file_handler_error.setLevel(logging.ERROR)

# Add handlers to the infolog
errorlog.addHandler(file_handler_error)

# set handlers to log info
infolog.setLevel(logging.INFO)


#defining function 1
"""Add Function"""
def add(x, y):
    try:
        result =  x + y
        infolog.info('Code run successfully - Add: {} + {} = {}'.format(num_1, num_2, result))
    except Exception as e:
        
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error_msg = str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno)
        #print(exc_type, fname, exc_tb.tb_lineno)
        #print(error_msg)
        errorlog.error(" add_result - " + str(error_msg))
            

"""Subtract Function"""
def subtract(x, y):
    try:    
        result =  x - y - 'bad_error'
        infolog.info('Code run successfully - Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error_msg = str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno)
        errorlog.error(" sub_result - " + str(error_msg))
        pass


"""Multiply Function"""
def multiply(x, y):
    try:
        result = x**y*z  
        return result
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error_msg = str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno)
        errorlog.error(" mul_result - " + str(error_msg))
        pass 
    
"""Divide Function"""
def divide(x, y):
    try:
        result = x / y
        infolog.info('Code run successfully - div: {} / {} = {}'.format(num_1, num_2, result))
        
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error_msg = str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno)
        errorlog.error(" divide_result - " + str(error_msg))
        pass

# Constant variable        
num_1 = 10
num_2 = 8

#call the functions
add_result = add(num_1, num_2)
sub_result = subtract(num_1, num_2)
mul_result = multiply(num_1, num_2)
div_result = divide(num_1,num_2)
