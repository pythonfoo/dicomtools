#!/usr/bin/env python 
#-*- coding: utf-8 -*-
""" Some Description to enter"""
__author__ = "oerb"
__copyright__ = "GPL 2013"
__license__ = "GPL" 


def print_data_command(filepath, instanceCreationDate=False, 
        accessionNumber=False, approvalStatus=False, 
        beamSequence=False, doseReferenceSequence=False, 
        fractionGroupSequence=False):
    """ Show dicom Data by given Parameter

    some commend foo
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
    if manufacturerMode1Name:
        print "ManufacturerMode1Name: " + plan.ManufacturerMode1Name
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
    if RTPlanGeomentry:
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
        print str(plan.Referenced RTPlanSequence)
    if ReferencedStructureSetSequence:
        print " ------------- Referenced Structure Set Sequence ----------"
        print str(plan.ReferencedStructureSetSequence)
    if referencedPhysicianName:
        print "ReferencedPhysicianName: " + plan.ReferencedPhysicianName
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
