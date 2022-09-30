# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gossip/message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from peer import collection_pb2 as peer_dot_collection__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14gossip/message.proto\x12\x06gossip\x1a\x15peer/collection.proto\"_\n\x08\x45nvelope\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12/\n\x0fsecret_envelope\x18\x03 \x01(\x0b\x32\x16.gossip.SecretEnvelope\"4\n\x0eSecretEnvelope\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"/\n\x06Secret\x12\x1a\n\x10internalEndpoint\x18\x01 \x01(\tH\x00\x42\t\n\x07\x63ontent\"\x8d\t\n\rGossipMessage\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\x0c\x12&\n\x03tag\x18\x03 \x01(\x0e\x32\x19.gossip.GossipMessage.Tag\x12)\n\talive_msg\x18\x05 \x01(\x0b\x32\x14.gossip.AliveMessageH\x00\x12,\n\x07mem_req\x18\x06 \x01(\x0b\x32\x19.gossip.MembershipRequestH\x00\x12-\n\x07mem_res\x18\x07 \x01(\x0b\x32\x1a.gossip.MembershipResponseH\x00\x12\'\n\x08\x64\x61ta_msg\x18\x08 \x01(\x0b\x32\x13.gossip.DataMessageH\x00\x12$\n\x05hello\x18\t \x01(\x0b\x32\x13.gossip.GossipHelloH\x00\x12&\n\x08\x64\x61ta_dig\x18\n \x01(\x0b\x32\x12.gossip.DataDigestH\x00\x12\'\n\x08\x64\x61ta_req\x18\x0b \x01(\x0b\x32\x13.gossip.DataRequestH\x00\x12)\n\x0b\x64\x61ta_update\x18\x0c \x01(\x0b\x32\x12.gossip.DataUpdateH\x00\x12\x1e\n\x05\x65mpty\x18\r \x01(\x0b\x32\r.gossip.EmptyH\x00\x12%\n\x04\x63onn\x18\x0e \x01(\x0b\x32\x15.gossip.ConnEstablishH\x00\x12\'\n\nstate_info\x18\x0f \x01(\x0b\x32\x11.gossip.StateInfoH\x00\x12\x33\n\x0estate_snapshot\x18\x10 \x01(\x0b\x32\x19.gossip.StateInfoSnapshotH\x00\x12;\n\x13state_info_pull_req\x18\x11 \x01(\x0b\x32\x1c.gossip.StateInfoPullRequestH\x00\x12\x33\n\rstate_request\x18\x12 \x01(\x0b\x32\x1a.gossip.RemoteStateRequestH\x00\x12\x35\n\x0estate_response\x18\x13 \x01(\x0b\x32\x1b.gossip.RemoteStateResponseH\x00\x12\x33\n\x0eleadership_msg\x18\x14 \x01(\x0b\x32\x19.gossip.LeadershipMessageH\x00\x12-\n\rpeer_identity\x18\x15 \x01(\x0b\x32\x14.gossip.PeerIdentityH\x00\x12&\n\x03\x61\x63k\x18\x16 \x01(\x0b\x32\x17.gossip.AcknowledgementH\x00\x12\x32\n\nprivateReq\x18\x17 \x01(\x0b\x32\x1c.gossip.RemotePvtDataRequestH\x00\x12\x33\n\nprivateRes\x18\x18 \x01(\x0b\x32\x1d.gossip.RemotePvtDataResponseH\x00\x12\x32\n\x0cprivate_data\x18\x19 \x01(\x0b\x32\x1a.gossip.PrivateDataMessageH\x00\"_\n\x03Tag\x12\r\n\tUNDEFINED\x10\x00\x12\t\n\x05\x45MPTY\x10\x01\x12\x0c\n\x08ORG_ONLY\x10\x02\x12\r\n\tCHAN_ONLY\x10\x03\x12\x10\n\x0c\x43HAN_AND_ORG\x10\x04\x12\x0f\n\x0b\x43HAN_OR_ORG\x10\x05\x42\t\n\x07\x63ontent\"}\n\tStateInfo\x12#\n\ttimestamp\x18\x02 \x01(\x0b\x32\x10.gossip.PeerTime\x12\x0e\n\x06pki_id\x18\x03 \x01(\x0c\x12\x13\n\x0b\x63hannel_MAC\x18\x04 \x01(\x0c\x12&\n\nproperties\x18\x05 \x01(\x0b\x32\x12.gossip.Properties\"`\n\nProperties\x12\x15\n\rledger_height\x18\x01 \x01(\x04\x12\x14\n\x0cleft_channel\x18\x02 \x01(\x08\x12%\n\nchaincodes\x18\x03 \x03(\x0b\x32\x11.gossip.Chaincode\"7\n\x11StateInfoSnapshot\x12\"\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x10.gossip.Envelope\"+\n\x14StateInfoPullRequest\x12\x13\n\x0b\x63hannel_MAC\x18\x01 \x01(\x0c\"H\n\rConnEstablish\x12\x0e\n\x06pki_id\x18\x01 \x01(\x0c\x12\x10\n\x08identity\x18\x02 \x01(\x0c\x12\x15\n\rtls_cert_hash\x18\x03 \x01(\x0c\">\n\x0cPeerIdentity\x12\x0e\n\x06pki_id\x18\x01 \x01(\x0c\x12\x0c\n\x04\x63\x65rt\x18\x02 \x01(\x0c\x12\x10\n\x08metadata\x18\x03 \x01(\x0c\"T\n\x0b\x44\x61taRequest\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x0f\n\x07\x64igests\x18\x02 \x03(\x0c\x12%\n\x08msg_type\x18\x03 \x01(\x0e\x32\x13.gossip.PullMsgType\"U\n\x0bGossipHello\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x10\n\x08metadata\x18\x02 \x01(\x0c\x12%\n\x08msg_type\x18\x03 \x01(\x0e\x32\x13.gossip.PullMsgType\"b\n\nDataUpdate\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x1e\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x10.gossip.Envelope\x12%\n\x08msg_type\x18\x03 \x01(\x0e\x32\x13.gossip.PullMsgType\"S\n\nDataDigest\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x0f\n\x07\x64igests\x18\x02 \x03(\x0c\x12%\n\x08msg_type\x18\x03 \x01(\x0e\x32\x13.gossip.PullMsgType\"/\n\x0b\x44\x61taMessage\x12 \n\x07payload\x18\x01 \x01(\x0b\x32\x0f.gossip.Payload\"=\n\x12PrivateDataMessage\x12\'\n\x07payload\x18\x01 \x01(\x0b\x32\x16.gossip.PrivatePayload\">\n\x07Payload\x12\x0f\n\x07seq_num\x18\x01 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x14\n\x0cprivate_data\x18\x03 \x03(\x0c\"\xbb\x01\n\x0ePrivatePayload\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\r\n\x05tx_id\x18\x03 \x01(\t\x12\x15\n\rprivate_rwset\x18\x04 \x01(\x0c\x12\x1a\n\x12private_sim_height\x18\x05 \x01(\x04\x12;\n\x12\x63ollection_configs\x18\x06 \x01(\x0b\x32\x1f.protos.CollectionConfigPackage\"i\n\x0c\x41liveMessage\x12\"\n\nmembership\x18\x01 \x01(\x0b\x32\x0e.gossip.Member\x12#\n\ttimestamp\x18\x02 \x01(\x0b\x32\x10.gossip.PeerTime\x12\x10\n\x08identity\x18\x04 \x01(\x0c\"`\n\x11LeadershipMessage\x12\x0e\n\x06pki_id\x18\x01 \x01(\x0c\x12#\n\ttimestamp\x18\x02 \x01(\x0b\x32\x10.gossip.PeerTime\x12\x16\n\x0eis_declaration\x18\x03 \x01(\x08\",\n\x08PeerTime\x12\x0f\n\x07inc_num\x18\x01 \x01(\x04\x12\x0f\n\x07seq_num\x18\x02 \x01(\x04\"N\n\x11MembershipRequest\x12*\n\x10self_information\x18\x01 \x01(\x0b\x32\x10.gossip.Envelope\x12\r\n\x05known\x18\x02 \x03(\x0c\"U\n\x12MembershipResponse\x12\x1f\n\x05\x61live\x18\x01 \x03(\x0b\x32\x10.gossip.Envelope\x12\x1e\n\x04\x64\x65\x61\x64\x18\x02 \x03(\x0b\x32\x10.gossip.Envelope\"<\n\x06Member\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x10\n\x08metadata\x18\x02 \x01(\x0c\x12\x0e\n\x06pki_id\x18\x03 \x01(\x0c\"\x07\n\x05\x45mpty\"@\n\x12RemoteStateRequest\x12\x15\n\rstart_seq_num\x18\x01 \x01(\x04\x12\x13\n\x0b\x65nd_seq_num\x18\x02 \x01(\x04\"8\n\x13RemoteStateResponse\x12!\n\x08payloads\x18\x01 \x03(\x0b\x32\x0f.gossip.Payload\">\n\x14RemotePvtDataRequest\x12&\n\x07\x64igests\x18\x01 \x03(\x0b\x32\x15.gossip.PvtDataDigest\"n\n\rPvtDataDigest\x12\r\n\x05tx_id\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x12\n\ncollection\x18\x03 \x01(\t\x12\x11\n\tblock_seq\x18\x04 \x01(\x04\x12\x14\n\x0cseq_in_block\x18\x05 \x01(\x04\"A\n\x15RemotePvtDataResponse\x12(\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x16.gossip.PvtDataElement\"H\n\x0ePvtDataElement\x12%\n\x06\x64igest\x18\x01 \x01(\x0b\x32\x15.gossip.PvtDataDigest\x12\x0f\n\x07payload\x18\x02 \x03(\x0c\":\n\x0ePvtDataPayload\x12\x17\n\x0ftx_seq_in_block\x18\x01 \x01(\x04\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\" \n\x0f\x41\x63knowledgement\x12\r\n\x05\x65rror\x18\x01 \x01(\t\"<\n\tChaincode\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\x0c*=\n\x0bPullMsgType\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tBLOCK_MSG\x10\x01\x12\x10\n\x0cIDENTITY_MSG\x10\x02\x32\x66\n\x06Gossip\x12\x36\n\x0cGossipStream\x12\x10.gossip.Envelope\x1a\x10.gossip.Envelope(\x01\x30\x01\x12$\n\x04Ping\x12\r.gossip.Empty\x1a\r.gossip.EmptyBV\n$org.hyperledger.fabric.protos.gossipZ.github.com/hyperledger/fabric-protos-go/gossipb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gossip.message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$org.hyperledger.fabric.protos.gossipZ.github.com/hyperledger/fabric-protos-go/gossip'
  _PULLMSGTYPE._serialized_start=3698
  _PULLMSGTYPE._serialized_end=3759
  _ENVELOPE._serialized_start=55
  _ENVELOPE._serialized_end=150
  _SECRETENVELOPE._serialized_start=152
  _SECRETENVELOPE._serialized_end=204
  _SECRET._serialized_start=206
  _SECRET._serialized_end=253
  _GOSSIPMESSAGE._serialized_start=256
  _GOSSIPMESSAGE._serialized_end=1421
  _GOSSIPMESSAGE_TAG._serialized_start=1315
  _GOSSIPMESSAGE_TAG._serialized_end=1410
  _STATEINFO._serialized_start=1423
  _STATEINFO._serialized_end=1548
  _PROPERTIES._serialized_start=1550
  _PROPERTIES._serialized_end=1646
  _STATEINFOSNAPSHOT._serialized_start=1648
  _STATEINFOSNAPSHOT._serialized_end=1703
  _STATEINFOPULLREQUEST._serialized_start=1705
  _STATEINFOPULLREQUEST._serialized_end=1748
  _CONNESTABLISH._serialized_start=1750
  _CONNESTABLISH._serialized_end=1822
  _PEERIDENTITY._serialized_start=1824
  _PEERIDENTITY._serialized_end=1886
  _DATAREQUEST._serialized_start=1888
  _DATAREQUEST._serialized_end=1972
  _GOSSIPHELLO._serialized_start=1974
  _GOSSIPHELLO._serialized_end=2059
  _DATAUPDATE._serialized_start=2061
  _DATAUPDATE._serialized_end=2159
  _DATADIGEST._serialized_start=2161
  _DATADIGEST._serialized_end=2244
  _DATAMESSAGE._serialized_start=2246
  _DATAMESSAGE._serialized_end=2293
  _PRIVATEDATAMESSAGE._serialized_start=2295
  _PRIVATEDATAMESSAGE._serialized_end=2356
  _PAYLOAD._serialized_start=2358
  _PAYLOAD._serialized_end=2420
  _PRIVATEPAYLOAD._serialized_start=2423
  _PRIVATEPAYLOAD._serialized_end=2610
  _ALIVEMESSAGE._serialized_start=2612
  _ALIVEMESSAGE._serialized_end=2717
  _LEADERSHIPMESSAGE._serialized_start=2719
  _LEADERSHIPMESSAGE._serialized_end=2815
  _PEERTIME._serialized_start=2817
  _PEERTIME._serialized_end=2861
  _MEMBERSHIPREQUEST._serialized_start=2863
  _MEMBERSHIPREQUEST._serialized_end=2941
  _MEMBERSHIPRESPONSE._serialized_start=2943
  _MEMBERSHIPRESPONSE._serialized_end=3028
  _MEMBER._serialized_start=3030
  _MEMBER._serialized_end=3090
  _EMPTY._serialized_start=3092
  _EMPTY._serialized_end=3099
  _REMOTESTATEREQUEST._serialized_start=3101
  _REMOTESTATEREQUEST._serialized_end=3165
  _REMOTESTATERESPONSE._serialized_start=3167
  _REMOTESTATERESPONSE._serialized_end=3223
  _REMOTEPVTDATAREQUEST._serialized_start=3225
  _REMOTEPVTDATAREQUEST._serialized_end=3287
  _PVTDATADIGEST._serialized_start=3289
  _PVTDATADIGEST._serialized_end=3399
  _REMOTEPVTDATARESPONSE._serialized_start=3401
  _REMOTEPVTDATARESPONSE._serialized_end=3466
  _PVTDATAELEMENT._serialized_start=3468
  _PVTDATAELEMENT._serialized_end=3540
  _PVTDATAPAYLOAD._serialized_start=3542
  _PVTDATAPAYLOAD._serialized_end=3600
  _ACKNOWLEDGEMENT._serialized_start=3602
  _ACKNOWLEDGEMENT._serialized_end=3634
  _CHAINCODE._serialized_start=3636
  _CHAINCODE._serialized_end=3696
  _GOSSIP._serialized_start=3761
  _GOSSIP._serialized_end=3863
# @@protoc_insertion_point(module_scope)
