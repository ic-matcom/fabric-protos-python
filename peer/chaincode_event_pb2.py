# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/chaincode_event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apeer/chaincode_event.proto\x12\x06protos\"Z\n\x0e\x43haincodeEvent\x12\x14\n\x0c\x63haincode_id\x18\x01 \x01(\t\x12\r\n\x05tx_id\x18\x02 \x01(\t\x12\x12\n\nevent_name\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x42i\n\"org.hyperledger.fabric.protos.peerB\x15\x43haincodeEventPackageZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'peer.chaincode_event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"org.hyperledger.fabric.protos.peerB\025ChaincodeEventPackageZ,github.com/hyperledger/fabric-protos-go/peer'
  _CHAINCODEEVENT._serialized_start=38
  _CHAINCODEEVENT._serialized_end=128
# @@protoc_insertion_point(module_scope)
