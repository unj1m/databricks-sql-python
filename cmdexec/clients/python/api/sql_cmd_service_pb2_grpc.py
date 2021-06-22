# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cmdexec.clients.python.api import messages_pb2 as cmdexec_dot_api_dot_proto_dot_messages__pb2


class SqlCommandServiceStub(object):
    """
    gRPC service for the SQL command execution server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OpenSession = channel.unary_unary(
            '/com.databricks.cmdexec.SqlCommandService/OpenSession',
            request_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.OpenSessionRequest.
            SerializeToString,
            response_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.OpenSessionResponse.
            FromString,
        )
        self.CloseSession = channel.unary_unary(
            '/com.databricks.cmdexec.SqlCommandService/CloseSession',
            request_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseSessionRequest.
            SerializeToString,
            response_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseSessionResponse.
            FromString,
        )
        self.GetSessionInfo = channel.unary_unary(
            '/com.databricks.cmdexec.SqlCommandService/GetSessionInfo',
            request_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.GetSessionInfoRequest.
            SerializeToString,
            response_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.
            GetSessionInfoResponse.FromString,
        )
        self.ExecuteCommand = channel.unary_unary(
            '/com.databricks.cmdexec.SqlCommandService/ExecuteCommand',
            request_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.ExecuteCommandRequest.
            SerializeToString,
            response_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.
            ExecuteCommandResponse.FromString,
        )
        self.GetCommandStatus = channel.unary_unary(
            '/com.databricks.cmdexec.SqlCommandService/GetCommandStatus',
            request_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.GetCommandStatusRequest.
            SerializeToString,
            response_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.
            GetCommandStatusResponse.FromString,
        )
        self.FetchCommandResults = channel.unary_unary(
            '/com.databricks.cmdexec.SqlCommandService/FetchCommandResults',
            request_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.
            FetchCommandResultsRequest.SerializeToString,
            response_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.
            FetchCommandResultsResponse.FromString,
        )
        self.CloseCommand = channel.unary_unary(
            '/com.databricks.cmdexec.SqlCommandService/CloseCommand',
            request_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseCommandRequest.
            SerializeToString,
            response_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseCommandResponse.
            FromString,
        )


class SqlCommandServiceServicer(object):
    """
    gRPC service for the SQL command execution server
    """

    def OpenSession(self, request, context):
        """
        Opens a new session using the provided ID or generates a new one.
        Returns the session ID and any requested info
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseSession(self, request, context):
        """Closes the requested session, cancels any active commands, and frees resources 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSessionInfo(self, request, context):
        """Returns the requested session info values 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteCommand(self, request, context):
        """
        Submits a new command to be executed asynchronously. Creates a new session if the session ID
        is not provided, which will be automatically closed when the command is closed.
        Returns the new command ID and command status. It also waits up to a specified amount of time
        (default 5 seconds) for the command to complete. Returns the results if the command
        completes within that time
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCommandStatus(self, request, context):
        """Retrieves the status of the requested command 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchCommandResults(self, request, context):
        """
        Fetches command results and metadata from a specified offset. Throws an error if the
        command state is not SUCCESS and returns empty results when there are no rows to return
        or the requested offset is out of bounds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseCommand(self, request, context):
        """Closes the requested command, cancels active commands, and frees associated resources 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SqlCommandServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'OpenSession': grpc.unary_unary_rpc_method_handler(
            servicer.OpenSession,
            request_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.OpenSessionRequest.
            FromString,
            response_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.OpenSessionResponse.
            SerializeToString,
        ),
        'CloseSession': grpc.unary_unary_rpc_method_handler(
            servicer.CloseSession,
            request_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseSessionRequest.
            FromString,
            response_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseSessionResponse.
            SerializeToString,
        ),
        'GetSessionInfo': grpc.unary_unary_rpc_method_handler(
            servicer.GetSessionInfo,
            request_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.GetSessionInfoRequest.
            FromString,
            response_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.GetSessionInfoResponse.
            SerializeToString,
        ),
        'ExecuteCommand': grpc.unary_unary_rpc_method_handler(
            servicer.ExecuteCommand,
            request_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.ExecuteCommandRequest.
            FromString,
            response_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.ExecuteCommandResponse.
            SerializeToString,
        ),
        'GetCommandStatus': grpc.unary_unary_rpc_method_handler(
            servicer.GetCommandStatus,
            request_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.
            GetCommandStatusRequest.FromString,
            response_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.
            GetCommandStatusResponse.SerializeToString,
        ),
        'FetchCommandResults': grpc.unary_unary_rpc_method_handler(
            servicer.FetchCommandResults,
            request_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.
            FetchCommandResultsRequest.FromString,
            response_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.
            FetchCommandResultsResponse.SerializeToString,
        ),
        'CloseCommand': grpc.unary_unary_rpc_method_handler(
            servicer.CloseCommand,
            request_deserializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseCommandRequest.
            FromString,
            response_serializer=cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseCommandResponse.
            SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'com.databricks.cmdexec.SqlCommandService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler, ))


# This class is part of an EXPERIMENTAL API.
class SqlCommandService(object):
    """
    gRPC service for the SQL command execution server
    """

    @staticmethod
    def OpenSession(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.cmdexec.SqlCommandService/OpenSession',
            cmdexec_dot_api_dot_proto_dot_messages__pb2.OpenSessionRequest.SerializeToString,
            cmdexec_dot_api_dot_proto_dot_messages__pb2.OpenSessionResponse.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def CloseSession(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.cmdexec.SqlCommandService/CloseSession',
            cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseSessionRequest.SerializeToString,
            cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseSessionResponse.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def GetSessionInfo(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.cmdexec.SqlCommandService/GetSessionInfo',
            cmdexec_dot_api_dot_proto_dot_messages__pb2.GetSessionInfoRequest.SerializeToString,
            cmdexec_dot_api_dot_proto_dot_messages__pb2.GetSessionInfoResponse.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def ExecuteCommand(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.cmdexec.SqlCommandService/ExecuteCommand',
            cmdexec_dot_api_dot_proto_dot_messages__pb2.ExecuteCommandRequest.SerializeToString,
            cmdexec_dot_api_dot_proto_dot_messages__pb2.ExecuteCommandResponse.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def GetCommandStatus(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.cmdexec.SqlCommandService/GetCommandStatus',
            cmdexec_dot_api_dot_proto_dot_messages__pb2.GetCommandStatusRequest.SerializeToString,
            cmdexec_dot_api_dot_proto_dot_messages__pb2.GetCommandStatusResponse.FromString,
            options, channel_credentials, insecure, call_credentials, compression, wait_for_ready,
            timeout, metadata)

    @staticmethod
    def FetchCommandResults(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.cmdexec.SqlCommandService/FetchCommandResults',
            cmdexec_dot_api_dot_proto_dot_messages__pb2.FetchCommandResultsRequest.SerializeToString,
            cmdexec_dot_api_dot_proto_dot_messages__pb2.FetchCommandResultsResponse.FromString,
            options, channel_credentials, insecure, call_credentials, compression, wait_for_ready,
            timeout, metadata)

    @staticmethod
    def CloseCommand(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/com.databricks.cmdexec.SqlCommandService/CloseCommand',
            cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseCommandRequest.SerializeToString,
            cmdexec_dot_api_dot_proto_dot_messages__pb2.CloseCommandResponse.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)