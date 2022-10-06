# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/gateway.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fabric_protos_python.peer import chaincode_event_pb2 as peer_dot_chaincode__event__pb2
from fabric_protos_python.peer import proposal_pb2 as peer_dot_proposal__pb2
from fabric_protos_python.peer import proposal_response_pb2 as peer_dot_proposal__response__pb2
from fabric_protos_python.peer import transaction_pb2 as peer_dot_transaction__pb2
from fabric_protos_python.common import common_pb2 as common_dot_common__pb2
from fabric_protos_python.orderer import ab_pb2 as orderer_dot_ab__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15gateway/gateway.proto\x12\x07gateway\x1a\x1apeer/chaincode_event.proto\x1a\x13peer/proposal.proto\x1a\x1cpeer/proposal_response.proto\x1a\x16peer/transaction.proto\x1a\x13\x63ommon/common.proto\x1a\x10orderer/ab.proto\"\x93\x01\n\x0e\x45ndorseRequest\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x34\n\x14proposed_transaction\x18\x03 \x01(\x0b\x32\x16.protos.SignedProposal\x12\x1f\n\x17\x65ndorsing_organizations\x18\x04 \x03(\t\"A\n\x0f\x45ndorseResponse\x12.\n\x14prepared_transaction\x18\x01 \x01(\x0b\x32\x10.common.Envelope\"k\n\rSubmitRequest\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12.\n\x14prepared_transaction\x18\x03 \x01(\x0b\x32\x10.common.Envelope\"\x10\n\x0eSubmitResponse\"?\n\x19SignedCommitStatusRequest\x12\x0f\n\x07request\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"S\n\x13\x43ommitStatusRequest\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\x0c\"V\n\x14\x43ommitStatusResponse\x12(\n\x06result\x18\x01 \x01(\x0e\x32\x18.protos.TxValidationCode\x12\x14\n\x0c\x62lock_number\x18\x02 \x01(\x04\"\x91\x01\n\x0f\x45valuateRequest\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x34\n\x14proposed_transaction\x18\x03 \x01(\x0b\x32\x16.protos.SignedProposal\x12\x1c\n\x14target_organizations\x18\x04 \x03(\t\"4\n\x10\x45valuateResponse\x12 \n\x06result\x18\x01 \x01(\x0b\x32\x10.protos.Response\"B\n\x1cSignedChaincodeEventsRequest\x12\x0f\n\x07request\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\xa1\x01\n\x16\x43haincodeEventsRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63haincode_id\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\x0c\x12-\n\x0estart_position\x18\x04 \x01(\x0b\x32\x15.orderer.SeekPosition\x12\x1c\n\x14\x61\x66ter_transaction_id\x18\x05 \x01(\t\"W\n\x17\x43haincodeEventsResponse\x12&\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x16.protos.ChaincodeEvent\x12\x14\n\x0c\x62lock_number\x18\x02 \x01(\x04\"?\n\x0b\x45rrorDetail\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06msp_id\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"x\n\x13ProposedTransaction\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12(\n\x08proposal\x18\x02 \x01(\x0b\x32\x16.protos.SignedProposal\x12\x1f\n\x17\x65ndorsing_organizations\x18\x03 \x03(\t\"Q\n\x13PreparedTransaction\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\"\n\x08\x65nvelope\x18\x02 \x01(\x0b\x32\x10.common.Envelope2\xf4\x02\n\x07Gateway\x12<\n\x07\x45ndorse\x12\x17.gateway.EndorseRequest\x1a\x18.gateway.EndorseResponse\x12\x39\n\x06Submit\x12\x16.gateway.SubmitRequest\x1a\x17.gateway.SubmitResponse\x12Q\n\x0c\x43ommitStatus\x12\".gateway.SignedCommitStatusRequest\x1a\x1d.gateway.CommitStatusResponse\x12?\n\x08\x45valuate\x12\x18.gateway.EvaluateRequest\x1a\x19.gateway.EvaluateResponse\x12\\\n\x0f\x43haincodeEvents\x12%.gateway.SignedChaincodeEventsRequest\x1a .gateway.ChaincodeEventsResponse0\x01\x42h\n%org.hyperledger.fabric.protos.gatewayB\x0cGatewayProtoP\x01Z/github.com/hyperledger/fabric-protos-go/gatewayb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway.gateway_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%org.hyperledger.fabric.protos.gatewayB\014GatewayProtoP\001Z/github.com/hyperledger/fabric-protos-go/gateway'
  _ENDORSEREQUEST._serialized_start=177
  _ENDORSEREQUEST._serialized_end=324
  _ENDORSERESPONSE._serialized_start=326
  _ENDORSERESPONSE._serialized_end=391
  _SUBMITREQUEST._serialized_start=393
  _SUBMITREQUEST._serialized_end=500
  _SUBMITRESPONSE._serialized_start=502
  _SUBMITRESPONSE._serialized_end=518
  _SIGNEDCOMMITSTATUSREQUEST._serialized_start=520
  _SIGNEDCOMMITSTATUSREQUEST._serialized_end=583
  _COMMITSTATUSREQUEST._serialized_start=585
  _COMMITSTATUSREQUEST._serialized_end=668
  _COMMITSTATUSRESPONSE._serialized_start=670
  _COMMITSTATUSRESPONSE._serialized_end=756
  _EVALUATEREQUEST._serialized_start=759
  _EVALUATEREQUEST._serialized_end=904
  _EVALUATERESPONSE._serialized_start=906
  _EVALUATERESPONSE._serialized_end=958
  _SIGNEDCHAINCODEEVENTSREQUEST._serialized_start=960
  _SIGNEDCHAINCODEEVENTSREQUEST._serialized_end=1026
  _CHAINCODEEVENTSREQUEST._serialized_start=1029
  _CHAINCODEEVENTSREQUEST._serialized_end=1190
  _CHAINCODEEVENTSRESPONSE._serialized_start=1192
  _CHAINCODEEVENTSRESPONSE._serialized_end=1279
  _ERRORDETAIL._serialized_start=1281
  _ERRORDETAIL._serialized_end=1344
  _PROPOSEDTRANSACTION._serialized_start=1346
  _PROPOSEDTRANSACTION._serialized_end=1466
  _PREPAREDTRANSACTION._serialized_start=1468
  _PREPAREDTRANSACTION._serialized_end=1549
  _GATEWAY._serialized_start=1552
  _GATEWAY._serialized_end=1924
# @@protoc_insertion_point(module_scope)
