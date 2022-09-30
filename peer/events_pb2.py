# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2
from ledger.rwset import rwset_pb2 as ledger_dot_rwset_dot_rwset__pb2
from peer import chaincode_event_pb2 as peer_dot_chaincode__event__pb2
from peer import transaction_pb2 as peer_dot_transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11peer/events.proto\x12\x06protos\x1a\x13\x63ommon/common.proto\x1a\x18ledger/rwset/rwset.proto\x1a\x1apeer/chaincode_event.proto\x1a\x16peer/transaction.proto\"o\n\rFilteredBlock\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x04\x12:\n\x15\x66iltered_transactions\x18\x04 \x03(\x0b\x32\x1b.protos.FilteredTransaction\"\xc6\x01\n\x13\x46ilteredTransaction\x12\x0c\n\x04txid\x18\x01 \x01(\t\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.common.HeaderType\x12\x34\n\x12tx_validation_code\x18\x03 \x01(\x0e\x32\x18.protos.TxValidationCode\x12\x41\n\x13transaction_actions\x18\x04 \x01(\x0b\x32\".protos.FilteredTransactionActionsH\x00\x42\x06\n\x04\x44\x61ta\"X\n\x1a\x46ilteredTransactionActions\x12:\n\x11\x63haincode_actions\x18\x01 \x03(\x0b\x32\x1f.protos.FilteredChaincodeAction\"J\n\x17\x46ilteredChaincodeAction\x12/\n\x0f\x63haincode_event\x18\x01 \x01(\x0b\x32\x16.protos.ChaincodeEvent\"\xcf\x01\n\x13\x42lockAndPrivateData\x12\x1c\n\x05\x62lock\x18\x01 \x01(\x0b\x32\r.common.Block\x12I\n\x10private_data_map\x18\x02 \x03(\x0b\x32/.protos.BlockAndPrivateData.PrivateDataMapEntry\x1aO\n\x13PrivateDataMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.rwset.TxPvtReadWriteSet:\x02\x38\x01\"\xcb\x01\n\x0f\x44\x65liverResponse\x12 \n\x06status\x18\x01 \x01(\x0e\x32\x0e.common.StatusH\x00\x12\x1e\n\x05\x62lock\x18\x02 \x01(\x0b\x32\r.common.BlockH\x00\x12/\n\x0e\x66iltered_block\x18\x03 \x01(\x0b\x32\x15.protos.FilteredBlockH\x00\x12=\n\x16\x62lock_and_private_data\x18\x04 \x01(\x0b\x32\x1b.protos.BlockAndPrivateDataH\x00\x42\x06\n\x04Type2\xd4\x01\n\x07\x44\x65liver\x12:\n\x07\x44\x65liver\x12\x10.common.Envelope\x1a\x17.protos.DeliverResponse\"\x00(\x01\x30\x01\x12\x42\n\x0f\x44\x65liverFiltered\x12\x10.common.Envelope\x1a\x17.protos.DeliverResponse\"\x00(\x01\x30\x01\x12I\n\x16\x44\x65liverWithPrivateData\x12\x10.common.Envelope\x1a\x17.protos.DeliverResponse\"\x00(\x01\x30\x01\x42\x61\n\"org.hyperledger.fabric.protos.peerB\rEventsPackageZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'peer.events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"org.hyperledger.fabric.protos.peerB\rEventsPackageZ,github.com/hyperledger/fabric-protos-go/peer'
  _BLOCKANDPRIVATEDATA_PRIVATEDATAMAPENTRY._options = None
  _BLOCKANDPRIVATEDATA_PRIVATEDATAMAPENTRY._serialized_options = b'8\001'
  _FILTEREDBLOCK._serialized_start=128
  _FILTEREDBLOCK._serialized_end=239
  _FILTEREDTRANSACTION._serialized_start=242
  _FILTEREDTRANSACTION._serialized_end=440
  _FILTEREDTRANSACTIONACTIONS._serialized_start=442
  _FILTEREDTRANSACTIONACTIONS._serialized_end=530
  _FILTEREDCHAINCODEACTION._serialized_start=532
  _FILTEREDCHAINCODEACTION._serialized_end=606
  _BLOCKANDPRIVATEDATA._serialized_start=609
  _BLOCKANDPRIVATEDATA._serialized_end=816
  _BLOCKANDPRIVATEDATA_PRIVATEDATAMAPENTRY._serialized_start=737
  _BLOCKANDPRIVATEDATA_PRIVATEDATAMAPENTRY._serialized_end=816
  _DELIVERRESPONSE._serialized_start=819
  _DELIVERRESPONSE._serialized_end=1022
  _DELIVER._serialized_start=1025
  _DELIVER._serialized_end=1237
# @@protoc_insertion_point(module_scope)
