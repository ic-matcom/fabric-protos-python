# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/ledger.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63ommon/ledger.proto\x12\x06\x63ommon\"\x9b\x01\n\x0e\x42lockchainInfo\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x18\n\x10\x63urrentBlockHash\x18\x02 \x01(\x0c\x12\x19\n\x11previousBlockHash\x18\x03 \x01(\x0c\x12\x44\n\x19\x62ootstrappingSnapshotInfo\x18\x04 \x01(\x0b\x32!.common.BootstrappingSnapshotInfo\"8\n\x19\x42ootstrappingSnapshotInfo\x12\x1b\n\x13lastBlockInSnapshot\x18\x01 \x01(\x04\x42V\n$org.hyperledger.fabric.protos.commonZ.github.com/hyperledger/fabric-protos-go/commonb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.ledger_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$org.hyperledger.fabric.protos.commonZ.github.com/hyperledger/fabric-protos-go/common'
  _BLOCKCHAININFO._serialized_start=32
  _BLOCKCHAININFO._serialized_end=187
  _BOOTSTRAPPINGSNAPSHOTINFO._serialized_start=189
  _BOOTSTRAPPINGSNAPSHOTINFO._serialized_end=245
# @@protoc_insertion_point(module_scope)
