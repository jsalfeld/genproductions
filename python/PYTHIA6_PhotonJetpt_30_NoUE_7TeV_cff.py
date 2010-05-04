

import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

from Configuration.GenProduction.PythiaUESettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(2.007e+04),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTJ(11)=3     ! Choice of the fragmentation function',
     'MSTJ(22)=2     ! Decay those unstable particles',
     'PARJ(71)=10 .  ! for which ctau  10 mm',
     'MSTP(2)=1      ! which order running alphaS',
     'MSTP(33)=0     ! no K factors in hard cross sections',
     'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
     'MSTP(52)=2     ! work with LHAPDF',
     'MSTP(81)=0     ! multiple parton interactions 1 is Pythia default',
     'MSTP(82)=4     ! Defines the multi-parton model',
     'MSTU(21)=1     ! Check on possible errors during program execution',
     'PARP(82)=1.8387   ! pt cutoff for multiparton interactions',
     'PARP(89)=1960. ! sqrts for which PARP82 is set',
     'PARP(83)=0.5   ! Multiple interactions: matter distrbn parameter',
     'PARP(84)=0.4   ! Multiple interactions: matter distribution parameter',
     'PARP(90)=0.16  ! Multiple interactions: rescaling power',
     'PARP(67)=2.5    ! amount of initial-state radiation',
     'PARP(85)=1.0  ! gluon prod. mechanism in MI',
     'PARP(86)=1.0  ! gluon prod. mechanism in MI',
     'PARP(62)=1.25   ! ',
     'PARP(64)=0.2    ! ',
     'MSTP(91)=1      !',
     'PARP(91)=2.1   ! kt distribution',
     'PARP(93)=15.0  ! '), 




processParameters = cms.vstring(
            'MSEL=10',
            'CKIN(3)=30  ! minimum pt hat for hard interactions'),
   # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')

       
   


    )
)
configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string
('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA6_PhotonJetpt_30_7TeV_cff.py,v $'),
    annotation = cms.untracked.string('PhotonJetpt-30 at 7TeV')
)

ProductionFilterSequence = cms.Sequence(generator)
