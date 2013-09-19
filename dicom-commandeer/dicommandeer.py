#!/usr/bin/env python 
#-*- coding: utf-8 -*-
""" 
dicommandeer is a small and simple Shelltool based on 
the python dicom Library

**************************************
    Copyright (C) <2013>  <Björn Leppin>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

**************************************

use the Parameter help for Help

Example:

./testcommandeer.py print_data pic/pic1.dcm --instanceCreationDate 

"""
__author__ = "oerb"
__copyright__ = "2013"
__license__ = "GPL v3" 


def show_command(filepath, instanceCreationDate=False, 
        accessionNumber=False, approvalStatus=False, 
        beamSequence=False, doseReferenceSequence=False, 
        fractionGroupSequence=False, instanceCreationTime=False,
        institutionName=False, institutionalDepartmentName=False,
        manufacturer=False, manufacturerModelName=False,
        modality=False, operatorsName=False,
        patientBirthDate=False, patientID=False,
        patientName=False, patientSetupSequence=False,
        patientSex=False,
        RTPlanDate=False, RTPlanGeometry=False,
        RTPlanLabel=False, RTPlanName=False,
        RTPlanTime=False,
        RefdRTPlanSequence=False, RefdStructureSetSequence=False,
        ReferencedRTPlanSequence=False, ReferencedStructureSetSequence=False,
        referringPhysicianName=False,
        SOPClassUID=False, SOPInstanceUID=False,
        seriesInstanceUID=False, seriesNumber=False,
        softwareVersions=False, stationName=False,
        studyDate=False, studyID=False,
        studyInstanceUID=False,
        studyTime=False):
    """ Show dicom Data by given Parameter

    Parameter   
    @param filepath to dicom File 
    @param accessionNumber
    @param approvalStatus
    @param beamSequence
    @param doseReferenceSequence
    @param fractionGroupSequence
    @param instanceCreation
    @param instanceCreationDate
    @param instanceCreationTime
    @param institutionName
    @param institutionalDepartmentName
    @param manufacturer
    @param manufacturerModelName
    @param modality
    @param operatorsName
    @param patientBirthDate
    @param patientID
    @param patientName
    @param patientSetupSequence
    @param patientSex
    @param RTPlanDate
    @param RTPlanGeometry
    @param RTPlanLabel
    @param RTPlanName
    @param RTPlanTime
    @param RefdRTPlanSequence
    @param RefdStructureSetSequence
    @param ReferencedRTPlanSequence
    @param ReferencedStructureSetSequence
    @param referringPhysicianName
    @param SOPClassUID
    @param SOPInstanceUID
    @param seriesInstanceUID
    @param seriesNumber
    @param softwareVersions
    @param stationName
    @param studyDate
    @param studyID
    @param studyInstanceUID
    @param studyTime
 
    """
    import dicom
    plan = dicom.read_file(filepath)

    if instanceCreationDate:   
        print "InstanceCreationDate: " + plan.InstanceCreationDate
    if accessionNumber:
        print "AccesionNumber: " + plan.AccessionNumber
    if approvalStatus:
        print "ApprovalStatus: " + plan.ApprovalStatus
    if beamSequence:
        print "BeamSequence: " + str(plan.BeamSequence)
    if doseReferenceSequence:
        print "DoseReferenceSequence: " + str(plan.DoseReferenceSequence)
    if fractionGroupSequence:
        print "FractionGroupSequence: " + str(plan.FractionGroupSequence)
    if instanceCreationTime:
        print "InstanceCreationTime: " + plan.InstanceCreationTime
    if institutionName:
        print "InstitutionName: " + plan.InstitutionName
    if manufacturer:
        print "Manufacturer: " + plan.Manufacturer
    if manufacturerModelName:
        print "ManufacturerModelName: " + plan.ManufacturerModelName
    if modality:
        print "Modality: " + plan.Modality
    if operatorsName:
        print "OperatorsName: " + plan.OperatorsName
    if patientBirthDate:
        print "PatientBirthDate: " + plan.PatientBirthDate
    if patientID:
        print "PatientID: " + plan.PatientID
    if patientName:
        print "PatientName: " + plan.PatientName
    if patientSetupSequence:
        print "PatientSetupSequence: " + str(plan.PatientSetupSequence)
    if patientSex:
        print "PatientSex: " + plan.PatientSex
    if RTPlanDate:
        print "RTPlanDate: " + plan.RTPlanDate
    if RTPlanGeometry:
        print "RTPlanGeometry: " + plan.RTPlanGeometry
    if RTPlanLabel:
        print "RTPlanLabel: " + plan.RTPlanLabel
    if RTPlanName:
        print "RTPlanName: " + plan.RTPlanName
    if RTPlanTime:
        print "RTPlanTime: " + plan.RTPlanTime
    if RefdRTPlanSequence:
        print " ---------------- RefdRTPlanSequence ----------------- "
        print str(plan.RefdRTPlanSequence)
    if RefdStructureSetSequence:
        print " --------------- RefdStructureSetSequence ---------------- "
        print str(plan.RefdStructureSetSequence)
    if ReferencedRTPlanSequence:
        print " ------------- Referenced RTPlanSequence -------------"
        print str(plan.ReferencedRTPlanSequence)
    if ReferencedStructureSetSequence:
        print " ------------- Referenced Structure Set Sequence ----------"
        print str(plan.ReferencedStructureSetSequence)
    if referringPhysicianName:
        print "ReferringPhysicianName: " + plan.ReferringPhysicianName
    if SOPClassUID:
        print "SOPClassUID: " + plan.SOPClassUID
    if SOPInstanceUID:
        print "SOPInstanceUID: " + plan.SOPInstanceUID
    if seriesInstanceUID:
        print "SeriesInstanceUID: " + plan.SeriesInstanceUID
    if seriesNumber:
        print "SeriesNumber: " + plan.SeriesNumber
    if softwareVersions:
        print "SoftwareVersions: " + plan.SoftwareVersions
    if stationName:
        print "StationName: " + plan.StationName
    if studyDate:
        print "StudyDate: " + plan.StudyDate
    if studyID:
        print "StudyID: " + plan.StudyID
    if studyInstanceUID:
        print "StudyInstanceUID: " + plan.StudyInstanceUID
    if studyTime:
        print "StudyTime: " + plan.StudyTime

