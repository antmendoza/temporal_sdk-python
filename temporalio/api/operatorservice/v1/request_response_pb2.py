# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/operatorservice/v1/request_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from temporalio.api.cluster.v1 import (
    message_pb2 as temporal_dot_api_dot_cluster_dot_v1_dot_message__pb2,
)
from temporalio.api.common.v1 import (
    message_pb2 as temporal_dot_api_dot_common_dot_v1_dot_message__pb2,
)
from temporalio.api.dependencies.gogoproto import (
    gogo_pb2 as dependencies_dot_gogoproto_dot_gogo__pb2,
)
from temporalio.api.enums.v1 import (
    cluster_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_cluster__pb2,
)
from temporalio.api.enums.v1 import (
    common_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_common__pb2,
)
from temporalio.api.version.v1 import (
    message_pb2 as temporal_dot_api_dot_version_dot_v1_dot_message__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n6temporal/api/operatorservice/v1/request_response.proto\x12\x1ftemporal.api.operatorservice.v1\x1a!dependencies/gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a%temporal/api/cluster/v1/message.proto\x1a$temporal/api/common/v1/message.proto\x1a#temporal/api/enums/v1/cluster.proto\x1a"temporal/api/enums/v1/common.proto\x1a%temporal/api/version/v1/message.proto"\xec\x01\n\x1a\x41\x64\x64SearchAttributesRequest\x12l\n\x11search_attributes\x18\x01 \x03(\x0b\x32Q.temporal.api.operatorservice.v1.AddSearchAttributesRequest.SearchAttributesEntry\x1a`\n\x15SearchAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0e\x32\'.temporal.api.enums.v1.IndexedValueType:\x02\x38\x01"\x1d\n\x1b\x41\x64\x64SearchAttributesResponse":\n\x1dRemoveSearchAttributesRequest\x12\x19\n\x11search_attributes\x18\x01 \x03(\t" \n\x1eRemoveSearchAttributesResponse"\x1d\n\x1bListSearchAttributesRequest"\xe2\x04\n\x1cListSearchAttributesResponse\x12n\n\x11\x63ustom_attributes\x18\x01 \x03(\x0b\x32S.temporal.api.operatorservice.v1.ListSearchAttributesResponse.CustomAttributesEntry\x12n\n\x11system_attributes\x18\x02 \x03(\x0b\x32S.temporal.api.operatorservice.v1.ListSearchAttributesResponse.SystemAttributesEntry\x12h\n\x0estorage_schema\x18\x03 \x03(\x0b\x32P.temporal.api.operatorservice.v1.ListSearchAttributesResponse.StorageSchemaEntry\x1a`\n\x15\x43ustomAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0e\x32\'.temporal.api.enums.v1.IndexedValueType:\x02\x38\x01\x1a`\n\x15SystemAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0e\x32\'.temporal.api.enums.v1.IndexedValueType:\x02\x38\x01\x1a\x34\n\x12StorageSchemaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"+\n\x16\x44\x65leteNamespaceRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t"4\n\x17\x44\x65leteNamespaceResponse\x12\x19\n\x11\x64\x65leted_namespace\x18\x01 \x01(\t"z\n\x1e\x44\x65leteWorkflowExecutionRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x45\n\x12workflow_execution\x18\x02 \x01(\x0b\x32).temporal.api.common.v1.WorkflowExecution"!\n\x1f\x44\x65leteWorkflowExecutionResponse"e\n\x1f\x41\x64\x64OrUpdateRemoteClusterRequest\x12\x18\n\x10\x66rontend_address\x18\x01 \x01(\t\x12(\n enable_remote_cluster_connection\x18\x02 \x01(\x08""\n AddOrUpdateRemoteClusterResponse"2\n\x1aRemoveRemoteClusterRequest\x12\x14\n\x0c\x63luster_name\x18\x01 \x01(\t"\x1d\n\x1bRemoveRemoteClusterResponse".\n\x16\x44\x65scribeClusterRequest\x12\x14\n\x0c\x63luster_name\x18\x01 \x01(\t"\xba\x04\n\x17\x44\x65scribeClusterResponse\x12i\n\x11supported_clients\x18\x01 \x03(\x0b\x32N.temporal.api.operatorservice.v1.DescribeClusterResponse.SupportedClientsEntry\x12\x16\n\x0eserver_version\x18\x02 \x01(\t\x12@\n\x0fmembership_info\x18\x03 \x01(\x0b\x32\'.temporal.api.cluster.v1.MembershipInfo\x12\x12\n\ncluster_id\x18\x04 \x01(\t\x12\x14\n\x0c\x63luster_name\x18\x05 \x01(\t\x12\x1b\n\x13history_shard_count\x18\x06 \x01(\x05\x12\x19\n\x11persistence_store\x18\x07 \x01(\t\x12\x18\n\x10visibility_store\x18\x08 \x01(\t\x12:\n\x0cversion_info\x18\t \x01(\x0b\x32$.temporal.api.version.v1.VersionInfo\x12"\n\x1a\x66\x61ilover_version_increment\x18\n \x01(\x03\x12 \n\x18initial_failover_version\x18\x0b \x01(\x03\x12#\n\x1bis_global_namespace_enabled\x18\x0c \x01(\x08\x1a\x37\n\x15SupportedClientsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"A\n\x13ListClustersRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\x0c"k\n\x14ListClustersResponse\x12:\n\x08\x63lusters\x18\x01 \x03(\x0b\x32(.temporal.api.cluster.v1.ClusterMetadata\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\x0c"\xab\x02\n\x19ListClusterMembersRequest\x12>\n\x15last_heartbeat_within\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\x98\xdf\x1f\x01\x12\x13\n\x0brpc_address\x18\x02 \x01(\t\x12\x0f\n\x07host_id\x18\x03 \x01(\t\x12\x36\n\x04role\x18\x04 \x01(\x0e\x32(.temporal.api.enums.v1.ClusterMemberRole\x12\x44\n\x1asession_started_after_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12\x17\n\x0fnext_page_token\x18\x07 \x01(\x0c"u\n\x1aListClusterMembersResponse\x12>\n\x0e\x61\x63tive_members\x18\x01 \x03(\x0b\x32&.temporal.api.cluster.v1.ClusterMember\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\x0c\x42\xba\x01\n"io.temporal.api.operatorservice.v1B\x14RequestResponseProtoP\x01Z5go.temporal.io/api/operatorservice/v1;operatorservice\xaa\x02\x1fTemporal.Api.OperatorService.V1\xea\x02"Temporal::Api::OperatorService::V1b\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "temporal.api.operatorservice.v1.request_response_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n"io.temporal.api.operatorservice.v1B\024RequestResponseProtoP\001Z5go.temporal.io/api/operatorservice/v1;operatorservice\252\002\037Temporal.Api.OperatorService.V1\352\002"Temporal::Api::OperatorService::V1'
    _ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY._options = None
    _ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY._serialized_options = b"8\001"
    _LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY._options = None
    _LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY._serialized_options = b"8\001"
    _LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY._options = None
    _LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY._serialized_options = b"8\001"
    _LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY._options = None
    _LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY._serialized_options = b"8\001"
    _DESCRIBECLUSTERRESPONSE_SUPPORTEDCLIENTSENTRY._options = None
    _DESCRIBECLUSTERRESPONSE_SUPPORTEDCLIENTSENTRY._serialized_options = b"8\001"
    _LISTCLUSTERMEMBERSREQUEST.fields_by_name["last_heartbeat_within"]._options = None
    _LISTCLUSTERMEMBERSREQUEST.fields_by_name[
        "last_heartbeat_within"
    ]._serialized_options = b"\230\337\037\001"
    _LISTCLUSTERMEMBERSREQUEST.fields_by_name[
        "session_started_after_time"
    ]._options = None
    _LISTCLUSTERMEMBERSREQUEST.fields_by_name[
        "session_started_after_time"
    ]._serialized_options = b"\220\337\037\001"
    _ADDSEARCHATTRIBUTESREQUEST._serialized_start = 381
    _ADDSEARCHATTRIBUTESREQUEST._serialized_end = 617
    _ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY._serialized_start = 521
    _ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY._serialized_end = 617
    _ADDSEARCHATTRIBUTESRESPONSE._serialized_start = 619
    _ADDSEARCHATTRIBUTESRESPONSE._serialized_end = 648
    _REMOVESEARCHATTRIBUTESREQUEST._serialized_start = 650
    _REMOVESEARCHATTRIBUTESREQUEST._serialized_end = 708
    _REMOVESEARCHATTRIBUTESRESPONSE._serialized_start = 710
    _REMOVESEARCHATTRIBUTESRESPONSE._serialized_end = 742
    _LISTSEARCHATTRIBUTESREQUEST._serialized_start = 744
    _LISTSEARCHATTRIBUTESREQUEST._serialized_end = 773
    _LISTSEARCHATTRIBUTESRESPONSE._serialized_start = 776
    _LISTSEARCHATTRIBUTESRESPONSE._serialized_end = 1386
    _LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY._serialized_start = 1138
    _LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY._serialized_end = 1234
    _LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY._serialized_start = 1236
    _LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY._serialized_end = 1332
    _LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY._serialized_start = 1334
    _LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY._serialized_end = 1386
    _DELETENAMESPACEREQUEST._serialized_start = 1388
    _DELETENAMESPACEREQUEST._serialized_end = 1431
    _DELETENAMESPACERESPONSE._serialized_start = 1433
    _DELETENAMESPACERESPONSE._serialized_end = 1485
    _DELETEWORKFLOWEXECUTIONREQUEST._serialized_start = 1487
    _DELETEWORKFLOWEXECUTIONREQUEST._serialized_end = 1609
    _DELETEWORKFLOWEXECUTIONRESPONSE._serialized_start = 1611
    _DELETEWORKFLOWEXECUTIONRESPONSE._serialized_end = 1644
    _ADDORUPDATEREMOTECLUSTERREQUEST._serialized_start = 1646
    _ADDORUPDATEREMOTECLUSTERREQUEST._serialized_end = 1747
    _ADDORUPDATEREMOTECLUSTERRESPONSE._serialized_start = 1749
    _ADDORUPDATEREMOTECLUSTERRESPONSE._serialized_end = 1783
    _REMOVEREMOTECLUSTERREQUEST._serialized_start = 1785
    _REMOVEREMOTECLUSTERREQUEST._serialized_end = 1835
    _REMOVEREMOTECLUSTERRESPONSE._serialized_start = 1837
    _REMOVEREMOTECLUSTERRESPONSE._serialized_end = 1866
    _DESCRIBECLUSTERREQUEST._serialized_start = 1868
    _DESCRIBECLUSTERREQUEST._serialized_end = 1914
    _DESCRIBECLUSTERRESPONSE._serialized_start = 1917
    _DESCRIBECLUSTERRESPONSE._serialized_end = 2487
    _DESCRIBECLUSTERRESPONSE_SUPPORTEDCLIENTSENTRY._serialized_start = 2432
    _DESCRIBECLUSTERRESPONSE_SUPPORTEDCLIENTSENTRY._serialized_end = 2487
    _LISTCLUSTERSREQUEST._serialized_start = 2489
    _LISTCLUSTERSREQUEST._serialized_end = 2554
    _LISTCLUSTERSRESPONSE._serialized_start = 2556
    _LISTCLUSTERSRESPONSE._serialized_end = 2663
    _LISTCLUSTERMEMBERSREQUEST._serialized_start = 2666
    _LISTCLUSTERMEMBERSREQUEST._serialized_end = 2965
    _LISTCLUSTERMEMBERSRESPONSE._serialized_start = 2967
    _LISTCLUSTERMEMBERSRESPONSE._serialized_end = 3084
# @@protoc_insertion_point(module_scope)
