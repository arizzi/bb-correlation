import FWCore.ParameterSet.Config as cms

selectedJetTriggerMatchHLTL1Jet10UCALO = cms.EDProducer(
            "PATTriggerMatcherDRDPtLessByR"                    # match by DeltaR only, best match by DeltaR
                        , src     = cms.InputTag( 'selectedPatJets' )
                        , matched = cms.InputTag( 'patTrigger' )          # default producer label as defined in PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
                        , andOr                      = cms.bool( False )  # AND
                        , filterIdsEnum              = cms.vstring( '*' ) # wildcard, overlaps with 'filterIds'
                        , filterIds                  = cms.vint32( 0 )    # wildcard, overlaps with 'filterIdsEnum'
                        , filterLabels               = cms.vstring( '*' ) # wildcard
                        , pathNames                  = cms.vstring(
            'HLT_L1Jet10U'
                        )
                         , pathLastFilterAcceptedOnly = cms.bool( True )   # select only trigger objects used in last filters of succeeding paths
                         , collectionTags             = cms.vstring( '*' ) # wildcard
                         , maxDPtRel = cms.double( 3.0 )
                         , maxDeltaR = cms.double( 0.4 )
                         , resolveAmbiguities    = cms.bool( True )        # only one match per trigger object
                         , resolveByMatchQuality = cms.bool( True )        # take best match found per reco object: by DeltaR here (s. above)

                        )

selectedJetTriggerMatchHLTL1Jet6UCALO = cms.EDProducer(
                "PATTriggerMatcherDRDPtLessByR"                    # match by DeltaR only, best match by DeltaR
                                        , src     = cms.InputTag( 'selectedPatJets' )
                                        , matched = cms.InputTag( 'patTrigger' )          # default producer label as defined in PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
                                        , andOr                      = cms.bool( False )  # AND
                                        , filterIdsEnum              = cms.vstring( '*' ) # wildcard, overlaps with 'filterIds'
                                        , filterIds                  = cms.vint32( 0 )    # wildcard, overlaps with 'filterIdsEnum'
                                        , filterLabels               = cms.vstring( '*' ) # wildcard
                                        , pathNames                  = cms.vstring(
                'HLT_L1Jet6U'
                                        )
                                         , pathLastFilterAcceptedOnly = cms.bool( True )   # select only trigger objects used in last filters of succeeding paths
                                         , collectionTags             = cms.vstring( '*' ) # wildcard
                                         , maxDPtRel = cms.double( 3.0 )
                                         , maxDeltaR = cms.double( 0.4 )
                                         , resolveAmbiguities    = cms.bool( True )        # only one match per trigger object
                                         , resolveByMatchQuality = cms.bool( True )        # take best match found per reco object: by DeltaR here (s. above)

                                        )



selectedJetTriggerMatchHLTJet15UCALO = cms.EDProducer(
        "PATTriggerMatcherDRDPtLessByR"                    # match by DeltaR only, best match by DeltaR
            , src     = cms.InputTag( 'selectedPatJets' )
            , matched = cms.InputTag( 'patTrigger' )          # default producer label as defined in PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
            , andOr                      = cms.bool( False )  # AND
            , filterIdsEnum              = cms.vstring( '*' ) # wildcard, overlaps with 'filterIds'
            , filterIds                  = cms.vint32( 0 )    # wildcard, overlaps with 'filterIdsEnum'
            , filterLabels               = cms.vstring( '*' ) # wildcard
            , pathNames                  = cms.vstring(
        'HLT_Jet15U'
            )
             , pathLastFilterAcceptedOnly = cms.bool( True )   # select only trigger objects used in last filters of succeeding paths
             , collectionTags             = cms.vstring( '*' ) # wildcard
             , maxDPtRel = cms.double( 3.0 )
             , maxDeltaR = cms.double( 0.4 )
             , resolveAmbiguities    = cms.bool( True )        # only one match per trigger object
             , resolveByMatchQuality = cms.bool( True )        # take best match found per reco object: by DeltaR here (s. above)

            )

selectedJetTriggerMatchHLTJet30UCALO = cms.EDProducer(
        "PATTriggerMatcherDRDPtLessByR"                    # match by DeltaR only, best match by DeltaR
            , src     = cms.InputTag( 'selectedPatJets' )
            , matched = cms.InputTag( 'patTrigger' )          # default producer label as defined in PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
            , andOr                      = cms.bool( False )  # AND
            , filterIdsEnum              = cms.vstring( '*' ) # wildcard, overlaps with 'filterIds'
            , filterIds                  = cms.vint32( 0 )    # wildcard, overlaps with 'filterIdsEnum'
            , filterLabels               = cms.vstring( '*' ) # wildcard
            , pathNames                  = cms.vstring(
        'HLT_Jet30U'
            )
             , pathLastFilterAcceptedOnly = cms.bool( True )   # select only trigger objects used in last filters of succeeding paths
             , collectionTags             = cms.vstring( '*' ) # wildcard
             , maxDPtRel = cms.double( 3.0 )
             , maxDeltaR = cms.double( 0.4 )
             , resolveAmbiguities    = cms.bool( True )        # only one match per trigger object
             , resolveByMatchQuality = cms.bool( True )        # take best match found per reco object: by DeltaR here (s. above)

            )

