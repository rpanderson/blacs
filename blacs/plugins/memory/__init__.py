#####################################################################
#                                                                   #
# /plugins/memory/__init__.py                                       #
#                                                                   #
# Copyright 2013, Monash University                                 #
#                                                                   #
# This file is part of the program BLACS, in the labscript suite    #
# (see http://labscriptsuite.org), and is licensed under the        #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
import os
import logging
import gc
from blacs import BLACS_DIR
from labscript_utils import memprof

FILEPATH_COLUMN = 0
name = "Memory Profile"
module = "memory" # should be folder name
logger = logging.getLogger('BLACS.plugin.%s'%module)

class Plugin(object):
    def __init__(self,initial_settings):
        self.menu = None
        self.notifications = {}
        self.initial_settings = initial_settings
        self.BLACS = None
        
    def get_menu_class(self):
        return Menu
        
    def get_notification_classes(self):
        return []
        
    def get_setting_classes(self):
        return []
        
    def get_callbacks(self):
        {}
        
    def set_menu_instance(self,menu):
        self.menu = menu
        
    def set_notification_instances(self,notifications):
        pass
        
    def plugin_setup_complete(self, BLACS):
        self.BLACS = BLACS
        
    def get_save_data(self):
        return {}
    
    def close(self):
        pass

class Menu(object):
    def __init__(self,BLACS):
        self.BLACS = BLACS
        self.close_notification_func = None
        memprof.start(filepath=os.path.join(BLACS_DIR, 'memprof.txt'))        
        
    def get_menu_items(self):
        return {'name':name,        
                'menu_items':[{'name':'Garbage collect',
                               'action':gc.collect,
                               'icon': ':/qtutils/fugue/memory'
                              },
                              {'name':'Reset profiler',
                               'action':memprof.start,
                               'icon': ':/qtutils/fugue/counter-reset'
                              },
                              {'name':'Diff memory usage',
                               'action':memprof.check,
                               'icon': ':/qtutils/fugue/tables'
                              }
                             ]                                
               }
    