def edit_command(filepath, infos=False, accessionNumber="", newfilepath="",  instanceCreationDate=""):
    """ edit dicom Data by given Parameter

    Parameter:
    @param filepath to dicom File ist allways needed EX: ./dicommandeer.py testfiles/rltplan.dcm 
    @param accessionNumber
    @param approvalStatus
    @param beamSequence
    @param doseReferenceSequence
    @param fractionGroupSequence
    @param instanceCreation
    @param instanceCreationDate
    @param instanceCreationTime
    @param institutionName
    @param institutionalDepartmentName
    @param manufacturer
    @param manufacturerModelName
    @param modality
    @param operatorsName
    @param patientBirthDate
    @param patientID
    @param patientName
    @param patientSetupSequence
    @param patientSex
    @param RTPlanDate
    @param RTPlanGeometry
    @param RTPlanLabel
    @param RTPlanName
    @param RTPlanTime
    @param RefdRTPlanSequence
    @param RefdStructureSetSequence
    @param ReferencedRTPlanSequence
    @param ReferencedStructureSetSequence
    @param referringPhysicianName
    @param SOPClassUID
    @param SOPInstanceUID
    @param seriesInstanceUID
    @param seriesNumber
    @param softwareVersions
    @param stationName
    @param studyDate
    @param studyID
    @param studyInstanceUID
    @param studyTime
    """
    
    import dicom
    import re
    plan = dicom.read_file(filepath)
    """
    if infos:
        for parameter in dir(plan):
            if parameter[0].isupper():
                if not parameter.find("Sequence") == -1:
                    print " **** Sequence ****** " + parameter
                else:
                    print parameter
                    print getattr(plan, parameter)
                 
                 
    for parameter in dir(plan):
        if parameter[0].isupper():
            if getattr(plan,parameter):
                if not parameter.find("Sequence") == -1:
                    getattr(plan, parameter) = fooo # TODO: Ask Shezi for parametric instance
                else:
                    print getattr(plan,parameter)
    """


    if accessionNumber:
        plan.AccessionNumber = accessionNumber
    if approvalStatus:
        plan.ApprovalStatus = approvalStatus
    if instanceCreation:
        plan.InstanceCreation = instanceCreation
    if instanceCreationDate:
        plan.InstanceCreationDate = instanceCreationDate
    if instanceCreationTime:
        plan.InstanceCreationTime = instanceCreationTime
    if institutionName:
        plan.InstitutionName = institutionName
    if institutionalDepartmentName:
        plan.InstitutionalDepartmentName = institutionalDepartmentName
    if manufacturer:
        plan.Manufacturer = manufacturer
    if manufacturerModelName:
        plan.ManufacturerModelName = manufacturerModelName
    if modality:
        plan.Modality = modality
    if operatorsName:
        plan.OperatorsName = operatorsName
    if patientBirthDate:
        plan.PatientBirthDate = patientBirthDate
    if patientID:
        plan.PatientID = patientID
    if patientName:
        plan.PatientName = patientName
    if patientSex:
        plan.PatientSex = patientSex
    if RTPlanDate:    
        plan.RTPlanDate = RTPlanDate
    if RTPlanGeometry:
        plan.RTPlanGeometry = RTPlanGeometry
    if RTPlanLabel:
        plan.RTPlanLabel = RTPlanLabel
    if RTPlanName:
        plan.RTPlanName = RTPlanName
    if RTPlanTime:
        plan.RTPlanTime = RTPlanTime
    if referringPhysicianName:
        plan.RefferingPhysicianName = refferingPhysicianName
    if SOPClassUID:
        plan.SOPClassUID = SOPClassUID
    if SOPInstanceUID:
        plan.SOPInstanceUID = SOPInstanceUID
    if seriesInstanceUID:
        plan.SeriesInstanceUID = seriesInstanceUID
    if seriesNumber:
        plan.SeriesNumber = seriesNumber
    if softwareVersions:
        plan.SoftwareVersions = softwareVersions
    if stationName:
        plan.StationName = stationName
    if studyDate:
        plan.StudyDate = studyDate
    if studyID:
        plan.StudyID = studyID
    if studyInstanceUID:
        plan.StudyInstanceUID = studyInstanceUID
    if studyTime:
        plan.StudyTime = studyTime

    if instanceCreationDate:
        plan.InstanceCreationDate = instanceCreationDate
    if newfilepath:
        plan.save_as(newfilepath)
    else:
        plan.save_as(filepath)

def clearall_command( filepath, newfilepath=""):
    import dicom
    import re
    plan = dicom.read_file(filepath)

    for parameter in dir(plan):
        if parameter[0].isupper():
            if not parameter.find("Sequence") == -1:
                setattr(plan, parameter, []) 
            else:
                setattr(plan, parameter, "") 

    if newfilepath:
        plan.save_as(newfilepath)
    else:
        plan.save_as(filepath)

if __name__ == '__main__':
    import commandeer
    commandeer.cli()
