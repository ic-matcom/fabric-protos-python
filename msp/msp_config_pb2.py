# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msp/msp_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14msp/msp_config.proto\x12\x03msp\")\n\tMSPConfig\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0e\n\x06\x63onfig\x18\x02 \x01(\x0c\"\x83\x03\n\x0f\x46\x61\x62ricMSPConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nroot_certs\x18\x02 \x03(\x0c\x12\x1a\n\x12intermediate_certs\x18\x03 \x03(\x0c\x12\x0e\n\x06\x61\x64mins\x18\x04 \x03(\x0c\x12\x17\n\x0frevocation_list\x18\x05 \x03(\x0c\x12\x32\n\x10signing_identity\x18\x06 \x01(\x0b\x32\x18.msp.SigningIdentityInfo\x12@\n\x1forganizational_unit_identifiers\x18\x07 \x03(\x0b\x32\x17.msp.FabricOUIdentifier\x12.\n\rcrypto_config\x18\x08 \x01(\x0b\x32\x17.msp.FabricCryptoConfig\x12\x16\n\x0etls_root_certs\x18\t \x03(\x0c\x12\x1e\n\x16tls_intermediate_certs\x18\n \x03(\x0c\x12+\n\x0f\x66\x61\x62ric_node_ous\x18\x0b \x01(\x0b\x32\x12.msp.FabricNodeOUs\"^\n\x12\x46\x61\x62ricCryptoConfig\x12\x1d\n\x15signature_hash_family\x18\x01 \x01(\t\x12)\n!identity_identifier_hash_function\x18\x02 \x01(\t\"~\n\x0fIdemixMSPConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03ipk\x18\x02 \x01(\x0c\x12*\n\x06signer\x18\x03 \x01(\x0b\x32\x1a.msp.IdemixMSPSignerConfig\x12\x15\n\rrevocation_pk\x18\x04 \x01(\x0c\x12\r\n\x05\x65poch\x18\x05 \x01(\x03\"\xa9\x01\n\x15IdemixMSPSignerConfig\x12\x0c\n\x04\x63red\x18\x01 \x01(\x0c\x12\n\n\x02sk\x18\x02 \x01(\x0c\x12&\n\x1eorganizational_unit_identifier\x18\x03 \x01(\t\x12\x0c\n\x04role\x18\x04 \x01(\x05\x12\x15\n\renrollment_id\x18\x05 \x01(\t\x12)\n!credential_revocation_information\x18\x06 \x01(\x0c\"R\n\x13SigningIdentityInfo\x12\x15\n\rpublic_signer\x18\x01 \x01(\x0c\x12$\n\x0eprivate_signer\x18\x02 \x01(\x0b\x32\x0c.msp.KeyInfo\"7\n\x07KeyInfo\x12\x16\n\x0ekey_identifier\x18\x01 \x01(\t\x12\x14\n\x0ckey_material\x18\x02 \x01(\x0c\"Q\n\x12\x46\x61\x62ricOUIdentifier\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0c\x12&\n\x1eorganizational_unit_identifier\x18\x02 \x01(\t\"\xf9\x01\n\rFabricNodeOUs\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x35\n\x14\x63lient_ou_identifier\x18\x02 \x01(\x0b\x32\x17.msp.FabricOUIdentifier\x12\x33\n\x12peer_ou_identifier\x18\x03 \x01(\x0b\x32\x17.msp.FabricOUIdentifier\x12\x34\n\x13\x61\x64min_ou_identifier\x18\x04 \x01(\x0b\x32\x17.msp.FabricOUIdentifier\x12\x36\n\x15orderer_ou_identifier\x18\x05 \x01(\x0b\x32\x17.msp.FabricOUIdentifierBb\n!org.hyperledger.fabric.protos.mspB\x10MspConfigPackageZ+github.com/hyperledger/fabric-protos-go/mspb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'msp.msp_config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!org.hyperledger.fabric.protos.mspB\020MspConfigPackageZ+github.com/hyperledger/fabric-protos-go/msp'
  _MSPCONFIG._serialized_start=29
  _MSPCONFIG._serialized_end=70
  _FABRICMSPCONFIG._serialized_start=73
  _FABRICMSPCONFIG._serialized_end=460
  _FABRICCRYPTOCONFIG._serialized_start=462
  _FABRICCRYPTOCONFIG._serialized_end=556
  _IDEMIXMSPCONFIG._serialized_start=558
  _IDEMIXMSPCONFIG._serialized_end=684
  _IDEMIXMSPSIGNERCONFIG._serialized_start=687
  _IDEMIXMSPSIGNERCONFIG._serialized_end=856
  _SIGNINGIDENTITYINFO._serialized_start=858
  _SIGNINGIDENTITYINFO._serialized_end=940
  _KEYINFO._serialized_start=942
  _KEYINFO._serialized_end=997
  _FABRICOUIDENTIFIER._serialized_start=999
  _FABRICOUIDENTIFIER._serialized_end=1080
  _FABRICNODEOUS._serialized_start=1083
  _FABRICNODEOUS._serialized_end=1332
# @@protoc_insertion_point(module_scope)
