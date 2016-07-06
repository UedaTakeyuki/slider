# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
#
import sys
import logging
import inspect
import traceback

logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename='/home/pi/LOG/slider.log',level=logging.DEBUG)

def msg_log(msg_str):
    print str(inspect.currentframe(1).f_lineno) + " " + msg_str
    logging.info(str(inspect.currentframe(1).f_lineno) + " " + msg_str)

def msg_err_log(msg_str):
    print str(inspect.currentframe(1).f_lineno) + " " + msg_str
    logging.error(str(inspect.currentframe(1).f_lineno) + " " + msg_str)

def inc_file_ioerror():
    global g_count_of_file_ioerrors
    g_count_of_file_ioerrors += 1
    if g_count_of_file_ioerrors == 3:
        subprocess.Popen(reboot, shell=True)

def dec_file_ioerror():
    global g_count_of_file_ioerrors
    if g_count_of_file_ioerrors > 0:
        g_count_of_file_ioerrors -= 1

def inc_network_ioerror():
    global g_count_of_network_ioerrors
    g_count_of_network_ioerrors += 1
    if g_count_of_network_ioerrors == 3:
        g_count_of_network_ioerrors = 0
        subprocess.Popen(network_restart, shell=True)

def dec_network_ioerror():
    global g_count_of_network_ioerrors
    if g_count_of_network_ioerrors > 0:
        g_count_of_network_ioerrors -= 1

def io_error_report():
  info=sys.exc_info()
  msg_err_log ("IOError:"+ traceback.format_exc(info[0]))
  msg_err_log (traceback.format_exc(info[1]))
  msg_err_log (traceback.format_exc(info[2]))
  #inc_file_ioerror()

def unknown_error_report():
  info=sys.exc_info()
  msg_err_log ("Unexpected error:"+ traceback.format_exc(info[0]))
  msg_err_log (traceback.format_exc(info[1]))
  msg_err_log (traceback.format_exc(info[2]))
