# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/lifecycle/lifecycle.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from peer import collection_pb2 as peer_dot_collection__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epeer/lifecycle/lifecycle.proto\x12\tlifecycle\x1a\x15peer/collection.proto\"9\n\x14InstallChaincodeArgs\x12!\n\x19\x63haincode_install_package\x18\x01 \x01(\x0c\";\n\x16InstallChaincodeResult\x12\x12\n\npackage_id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"1\n\x1bQueryInstalledChaincodeArgs\x12\x12\n\npackage_id\x18\x01 \x01(\t\"\xfa\x02\n\x1dQueryInstalledChaincodeResult\x12\x12\n\npackage_id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12L\n\nreferences\x18\x03 \x03(\x0b\x32\x38.lifecycle.QueryInstalledChaincodeResult.ReferencesEntry\x1a\x66\n\x0fReferencesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32\x33.lifecycle.QueryInstalledChaincodeResult.References:\x02\x38\x01\x1aT\n\nReferences\x12\x46\n\nchaincodes\x18\x01 \x03(\x0b\x32\x32.lifecycle.QueryInstalledChaincodeResult.Chaincode\x1a*\n\tChaincode\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"6\n GetInstalledChaincodePackageArgs\x12\x12\n\npackage_id\x18\x01 \x01(\t\"G\n\"GetInstalledChaincodePackageResult\x12!\n\x19\x63haincode_install_package\x18\x01 \x01(\x0c\"\x1e\n\x1cQueryInstalledChaincodesArgs\"\x84\x04\n\x1eQueryInstalledChaincodesResult\x12Z\n\x14installed_chaincodes\x18\x01 \x03(\x0b\x32<.lifecycle.QueryInstalledChaincodesResult.InstalledChaincode\x1a\x82\x02\n\x12InstalledChaincode\x12\x12\n\npackage_id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12`\n\nreferences\x18\x03 \x03(\x0b\x32L.lifecycle.QueryInstalledChaincodesResult.InstalledChaincode.ReferencesEntry\x1ag\n\x0fReferencesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0b\x32\x34.lifecycle.QueryInstalledChaincodesResult.References:\x02\x38\x01\x1aU\n\nReferences\x12G\n\nchaincodes\x18\x01 \x03(\x0b\x32\x33.lifecycle.QueryInstalledChaincodesResult.Chaincode\x1a*\n\tChaincode\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\xa7\x02\n&ApproveChaincodeDefinitionForMyOrgArgs\x12\x10\n\x08sequence\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x1a\n\x12\x65ndorsement_plugin\x18\x04 \x01(\t\x12\x19\n\x11validation_plugin\x18\x05 \x01(\t\x12\x1c\n\x14validation_parameter\x18\x06 \x01(\x0c\x12\x34\n\x0b\x63ollections\x18\x07 \x01(\x0b\x32\x1f.protos.CollectionConfigPackage\x12\x15\n\rinit_required\x18\x08 \x01(\x08\x12*\n\x06source\x18\t \x01(\x0b\x32\x1a.lifecycle.ChaincodeSource\"\xbf\x01\n\x0f\x43haincodeSource\x12=\n\x0bunavailable\x18\x01 \x01(\x0b\x32&.lifecycle.ChaincodeSource.UnavailableH\x00\x12\x39\n\rlocal_package\x18\x02 \x01(\x0b\x32 .lifecycle.ChaincodeSource.LocalH\x00\x1a\r\n\x0bUnavailable\x1a\x1b\n\x05Local\x12\x12\n\npackage_id\x18\x01 \x01(\tB\x06\n\x04Type\"*\n(ApproveChaincodeDefinitionForMyOrgResult\"\xf2\x01\n\x1d\x43ommitChaincodeDefinitionArgs\x12\x10\n\x08sequence\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x1a\n\x12\x65ndorsement_plugin\x18\x04 \x01(\t\x12\x19\n\x11validation_plugin\x18\x05 \x01(\t\x12\x1c\n\x14validation_parameter\x18\x06 \x01(\x0c\x12\x34\n\x0b\x63ollections\x18\x07 \x01(\x0b\x32\x1f.protos.CollectionConfigPackage\x12\x15\n\rinit_required\x18\x08 \x01(\x08\"!\n\x1f\x43ommitChaincodeDefinitionResult\"\xed\x01\n\x18\x43heckCommitReadinessArgs\x12\x10\n\x08sequence\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x1a\n\x12\x65ndorsement_plugin\x18\x04 \x01(\t\x12\x19\n\x11validation_plugin\x18\x05 \x01(\t\x12\x1c\n\x14validation_parameter\x18\x06 \x01(\x0c\x12\x34\n\x0b\x63ollections\x18\x07 \x01(\x0b\x32\x1f.protos.CollectionConfigPackage\x12\x15\n\rinit_required\x18\x08 \x01(\x08\"\x97\x01\n\x1a\x43heckCommitReadinessResult\x12G\n\tapprovals\x18\x01 \x03(\x0b\x32\x34.lifecycle.CheckCommitReadinessResult.ApprovalsEntry\x1a\x30\n\x0e\x41pprovalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"F\n$QueryApprovedChaincodeDefinitionArgs\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x03\"\x99\x02\n&QueryApprovedChaincodeDefinitionResult\x12\x10\n\x08sequence\x18\x01 \x01(\x03\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x1a\n\x12\x65ndorsement_plugin\x18\x03 \x01(\t\x12\x19\n\x11validation_plugin\x18\x04 \x01(\t\x12\x1c\n\x14validation_parameter\x18\x05 \x01(\x0c\x12\x34\n\x0b\x63ollections\x18\x06 \x01(\x0b\x32\x1f.protos.CollectionConfigPackage\x12\x15\n\rinit_required\x18\x07 \x01(\x08\x12*\n\x06source\x18\x08 \x01(\x0b\x32\x1a.lifecycle.ChaincodeSource\",\n\x1cQueryChaincodeDefinitionArgs\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xe4\x02\n\x1eQueryChaincodeDefinitionResult\x12\x10\n\x08sequence\x18\x01 \x01(\x03\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x1a\n\x12\x65ndorsement_plugin\x18\x03 \x01(\t\x12\x19\n\x11validation_plugin\x18\x04 \x01(\t\x12\x1c\n\x14validation_parameter\x18\x05 \x01(\x0c\x12\x34\n\x0b\x63ollections\x18\x06 \x01(\x0b\x32\x1f.protos.CollectionConfigPackage\x12\x15\n\rinit_required\x18\x07 \x01(\x08\x12K\n\tapprovals\x18\x08 \x03(\x0b\x32\x38.lifecycle.QueryChaincodeDefinitionResult.ApprovalsEntry\x1a\x30\n\x0e\x41pprovalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\x1f\n\x1dQueryChaincodeDefinitionsArgs\"\xeb\x02\n\x1fQueryChaincodeDefinitionsResult\x12]\n\x15\x63haincode_definitions\x18\x01 \x03(\x0b\x32>.lifecycle.QueryChaincodeDefinitionsResult.ChaincodeDefinition\x1a\xe8\x01\n\x13\x43haincodeDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x03\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x1a\n\x12\x65ndorsement_plugin\x18\x04 \x01(\t\x12\x19\n\x11validation_plugin\x18\x05 \x01(\t\x12\x1c\n\x14validation_parameter\x18\x06 \x01(\x0c\x12\x34\n\x0b\x63ollections\x18\x07 \x01(\x0b\x32\x1f.protos.CollectionConfigPackage\x12\x15\n\rinit_required\x18\x08 \x01(\x08\x42\x66\n,org.hyperledger.fabric.protos.peer.lifecycleZ6github.com/hyperledger/fabric-protos-go/peer/lifecycleb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'peer.lifecycle.lifecycle_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n,org.hyperledger.fabric.protos.peer.lifecycleZ6github.com/hyperledger/fabric-protos-go/peer/lifecycle'
  _QUERYINSTALLEDCHAINCODERESULT_REFERENCESENTRY._options = None
  _QUERYINSTALLEDCHAINCODERESULT_REFERENCESENTRY._serialized_options = b'8\001'
  _QUERYINSTALLEDCHAINCODESRESULT_INSTALLEDCHAINCODE_REFERENCESENTRY._options = None
  _QUERYINSTALLEDCHAINCODESRESULT_INSTALLEDCHAINCODE_REFERENCESENTRY._serialized_options = b'8\001'
  _CHECKCOMMITREADINESSRESULT_APPROVALSENTRY._options = None
  _CHECKCOMMITREADINESSRESULT_APPROVALSENTRY._serialized_options = b'8\001'
  _QUERYCHAINCODEDEFINITIONRESULT_APPROVALSENTRY._options = None
  _QUERYCHAINCODEDEFINITIONRESULT_APPROVALSENTRY._serialized_options = b'8\001'
  _INSTALLCHAINCODEARGS._serialized_start=68
  _INSTALLCHAINCODEARGS._serialized_end=125
  _INSTALLCHAINCODERESULT._serialized_start=127
  _INSTALLCHAINCODERESULT._serialized_end=186
  _QUERYINSTALLEDCHAINCODEARGS._serialized_start=188
  _QUERYINSTALLEDCHAINCODEARGS._serialized_end=237
  _QUERYINSTALLEDCHAINCODERESULT._serialized_start=240
  _QUERYINSTALLEDCHAINCODERESULT._serialized_end=618
  _QUERYINSTALLEDCHAINCODERESULT_REFERENCESENTRY._serialized_start=386
  _QUERYINSTALLEDCHAINCODERESULT_REFERENCESENTRY._serialized_end=488
  _QUERYINSTALLEDCHAINCODERESULT_REFERENCES._serialized_start=490
  _QUERYINSTALLEDCHAINCODERESULT_REFERENCES._serialized_end=574
  _QUERYINSTALLEDCHAINCODERESULT_CHAINCODE._serialized_start=576
  _QUERYINSTALLEDCHAINCODERESULT_CHAINCODE._serialized_end=618
  _GETINSTALLEDCHAINCODEPACKAGEARGS._serialized_start=620
  _GETINSTALLEDCHAINCODEPACKAGEARGS._serialized_end=674
  _GETINSTALLEDCHAINCODEPACKAGERESULT._serialized_start=676
  _GETINSTALLEDCHAINCODEPACKAGERESULT._serialized_end=747
  _QUERYINSTALLEDCHAINCODESARGS._serialized_start=749
  _QUERYINSTALLEDCHAINCODESARGS._serialized_end=779
  _QUERYINSTALLEDCHAINCODESRESULT._serialized_start=782
  _QUERYINSTALLEDCHAINCODESRESULT._serialized_end=1298
  _QUERYINSTALLEDCHAINCODESRESULT_INSTALLEDCHAINCODE._serialized_start=909
  _QUERYINSTALLEDCHAINCODESRESULT_INSTALLEDCHAINCODE._serialized_end=1167
  _QUERYINSTALLEDCHAINCODESRESULT_INSTALLEDCHAINCODE_REFERENCESENTRY._serialized_start=1064
  _QUERYINSTALLEDCHAINCODESRESULT_INSTALLEDCHAINCODE_REFERENCESENTRY._serialized_end=1167
  _QUERYINSTALLEDCHAINCODESRESULT_REFERENCES._serialized_start=1169
  _QUERYINSTALLEDCHAINCODESRESULT_REFERENCES._serialized_end=1254
  _QUERYINSTALLEDCHAINCODESRESULT_CHAINCODE._serialized_start=576
  _QUERYINSTALLEDCHAINCODESRESULT_CHAINCODE._serialized_end=618
  _APPROVECHAINCODEDEFINITIONFORMYORGARGS._serialized_start=1301
  _APPROVECHAINCODEDEFINITIONFORMYORGARGS._serialized_end=1596
  _CHAINCODESOURCE._serialized_start=1599
  _CHAINCODESOURCE._serialized_end=1790
  _CHAINCODESOURCE_UNAVAILABLE._serialized_start=1740
  _CHAINCODESOURCE_UNAVAILABLE._serialized_end=1753
  _CHAINCODESOURCE_LOCAL._serialized_start=1755
  _CHAINCODESOURCE_LOCAL._serialized_end=1782
  _APPROVECHAINCODEDEFINITIONFORMYORGRESULT._serialized_start=1792
  _APPROVECHAINCODEDEFINITIONFORMYORGRESULT._serialized_end=1834
  _COMMITCHAINCODEDEFINITIONARGS._serialized_start=1837
  _COMMITCHAINCODEDEFINITIONARGS._serialized_end=2079
  _COMMITCHAINCODEDEFINITIONRESULT._serialized_start=2081
  _COMMITCHAINCODEDEFINITIONRESULT._serialized_end=2114
  _CHECKCOMMITREADINESSARGS._serialized_start=2117
  _CHECKCOMMITREADINESSARGS._serialized_end=2354
  _CHECKCOMMITREADINESSRESULT._serialized_start=2357
  _CHECKCOMMITREADINESSRESULT._serialized_end=2508
  _CHECKCOMMITREADINESSRESULT_APPROVALSENTRY._serialized_start=2460
  _CHECKCOMMITREADINESSRESULT_APPROVALSENTRY._serialized_end=2508
  _QUERYAPPROVEDCHAINCODEDEFINITIONARGS._serialized_start=2510
  _QUERYAPPROVEDCHAINCODEDEFINITIONARGS._serialized_end=2580
  _QUERYAPPROVEDCHAINCODEDEFINITIONRESULT._serialized_start=2583
  _QUERYAPPROVEDCHAINCODEDEFINITIONRESULT._serialized_end=2864
  _QUERYCHAINCODEDEFINITIONARGS._serialized_start=2866
  _QUERYCHAINCODEDEFINITIONARGS._serialized_end=2910
  _QUERYCHAINCODEDEFINITIONRESULT._serialized_start=2913
  _QUERYCHAINCODEDEFINITIONRESULT._serialized_end=3269
  _QUERYCHAINCODEDEFINITIONRESULT_APPROVALSENTRY._serialized_start=2460
  _QUERYCHAINCODEDEFINITIONRESULT_APPROVALSENTRY._serialized_end=2508
  _QUERYCHAINCODEDEFINITIONSARGS._serialized_start=3271
  _QUERYCHAINCODEDEFINITIONSARGS._serialized_end=3302
  _QUERYCHAINCODEDEFINITIONSRESULT._serialized_start=3305
  _QUERYCHAINCODEDEFINITIONSRESULT._serialized_end=3668
  _QUERYCHAINCODEDEFINITIONSRESULT_CHAINCODEDEFINITION._serialized_start=3436
  _QUERYCHAINCODEDEFINITIONSRESULT_CHAINCODEDEFINITION._serialized_end=3668
# @@protoc_insertion_point(module_scope)
