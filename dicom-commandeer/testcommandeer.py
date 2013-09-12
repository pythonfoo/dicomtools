#!/usr/bin/env python 
#-*- coding: utf-8 -*-
""" Some Description to enter"""
__author__ = "oerb"
__copyright__ = "GPL 2013"
__license__ = "GPL" 


def print_data_command(filepath, instanceCreationDate=False, accessionNumber=False):
    """ Show dicom Data by given Parameter

    some commend foo
    @param filepath to dicom File
    @param instanceCreationDate 
    @param accessionNumber
    """
    import dicom
    plan = dicom.read_file(filepath)

    if instanceCreationDate:   
        print "InstanceCreationDate: " + plan.InstanceCreationDate
    if accessionNumber:
        print "AccesionNumber: " + plan.AccessionNumber


def edit_data_command(filepath, newfilepath="x", instanceCreationDate="", ):
    """ edit dicom Data by given Parameter

    some commend foo
    @param filepath to dicom File
    @param instanceCreationDate 
    """
    
    import dicom
    plan = dicom.read_file(filepath)
    if not instanceCreationDate == "":
        plan.InstanceCreationDate = instanceCreationDate
    if newfilepath == "x":
        plan.save_as(filepath)
    else:
        plan.save_as(newfilepath)

if __name__ == '__main__':
    import commandeer
    commandeer.cli()
