#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        Py_Folder_Sync
# Purpose:     Easy folder sync
# Version:     Version 1.0 (P3-20191101)
# Author:      CyberStack.org 
# Created:     2019/11/01
# Twitter:	   @CyberStackorg
#-------------------------------------------------------------------------------

'''To Do:
    * Create a GUI for selecting paths with default file/folder selcetion.
    * Integrate watchdog to check when thumbdrive is pluged in and sync data.
    * Save path config for re-use without re-entering path every time.
    * Extra advanced features'''

from dirsync import sync
import os

source_folder = 'source_path'    #e.g. D:\\'
sync_folder = 'destination_folder'      # e.g 'C:/Users/bob/Desktop/Sync_folder'

def main():

	os.system('cls')
	print("Syncing data please wait .......")

	# Set purge to True for removing files/forders in destinstion folder not in source.
	sync(source_folder, sync_folder, 'sync', purge = True) 
	print('-'*15)
	print('Done')
	print('-'*15)

if __name__ == '__main__':
	main() 