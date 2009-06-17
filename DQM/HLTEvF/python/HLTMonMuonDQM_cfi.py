import FWCore.ParameterSet.Config as cms

hltMonMuDQM = cms.EDAnalyzer("HLTMuonDQMSource",
    outputFile = cms.untracked.string('./L1TDQM.root'),
    verbose = cms.untracked.bool(False),
    MonitorDaemon = cms.untracked.bool(True),
    reqNum = cms.uint32(1),
    DaqMonitorBEInterface = cms.untracked.bool(True),
    filters = cms.VPSet(
    	# L1 muon
	cms.PSet(
		level = cms.string('L1'),
		directoryName = cms.string('L1PassThrough'),
		triggerBits = cms.vstring('HLT_L1MuOpen','HLT_L1Mu','HLT_L1Mu20')
	),
    	# L2 muon
	cms.PSet(
		level = cms.string('L2'),
		directoryName = cms.string('L2PassThrough'),
		triggerBits = cms.vstring('HLT_L2Mu3','HLT_L2Mu9')
	),
    	# L3 muon
	cms.PSet(
		level = cms.string('L3'),
		directoryName = cms.string('L3Triggers'),
		triggerBits = cms.vstring('HLT_Mu3','HLT_Mu5')
	),
    	# L3 muon
	cms.PSet(
		level = cms.string('JetStream'),
		directoryName = cms.string('JetStream'),
		triggerBits = cms.vstring('HLT_Jet30','HLT_QuadJet15')
	)
    ),
    disableROOToutput = cms.untracked.bool(True)
)


