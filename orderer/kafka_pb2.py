# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orderer/kafka.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13orderer/kafka.proto\x12\x07orderer\"\xaf\x01\n\x0cKafkaMessage\x12/\n\x07regular\x18\x01 \x01(\x0b\x32\x1c.orderer.KafkaMessageRegularH\x00\x12\x35\n\x0btime_to_cut\x18\x02 \x01(\x0b\x32\x1e.orderer.KafkaMessageTimeToCutH\x00\x12/\n\x07\x63onnect\x18\x03 \x01(\x0b\x32\x1c.orderer.KafkaMessageConnectH\x00\x42\x06\n\x04Type\"\xb4\x01\n\x13KafkaMessageRegular\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x12\n\nconfig_seq\x18\x02 \x01(\x04\x12\x31\n\x05\x63lass\x18\x03 \x01(\x0e\x32\".orderer.KafkaMessageRegular.Class\x12\x17\n\x0foriginal_offset\x18\x04 \x01(\x03\",\n\x05\x43lass\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\n\n\x06\x43ONFIG\x10\x02\"-\n\x15KafkaMessageTimeToCut\x12\x14\n\x0c\x62lock_number\x18\x01 \x01(\x04\"&\n\x13KafkaMessageConnect\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\"~\n\rKafkaMetadata\x12\x1d\n\x15last_offset_persisted\x18\x01 \x01(\x03\x12&\n\x1elast_original_offset_processed\x18\x02 \x01(\x03\x12&\n\x1elast_resubmitted_config_offset\x18\x03 \x01(\x03\x42X\n%org.hyperledger.fabric.protos.ordererZ/github.com/hyperledger/fabric-protos-go/ordererb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'orderer.kafka_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%org.hyperledger.fabric.protos.ordererZ/github.com/hyperledger/fabric-protos-go/orderer'
  _KAFKAMESSAGE._serialized_start=33
  _KAFKAMESSAGE._serialized_end=208
  _KAFKAMESSAGEREGULAR._serialized_start=211
  _KAFKAMESSAGEREGULAR._serialized_end=391
  _KAFKAMESSAGEREGULAR_CLASS._serialized_start=347
  _KAFKAMESSAGEREGULAR_CLASS._serialized_end=391
  _KAFKAMESSAGETIMETOCUT._serialized_start=393
  _KAFKAMESSAGETIMETOCUT._serialized_end=438
  _KAFKAMESSAGECONNECT._serialized_start=440
  _KAFKAMESSAGECONNECT._serialized_end=478
  _KAFKAMETADATA._serialized_start=480
  _KAFKAMETADATA._serialized_end=606
# @@protoc_insertion_point(module_scope)