selectedJetTriggerMatchHLTJet50UCALO = cms.EDProducer(
            "PATTriggerMatcherDRDPtLessByR"                    # match by DeltaR only, best match by DeltaR
                        , src     = cms.InputTag( 'selectedPatJets' )
                        , matched = cms.InputTag( 'patTrigger' )          # default producer label as defined in PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
                        , andOr                      = cms.bool( False )  # AND
                        , filterIdsEnum              = cms.vstring( '*' ) # wildcard, overlaps with 'filterIds'
                        , filterIds                  = cms.vint32( 0 )    # wildcard, overlaps with 'filterIdsEnum'
                        , filterLabels               = cms.vstring( '*' ) # wildcard
                        , pathNames                  = cms.vstring(
            'HLT_Jet50U'
                        )
                         , pathLastFilterAcceptedOnly = cms.bool( True )   # select only trigger objects used in last filters of succeeding paths
                         , collectionTags             = cms.vstring( '*' ) # wildcard
                         , maxDPtRel = cms.double( 3.0 )
                         , maxDeltaR = cms.double( 0.4 )
                         , resolveAmbiguities    = cms.bool( True )        # only one match per trigger object
                         , resolveByMatchQuality = cms.bool( True )        # take best match found per reco object: by DeltaR here (s. above)

                        )

selectedJetTriggerMatchHLTJet70UCALO = cms.EDProducer(
            "PATTriggerMatcherDRDPtLessByR"                    # match by DeltaR only, best match by DeltaR
                        , src     = cms.InputTag( 'selectedPatJets' )
                        , matched = cms.InputTag( 'patTrigger' )          # default producer label as defined in PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
                        , andOr                      = cms.bool( False )  # AND
                        , filterIdsEnum              = cms.vstring( '*' ) # wildcard, overlaps with 'filterIds'
                        , filterIds                  = cms.vint32( 0 )    # wildcard, overlaps with 'filterIdsEnum'
                        , filterLabels               = cms.vstring( '*' ) # wildcard
                        , pathNames                  = cms.vstring(
            'HLT_Jet70U'
                        )
                         , pathLastFilterAcceptedOnly = cms.bool( True )   # select only trigger objects used in last filters of succeeding paths
                         , collectionTags             = cms.vstring( '*' ) # wildcard
                         , maxDPtRel = cms.double( 3.0 )
                         , maxDeltaR = cms.double( 0.4 )
                         , resolveAmbiguities    = cms.bool( True )        # only one match per trigger object
                         , resolveByMatchQuality = cms.bool( True )        # take best match found per reco object: by DeltaR here (s. above)

                        )

selectedJetTriggerMatchHLTJet100UCALO = cms.EDProducer(
            "PATTriggerMatcherDRDPtLessByR"                    # match by DeltaR only, best match by DeltaR
                        , src     = cms.InputTag( 'selectedPatJets' )
                        , matched = cms.InputTag( 'patTrigger' )          # default producer label as defined in PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
                        , andOr                      = cms.bool( False )  # AND
                        , filterIdsEnum              = cms.vstring( '*' ) # wildcard, overlaps with 'filterIds'
                        , filterIds                  = cms.vint32( 0 )    # wildcard, overlaps with 'filterIdsEnum'
                        , filterLabels               = cms.vstring( '*' ) # wildcard
                        , pathNames                  = cms.vstring(
            'HLT_Jet100U'
                        )
                         , pathLastFilterAcceptedOnly = cms.bool( True )   # select only trigger objects used in last filters of succeeding paths
                         , collectionTags             = cms.vstring( '*' ) # wildcard
                         , maxDPtRel = cms.double( 3.0 )
                         , maxDeltaR = cms.double( 0.4 )
                         , resolveAmbiguities    = cms.bool( True )        # only one match per trigger object
                         , resolveByMatchQuality = cms.bool( True )        # take best match found per reco object: by DeltaR here (s. above)

                        )




matchPATCALO = cms.Sequence(
    selectedJetTriggerMatchHLTL1Jet6UCALO*
    selectedJetTriggerMatchHLTL1Jet10UCALO*
    selectedJetTriggerMatchHLTJet15UCALO*
    selectedJetTriggerMatchHLTJet30UCALO*
    selectedJetTriggerMatchHLTJet50UCALO*
    selectedJetTriggerMatchHLTJet70UCALO*
    selectedJetTriggerMatchHLTJet100UCALO
    )
