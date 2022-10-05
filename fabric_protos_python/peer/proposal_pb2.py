# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fabric_protos_python.peer import chaincode_pb2 as peer_dot_chaincode__pb2
from fabric_protos_python.peer import proposal_response_pb2 as peer_dot_proposal__response__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13peer/proposal.proto\x12\x06protos\x1a\x14peer/chaincode.proto\x1a\x1cpeer/proposal_response.proto\";\n\x0eSignedProposal\x12\x16\n\x0eproposal_bytes\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\">\n\x08Proposal\x12\x0e\n\x06header\x18\x01 \x01(\x0c\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x11\n\textension\x18\x03 \x01(\x0c\"^\n\x18\x43haincodeHeaderExtension\x12)\n\x0c\x63haincode_id\x18\x02 \x01(\x0b\x32\x13.protos.ChaincodeIDJ\x04\x08\x01\x10\x02R\x11payload_visbility\"\xa8\x01\n\x18\x43haincodeProposalPayload\x12\r\n\x05input\x18\x01 \x01(\x0c\x12H\n\x0cTransientMap\x18\x02 \x03(\x0b\x32\x32.protos.ChaincodeProposalPayload.TransientMapEntry\x1a\x33\n\x11TransientMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\x99\x01\n\x0f\x43haincodeAction\x12\x0f\n\x07results\x18\x01 \x01(\x0c\x12\x0e\n\x06\x65vents\x18\x02 \x01(\x0c\x12\"\n\x08response\x18\x03 \x01(\x0b\x32\x10.protos.Response\x12)\n\x0c\x63haincode_id\x18\x04 \x01(\x0b\x32\x13.protos.ChaincodeIDJ\x04\x08\x05\x10\x06R\x10token_operationsBc\n\"org.hyperledger.fabric.protos.peerB\x0fProposalPackageZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'peer.proposal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"org.hyperledger.fabric.protos.peerB\017ProposalPackageZ,github.com/hyperledger/fabric-protos-go/peer'
  _CHAINCODEPROPOSALPAYLOAD_TRANSIENTMAPENTRY._options = None
  _CHAINCODEPROPOSALPAYLOAD_TRANSIENTMAPENTRY._serialized_options = b'8\001'
  _SIGNEDPROPOSAL._serialized_start=83
  _SIGNEDPROPOSAL._serialized_end=142
  _PROPOSAL._serialized_start=144
  _PROPOSAL._serialized_end=206
  _CHAINCODEHEADEREXTENSION._serialized_start=208
  _CHAINCODEHEADEREXTENSION._serialized_end=302
  _CHAINCODEPROPOSALPAYLOAD._serialized_start=305
  _CHAINCODEPROPOSALPAYLOAD._serialized_end=473
  _CHAINCODEPROPOSALPAYLOAD_TRANSIENTMAPENTRY._serialized_start=422
  _CHAINCODEPROPOSALPAYLOAD_TRANSIENTMAPENTRY._serialized_end=473
  _CHAINCODEACTION._serialized_start=476
  _CHAINCODEACTION._serialized_end=629
# @@protoc_insertion_point(module_scope)