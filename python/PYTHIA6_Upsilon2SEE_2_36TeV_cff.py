import FWCore.ParameterSet.Config as cms

# since a source is still needed   
source = cms.Source('EmptySource')

from Configuration.Generator.PythiaUESettings_cfi import *
generator = cms.EDFilter('Pythia6GeneratorFilter',
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.132),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(2360.0),
    crossSection = cms.untracked.double(22440.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSEL=62          ! Quarkonia NRQCD ', 
            'KFPR(461,1)  = 100553     ! change 461 to Upsilon(2S) + g', 
            'PMAS(365,1)  = 10.0300   ! change bb~ mass larger than Upsilon(2S) 10.02330',
            'PMAS(366,1)  = 10.0300   ! change bb~ mass larger than Upsilon(2S) 10.02330',
            'PMAS(367,1)  = 10.0300   ! change bb~ mass larger than Upsilon(2S) 10.02330',
            'KFDP(4214,1) = 100553     ! bb~ -> Upsilon(2S)',
            'KFDP(4215,1) = 100553     ! bb~ -> Upsilon(2S)',
            'KFDP(4216,1) = 100553     ! bb~ -> Upsilon(2S)',
            'PMAS(278,1)  = 10.23250   ! change chi_0b(1P) mass to chi_0b(2P)', 
            'KFDP(1520,1) = 100553     ! chi_0b(2P) -> Upsilon(2S)', 
            'BRAT(1520)   = 0.046      ! br of chi_0b(2P) -> Upsilon(2S)', 
            'BRAT(1521)   = 0.954      ! br of chi_0b(2P) -> rndmflav rndmflavbar', 
            'PMAS(294,1)  = 10.25546   ! change chi_1b(1P) mass to chi_1b(2P)', 
            'KFDP(1565,1) = 100553     ! chi_1b(2P) -> Upsilon(2S)', 
            'BRAT(1565)   = 0.210      ! br of chi_1b(2P) -> Upsilon(2S)', 
            'BRAT(1566)   = 0.790      ! br of chi_1b(2P) -> rndmflav rndmflavbar', 
            'PMAS(148,1)  = 10.26865   ! change chi_2b(1P) mass to chi_2b(2P)', 
            'KFDP(1043,1) = 100553     ! chi_2b(2P) -> Upsilon(2S)', 
            'BRAT(1043)   = 0.162      ! br of chi_2b(2P) -> Upsilon(2S)', 
            'BRAT(1044)   = 0.838      ! br of chi_2b(2P) -> rndmflav rndmflavbar', 
            'PARP(146)=4.63   ! New values for COM matrix elements', 
            'PARP(147)=0.045  ! New values for COM matrix elements', 
            'PARP(148)=0.006  ! New values for COM matrix elements', 
            'PARP(149)=0.006  ! New values for COM matrix elements', 
            'PARP(150)=0.108  ! New values for COM matrix elements', 
            'MDME(1578,1) = 1 ! 0.014000    e-              e+', 
            'MDME(1579,1) = 0 ! 0.014000    mu-             mu+', 
            'MDME(1580,1) = 0 ! 0.014000    tau-            tau+', 
            'MDME(1581,1) = 0 ! 0.008000    d               dbar', 
            'MDME(1582,1) = 0 ! 0.024000    u               ubar', 
            'MDME(1583,1) = 0 ! 0.008000    s               sbar', 
            'MDME(1584,1) = 0 ! 0.024000    c               cbar', 
            'MDME(1585,1) = 0 ! 0.425000    g               g            g', 
            'MDME(1586,1) = 0 ! 0.020000    gamma           g            g', 
            'MDME(1587,1) = 0 ! 0.185000    Upsilon         pi+          pi-', 
            'MDME(1588,1) = 0 ! 0.088000    Upsilon         pi0          pi0', 
            'MDME(1589,1) = 0 ! 0.043000    chi_0b          gamma', 
            'MDME(1590,1) = 0 ! 0.067000    chi_1b          gamma', 
            'MDME(1591,1) = 0 ! 0.066000    chi_2b          gamma', 
            'MSTP(142)=2      ! turns on the PYEVWT Pt re-weighting routine', 
            'PARJ(13)=0.750   ! probability that a c or b meson has S=1', 
            'PARJ(14)=0.162   ! probability that a meson with S=0 is produced with L=1, J=1', 
            'PARJ(15)=0.018   ! probability that a meson with S=1 is produced with L=1, J=0', 
            'PARJ(16)=0.054   ! probability that a meson with S=1 is produced with L=1, J=1', 
            'MSTP(145)=0      ! choice of polarization', 
            'MSTP(146)=0      ! choice of polarization frame ONLY when mstp(145)=1', 
            'MSTP(147)=0      ! particular helicity or density matrix component when mstp(145)=1', 
            'MSTP(148)=1      ! possibility to allow for final-state shower evolution, extreme case !', 
            'MSTP(149)=1      ! if mstp(148)=1, it determines the kinematics of the QQ~3S1(8)->QQ~3S1(8)+g branching'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters', 
            'CSAParameters'),
        CSAParameters = cms.vstring('CSAMODE = 6     ! cross-section reweighted quarkonia')
    )
)


oniafilter = cms.EDFilter("MCSmartSingleParticleFilter",
    Status = cms.untracked.vint32(2),
    MinPt = cms.untracked.vdouble(0.0),
    ParticleID = cms.untracked.vint32(100553),
    MaxEta = cms.untracked.vdouble(1000.0),
    MinEta = cms.untracked.vdouble(-1000.0)
)

egenfilter = cms.EDFilter("MCSmartSingleParticleFilter",
    MaxDecayRadius = cms.untracked.vdouble(1500.0, 1500.0),
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(1.0, 1.0),
    MaxPt = cms.untracked.vdouble(1000.0, 1000.0),
    ParticleID = cms.untracked.vint32(11, -11),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MaxDecayZ = cms.untracked.vdouble(3000.0, 3000.0),
    MinDecayZ = cms.untracked.vdouble(-3000.0, -3000.0)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*egenfilter)


