# Auto generated configuration file
# using: 
# Revision: 1.77 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/PYTHIA6_Tauola_SM_VBF_H_ZZ_2l2nu_mH180_10TeV_cff.py -s GEN --eventcontent RAWSIM --datatier GEN --conditions FrontierConditions_GlobalTag,IDEAL_V9::All -n 1000 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/MixingNoPileUp_cff')
process.load('Configuration/StandardSequences/GeometryPilot2_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('Configuration/StandardSequences/Generator_cff')
process.load('Configuration/StandardSequences/VtxSmearedEarly10TeVCollision_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration/EventContent/EventContent_cff')

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('PYTHIA6 Tauola SM VBF H->ZZ->2l 2nu  at 10TeV with mH=180 GeV'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA6_Tauola_SM_VBF_H_ZZ_2l2nu_mH180_10TeV_cff.py,v $')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)
process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)
# Input source
process.source = cms.Source("PythiaSource",
    UseExternalGenerators = cms.untracked.bool(True),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    ExternalGenerators = cms.PSet(
        Tauola = cms.untracked.PSet(
            UseTauolaPolarization = cms.bool(True),
            InputCards = cms.vstring('TAUOLA = 0 0 0   ! TAUOLA ')
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    comEnergy = cms.untracked.double(10000.0),
    crossSection = cms.untracked.double(55000000000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTJ(11)=3     ! Choice of the fragmentation function', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(51)=10042     ! CTEQ6L1 structure function chosen', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'MSTP(81)=1     ! multiple parton interactions 1 is Pythia default', 
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
            'MSTP(91)=1     !', 
            'PARP(91)=2.1   ! kt distribution', 
            'PARP(93)=15.0  ! '),
        processParameters = cms.vstring('MSEL=0            ! User defined processes', 
            'MSUB(102)=0       ! gg->H', 
            'MSUB(123)=1       ! qq-ZZqq->Hqq', 
            'MSUB(124)=1       ! qq-WWqq->Hqq', 
            'PMAS(23,1)=91.188 ! Z mass', 
            'PMAS(24,1)=80.450 ! W mass', 
            'PMAS(25,1)=180.0  ! mass of Higgs', 
            'MDME(210,1)=0    ! Higgs decay into dd', 
            'MDME(211,1)=0    ! Higgs decay into uu', 
            'MDME(212,1)=0    ! Higgs decay into ss', 
            'MDME(213,1)=0    ! Higgs decay into cc', 
            'MDME(214,1)=0    ! Higgs decay into bb', 
            'MDME(215,1)=0    ! Higgs decay into tt', 
            'MDME(216,1)=0    ! Higgs decay into', 
            'MDME(217,1)=0    ! Higgs decay into Higgs decay', 
            'MDME(218,1)=0    ! Higgs decay into e e', 
            'MDME(219,1)=0    ! Higgs decay into mu mu', 
            'MDME(220,1)=0    ! Higgs decay into tau tau', 
            'MDME(221,1)=0    ! Higgs decay into Higgs decay', 
            'MDME(222,1)=0    ! Higgs decay into g g', 
            'MDME(223,1)=0    ! Higgs decay into gam gam', 
            'MDME(224,1)=0    ! Higgs decay into gam Z', 
            'MDME(225,1)=1    ! Higgs decay into Z Z', 
            'MDME(226,1)=0    ! Higgs decay into W W', 
            'MDME(174,1)=0           ! Z decay into d dbar', 
            'MDME(175,1)=0           ! Z decay into u ubar', 
            'MDME(176,1)=0           ! Z decay into s sbar', 
            'MDME(177,1)=0           ! Z decay into c cbar', 
            'MDME(178,1)=0           ! Z decay into b bbar', 
            'MDME(179,1)=0           ! Z decay into t tbar', 
            'MDME(182,1)=4           ! Z decay into e- e+', 
            'MDME(183,1)=5           ! Z decay into nu_e nu_ebar', 
            'MDME(184,1)=4           ! Z decay into mu- mu+', 
            'MDME(185,1)=5           ! Z decay into nu_mu nu_mubar', 
            'MDME(186,1)=4           ! Z decay into tau- tau+', 
            'MDME(187,1)=5           ! Z decay into nu_tau nu_taubar'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('PYTHIA6_Tauola_SM_VBF_H_ZZ_2l2nu_mH180_10TeV_cff_py_GEN.root'),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'IDEAL_V9::All'

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.out_step = cms.EndPath(process.output)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.out_step)