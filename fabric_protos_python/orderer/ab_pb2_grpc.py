# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fabric_protos_python.common import common_pb2 as common_dot_common__pb2
from fabric_protos_python.orderer import ab_pb2 as orderer_dot_ab__pb2


class AtomicBroadcastStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Broadcast = channel.stream_stream(
                '/orderer.AtomicBroadcast/Broadcast',
                request_serializer=common_dot_common__pb2.Envelope.SerializeToString,
                response_deserializer=orderer_dot_ab__pb2.BroadcastResponse.FromString,
                )
        self.Deliver = channel.stream_stream(
                '/orderer.AtomicBroadcast/Deliver',
                request_serializer=common_dot_common__pb2.Envelope.SerializeToString,
                response_deserializer=orderer_dot_ab__pb2.DeliverResponse.FromString,
                )


class AtomicBroadcastServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Broadcast(self, request_iterator, context):
        """broadcast receives a reply of Acknowledgement for each common.Envelope in order, indicating success or type of failure
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deliver(self, request_iterator, context):
        """deliver first requires an Envelope of type DELIVER_SEEK_INFO with Payload data as a mashaled SeekInfo message, then a stream of block replies is received.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AtomicBroadcastServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Broadcast': grpc.stream_stream_rpc_method_handler(
                    servicer.Broadcast,
                    request_deserializer=common_dot_common__pb2.Envelope.FromString,
                    response_serializer=orderer_dot_ab__pb2.BroadcastResponse.SerializeToString,
            ),
            'Deliver': grpc.stream_stream_rpc_method_handler(
                    servicer.Deliver,
                    request_deserializer=common_dot_common__pb2.Envelope.FromString,
                    response_serializer=orderer_dot_ab__pb2.DeliverResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'orderer.AtomicBroadcast', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AtomicBroadcast(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Broadcast(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/orderer.AtomicBroadcast/Broadcast',
            common_dot_common__pb2.Envelope.SerializeToString,
            orderer_dot_ab__pb2.BroadcastResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deliver(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/orderer.AtomicBroadcast/Deliver',
            common_dot_common__pb2.Envelope.SerializeToString,
            orderer_dot_ab__pb2.DeliverResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
