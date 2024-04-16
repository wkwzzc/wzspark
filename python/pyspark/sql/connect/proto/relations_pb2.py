#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/relations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyspark.sql.connect.proto import expressions_pb2 as spark_dot_connect_dot_expressions__pb2
from pyspark.sql.connect.proto import types_pb2 as spark_dot_connect_dot_types__pb2
from pyspark.sql.connect.proto import catalog_pb2 as spark_dot_connect_dot_catalog__pb2
from pyspark.sql.connect.proto import common_pb2 as spark_dot_connect_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1dspark/connect/relations.proto\x12\rspark.connect\x1a\x19google/protobuf/any.proto\x1a\x1fspark/connect/expressions.proto\x1a\x19spark/connect/types.proto\x1a\x1bspark/connect/catalog.proto\x1a\x1aspark/connect/common.proto"\xe9\x1a\n\x08Relation\x12\x35\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1d.spark.connect.RelationCommonR\x06\x63ommon\x12)\n\x04read\x18\x02 \x01(\x0b\x32\x13.spark.connect.ReadH\x00R\x04read\x12\x32\n\x07project\x18\x03 \x01(\x0b\x32\x16.spark.connect.ProjectH\x00R\x07project\x12/\n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x15.spark.connect.FilterH\x00R\x06\x66ilter\x12)\n\x04join\x18\x05 \x01(\x0b\x32\x13.spark.connect.JoinH\x00R\x04join\x12\x34\n\x06set_op\x18\x06 \x01(\x0b\x32\x1b.spark.connect.SetOperationH\x00R\x05setOp\x12)\n\x04sort\x18\x07 \x01(\x0b\x32\x13.spark.connect.SortH\x00R\x04sort\x12,\n\x05limit\x18\x08 \x01(\x0b\x32\x14.spark.connect.LimitH\x00R\x05limit\x12\x38\n\taggregate\x18\t \x01(\x0b\x32\x18.spark.connect.AggregateH\x00R\taggregate\x12&\n\x03sql\x18\n \x01(\x0b\x32\x12.spark.connect.SQLH\x00R\x03sql\x12\x45\n\x0elocal_relation\x18\x0b \x01(\x0b\x32\x1c.spark.connect.LocalRelationH\x00R\rlocalRelation\x12/\n\x06sample\x18\x0c \x01(\x0b\x32\x15.spark.connect.SampleH\x00R\x06sample\x12/\n\x06offset\x18\r \x01(\x0b\x32\x15.spark.connect.OffsetH\x00R\x06offset\x12>\n\x0b\x64\x65\x64uplicate\x18\x0e \x01(\x0b\x32\x1a.spark.connect.DeduplicateH\x00R\x0b\x64\x65\x64uplicate\x12,\n\x05range\x18\x0f \x01(\x0b\x32\x14.spark.connect.RangeH\x00R\x05range\x12\x45\n\x0esubquery_alias\x18\x10 \x01(\x0b\x32\x1c.spark.connect.SubqueryAliasH\x00R\rsubqueryAlias\x12>\n\x0brepartition\x18\x11 \x01(\x0b\x32\x1a.spark.connect.RepartitionH\x00R\x0brepartition\x12*\n\x05to_df\x18\x12 \x01(\x0b\x32\x13.spark.connect.ToDFH\x00R\x04toDf\x12U\n\x14with_columns_renamed\x18\x13 \x01(\x0b\x32!.spark.connect.WithColumnsRenamedH\x00R\x12withColumnsRenamed\x12<\n\x0bshow_string\x18\x14 \x01(\x0b\x32\x19.spark.connect.ShowStringH\x00R\nshowString\x12)\n\x04\x64rop\x18\x15 \x01(\x0b\x32\x13.spark.connect.DropH\x00R\x04\x64rop\x12)\n\x04tail\x18\x16 \x01(\x0b\x32\x13.spark.connect.TailH\x00R\x04tail\x12?\n\x0cwith_columns\x18\x17 \x01(\x0b\x32\x1a.spark.connect.WithColumnsH\x00R\x0bwithColumns\x12)\n\x04hint\x18\x18 \x01(\x0b\x32\x13.spark.connect.HintH\x00R\x04hint\x12\x32\n\x07unpivot\x18\x19 \x01(\x0b\x32\x16.spark.connect.UnpivotH\x00R\x07unpivot\x12\x36\n\tto_schema\x18\x1a \x01(\x0b\x32\x17.spark.connect.ToSchemaH\x00R\x08toSchema\x12\x64\n\x19repartition_by_expression\x18\x1b \x01(\x0b\x32&.spark.connect.RepartitionByExpressionH\x00R\x17repartitionByExpression\x12\x45\n\x0emap_partitions\x18\x1c \x01(\x0b\x32\x1c.spark.connect.MapPartitionsH\x00R\rmapPartitions\x12H\n\x0f\x63ollect_metrics\x18\x1d \x01(\x0b\x32\x1d.spark.connect.CollectMetricsH\x00R\x0e\x63ollectMetrics\x12,\n\x05parse\x18\x1e \x01(\x0b\x32\x14.spark.connect.ParseH\x00R\x05parse\x12\x36\n\tgroup_map\x18\x1f \x01(\x0b\x32\x17.spark.connect.GroupMapH\x00R\x08groupMap\x12=\n\x0c\x63o_group_map\x18  \x01(\x0b\x32\x19.spark.connect.CoGroupMapH\x00R\ncoGroupMap\x12\x45\n\x0ewith_watermark\x18! \x01(\x0b\x32\x1c.spark.connect.WithWatermarkH\x00R\rwithWatermark\x12\x63\n\x1a\x61pply_in_pandas_with_state\x18" \x01(\x0b\x32%.spark.connect.ApplyInPandasWithStateH\x00R\x16\x61pplyInPandasWithState\x12<\n\x0bhtml_string\x18# \x01(\x0b\x32\x19.spark.connect.HtmlStringH\x00R\nhtmlString\x12X\n\x15\x63\x61\x63hed_local_relation\x18$ \x01(\x0b\x32".spark.connect.CachedLocalRelationH\x00R\x13\x63\x61\x63hedLocalRelation\x12[\n\x16\x63\x61\x63hed_remote_relation\x18% \x01(\x0b\x32#.spark.connect.CachedRemoteRelationH\x00R\x14\x63\x61\x63hedRemoteRelation\x12\x8e\x01\n)common_inline_user_defined_table_function\x18& \x01(\x0b\x32\x33.spark.connect.CommonInlineUserDefinedTableFunctionH\x00R$commonInlineUserDefinedTableFunction\x12\x37\n\nas_of_join\x18\' \x01(\x0b\x32\x17.spark.connect.AsOfJoinH\x00R\x08\x61sOfJoin\x12\x85\x01\n&common_inline_user_defined_data_source\x18( \x01(\x0b\x32\x30.spark.connect.CommonInlineUserDefinedDataSourceH\x00R!commonInlineUserDefinedDataSource\x12\x45\n\x0ewith_relations\x18) \x01(\x0b\x32\x1c.spark.connect.WithRelationsH\x00R\rwithRelations\x12\x30\n\x07\x66ill_na\x18Z \x01(\x0b\x32\x15.spark.connect.NAFillH\x00R\x06\x66illNa\x12\x30\n\x07\x64rop_na\x18[ \x01(\x0b\x32\x15.spark.connect.NADropH\x00R\x06\x64ropNa\x12\x34\n\x07replace\x18\\ \x01(\x0b\x32\x18.spark.connect.NAReplaceH\x00R\x07replace\x12\x36\n\x07summary\x18\x64 \x01(\x0b\x32\x1a.spark.connect.StatSummaryH\x00R\x07summary\x12\x39\n\x08\x63rosstab\x18\x65 \x01(\x0b\x32\x1b.spark.connect.StatCrosstabH\x00R\x08\x63rosstab\x12\x39\n\x08\x64\x65scribe\x18\x66 \x01(\x0b\x32\x1b.spark.connect.StatDescribeH\x00R\x08\x64\x65scribe\x12*\n\x03\x63ov\x18g \x01(\x0b\x32\x16.spark.connect.StatCovH\x00R\x03\x63ov\x12-\n\x04\x63orr\x18h \x01(\x0b\x32\x17.spark.connect.StatCorrH\x00R\x04\x63orr\x12L\n\x0f\x61pprox_quantile\x18i \x01(\x0b\x32!.spark.connect.StatApproxQuantileH\x00R\x0e\x61pproxQuantile\x12=\n\nfreq_items\x18j \x01(\x0b\x32\x1c.spark.connect.StatFreqItemsH\x00R\tfreqItems\x12:\n\tsample_by\x18k \x01(\x0b\x32\x1b.spark.connect.StatSampleByH\x00R\x08sampleBy\x12\x33\n\x07\x63\x61talog\x18\xc8\x01 \x01(\x0b\x32\x16.spark.connect.CatalogH\x00R\x07\x63\x61talog\x12\x35\n\textension\x18\xe6\x07 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\textension\x12\x33\n\x07unknown\x18\xe7\x07 \x01(\x0b\x32\x16.spark.connect.UnknownH\x00R\x07unknownB\n\n\x08rel_type"\t\n\x07Unknown"[\n\x0eRelationCommon\x12\x1f\n\x0bsource_info\x18\x01 \x01(\tR\nsourceInfo\x12\x1c\n\x07plan_id\x18\x02 \x01(\x03H\x00R\x06planId\x88\x01\x01\x42\n\n\x08_plan_id"\xde\x03\n\x03SQL\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query\x12\x34\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x1c.spark.connect.SQL.ArgsEntryB\x02\x18\x01R\x04\x61rgs\x12@\n\x08pos_args\x18\x03 \x03(\x0b\x32!.spark.connect.Expression.LiteralB\x02\x18\x01R\x07posArgs\x12O\n\x0fnamed_arguments\x18\x04 \x03(\x0b\x32&.spark.connect.SQL.NamedArgumentsEntryR\x0enamedArguments\x12>\n\rpos_arguments\x18\x05 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x0cposArguments\x1aZ\n\tArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x05value:\x02\x38\x01\x1a\\\n\x13NamedArgumentsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12/\n\x05value\x18\x02 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x05value:\x02\x38\x01"u\n\rWithRelations\x12+\n\x04root\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x04root\x12\x37\n\nreferences\x18\x02 \x03(\x0b\x32\x17.spark.connect.RelationR\nreferences"\x97\x05\n\x04Read\x12\x41\n\x0bnamed_table\x18\x01 \x01(\x0b\x32\x1e.spark.connect.Read.NamedTableH\x00R\nnamedTable\x12\x41\n\x0b\x64\x61ta_source\x18\x02 \x01(\x0b\x32\x1e.spark.connect.Read.DataSourceH\x00R\ndataSource\x12!\n\x0cis_streaming\x18\x03 \x01(\x08R\x0bisStreaming\x1a\xc0\x01\n\nNamedTable\x12/\n\x13unparsed_identifier\x18\x01 \x01(\tR\x12unparsedIdentifier\x12\x45\n\x07options\x18\x02 \x03(\x0b\x32+.spark.connect.Read.NamedTable.OptionsEntryR\x07options\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x95\x02\n\nDataSource\x12\x1b\n\x06\x66ormat\x18\x01 \x01(\tH\x00R\x06\x66ormat\x88\x01\x01\x12\x1b\n\x06schema\x18\x02 \x01(\tH\x01R\x06schema\x88\x01\x01\x12\x45\n\x07options\x18\x03 \x03(\x0b\x32+.spark.connect.Read.DataSource.OptionsEntryR\x07options\x12\x14\n\x05paths\x18\x04 \x03(\tR\x05paths\x12\x1e\n\npredicates\x18\x05 \x03(\tR\npredicates\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\t\n\x07_formatB\t\n\x07_schemaB\x0b\n\tread_type"u\n\x07Project\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12;\n\x0b\x65xpressions\x18\x03 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x0b\x65xpressions"p\n\x06\x46ilter\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x37\n\tcondition\x18\x02 \x01(\x0b\x32\x19.spark.connect.ExpressionR\tcondition"\x95\x05\n\x04Join\x12+\n\x04left\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x04left\x12-\n\x05right\x18\x02 \x01(\x0b\x32\x17.spark.connect.RelationR\x05right\x12@\n\x0ejoin_condition\x18\x03 \x01(\x0b\x32\x19.spark.connect.ExpressionR\rjoinCondition\x12\x39\n\tjoin_type\x18\x04 \x01(\x0e\x32\x1c.spark.connect.Join.JoinTypeR\x08joinType\x12#\n\rusing_columns\x18\x05 \x03(\tR\x0cusingColumns\x12K\n\x0ejoin_data_type\x18\x06 \x01(\x0b\x32 .spark.connect.Join.JoinDataTypeH\x00R\x0cjoinDataType\x88\x01\x01\x1a\\\n\x0cJoinDataType\x12$\n\x0eis_left_struct\x18\x01 \x01(\x08R\x0cisLeftStruct\x12&\n\x0fis_right_struct\x18\x02 \x01(\x08R\risRightStruct"\xd0\x01\n\x08JoinType\x12\x19\n\x15JOIN_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fJOIN_TYPE_INNER\x10\x01\x12\x18\n\x14JOIN_TYPE_FULL_OUTER\x10\x02\x12\x18\n\x14JOIN_TYPE_LEFT_OUTER\x10\x03\x12\x19\n\x15JOIN_TYPE_RIGHT_OUTER\x10\x04\x12\x17\n\x13JOIN_TYPE_LEFT_ANTI\x10\x05\x12\x17\n\x13JOIN_TYPE_LEFT_SEMI\x10\x06\x12\x13\n\x0fJOIN_TYPE_CROSS\x10\x07\x42\x11\n\x0f_join_data_type"\xdf\x03\n\x0cSetOperation\x12\x36\n\nleft_input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\tleftInput\x12\x38\n\x0bright_input\x18\x02 \x01(\x0b\x32\x17.spark.connect.RelationR\nrightInput\x12\x45\n\x0bset_op_type\x18\x03 \x01(\x0e\x32%.spark.connect.SetOperation.SetOpTypeR\tsetOpType\x12\x1a\n\x06is_all\x18\x04 \x01(\x08H\x00R\x05isAll\x88\x01\x01\x12\x1c\n\x07\x62y_name\x18\x05 \x01(\x08H\x01R\x06\x62yName\x88\x01\x01\x12\x37\n\x15\x61llow_missing_columns\x18\x06 \x01(\x08H\x02R\x13\x61llowMissingColumns\x88\x01\x01"r\n\tSetOpType\x12\x1b\n\x17SET_OP_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15SET_OP_TYPE_INTERSECT\x10\x01\x12\x15\n\x11SET_OP_TYPE_UNION\x10\x02\x12\x16\n\x12SET_OP_TYPE_EXCEPT\x10\x03\x42\t\n\x07_is_allB\n\n\x08_by_nameB\x18\n\x16_allow_missing_columns"L\n\x05Limit\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit"O\n\x06Offset\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x16\n\x06offset\x18\x02 \x01(\x05R\x06offset"K\n\x04Tail\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit"\xfe\x05\n\tAggregate\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x41\n\ngroup_type\x18\x02 \x01(\x0e\x32".spark.connect.Aggregate.GroupTypeR\tgroupType\x12L\n\x14grouping_expressions\x18\x03 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x13groupingExpressions\x12N\n\x15\x61ggregate_expressions\x18\x04 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x14\x61ggregateExpressions\x12\x34\n\x05pivot\x18\x05 \x01(\x0b\x32\x1e.spark.connect.Aggregate.PivotR\x05pivot\x12J\n\rgrouping_sets\x18\x06 \x03(\x0b\x32%.spark.connect.Aggregate.GroupingSetsR\x0cgroupingSets\x1ao\n\x05Pivot\x12+\n\x03\x63ol\x18\x01 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x03\x63ol\x12\x39\n\x06values\x18\x02 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06values\x1aL\n\x0cGroupingSets\x12<\n\x0cgrouping_set\x18\x01 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x0bgroupingSet"\x9f\x01\n\tGroupType\x12\x1a\n\x16GROUP_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12GROUP_TYPE_GROUPBY\x10\x01\x12\x15\n\x11GROUP_TYPE_ROLLUP\x10\x02\x12\x13\n\x0fGROUP_TYPE_CUBE\x10\x03\x12\x14\n\x10GROUP_TYPE_PIVOT\x10\x04\x12\x1c\n\x18GROUP_TYPE_GROUPING_SETS\x10\x05"\xa0\x01\n\x04Sort\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x39\n\x05order\x18\x02 \x03(\x0b\x32#.spark.connect.Expression.SortOrderR\x05order\x12 \n\tis_global\x18\x03 \x01(\x08H\x00R\x08isGlobal\x88\x01\x01\x42\x0c\n\n_is_global"\x8d\x01\n\x04\x44rop\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x33\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x07\x63olumns\x12!\n\x0c\x63olumn_names\x18\x03 \x03(\tR\x0b\x63olumnNames"\xf0\x01\n\x0b\x44\x65\x64uplicate\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12!\n\x0c\x63olumn_names\x18\x02 \x03(\tR\x0b\x63olumnNames\x12\x32\n\x13\x61ll_columns_as_keys\x18\x03 \x01(\x08H\x00R\x10\x61llColumnsAsKeys\x88\x01\x01\x12.\n\x10within_watermark\x18\x04 \x01(\x08H\x01R\x0fwithinWatermark\x88\x01\x01\x42\x16\n\x14_all_columns_as_keysB\x13\n\x11_within_watermark"Y\n\rLocalRelation\x12\x17\n\x04\x64\x61ta\x18\x01 \x01(\x0cH\x00R\x04\x64\x61ta\x88\x01\x01\x12\x1b\n\x06schema\x18\x02 \x01(\tH\x01R\x06schema\x88\x01\x01\x42\x07\n\x05_dataB\t\n\x07_schema"H\n\x13\x43\x61\x63hedLocalRelation\x12\x12\n\x04hash\x18\x03 \x01(\tR\x04hashJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03R\x06userIdR\tsessionId"7\n\x14\x43\x61\x63hedRemoteRelation\x12\x1f\n\x0brelation_id\x18\x01 \x01(\tR\nrelationId"\x91\x02\n\x06Sample\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x1f\n\x0blower_bound\x18\x02 \x01(\x01R\nlowerBound\x12\x1f\n\x0bupper_bound\x18\x03 \x01(\x01R\nupperBound\x12.\n\x10with_replacement\x18\x04 \x01(\x08H\x00R\x0fwithReplacement\x88\x01\x01\x12\x17\n\x04seed\x18\x05 \x01(\x03H\x01R\x04seed\x88\x01\x01\x12/\n\x13\x64\x65terministic_order\x18\x06 \x01(\x08R\x12\x64\x65terministicOrderB\x13\n\x11_with_replacementB\x07\n\x05_seed"\x91\x01\n\x05Range\x12\x19\n\x05start\x18\x01 \x01(\x03H\x00R\x05start\x88\x01\x01\x12\x10\n\x03\x65nd\x18\x02 \x01(\x03R\x03\x65nd\x12\x12\n\x04step\x18\x03 \x01(\x03R\x04step\x12*\n\x0enum_partitions\x18\x04 \x01(\x05H\x01R\rnumPartitions\x88\x01\x01\x42\x08\n\x06_startB\x11\n\x0f_num_partitions"r\n\rSubqueryAlias\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x14\n\x05\x61lias\x18\x02 \x01(\tR\x05\x61lias\x12\x1c\n\tqualifier\x18\x03 \x03(\tR\tqualifier"\x8e\x01\n\x0bRepartition\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12%\n\x0enum_partitions\x18\x02 \x01(\x05R\rnumPartitions\x12\x1d\n\x07shuffle\x18\x03 \x01(\x08H\x00R\x07shuffle\x88\x01\x01\x42\n\n\x08_shuffle"\x8e\x01\n\nShowString\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x19\n\x08num_rows\x18\x02 \x01(\x05R\x07numRows\x12\x1a\n\x08truncate\x18\x03 \x01(\x05R\x08truncate\x12\x1a\n\x08vertical\x18\x04 \x01(\x08R\x08vertical"r\n\nHtmlString\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x19\n\x08num_rows\x18\x02 \x01(\x05R\x07numRows\x12\x1a\n\x08truncate\x18\x03 \x01(\x05R\x08truncate"\\\n\x0bStatSummary\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x1e\n\nstatistics\x18\x02 \x03(\tR\nstatistics"Q\n\x0cStatDescribe\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols"e\n\x0cStatCrosstab\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ol1\x18\x02 \x01(\tR\x04\x63ol1\x12\x12\n\x04\x63ol2\x18\x03 \x01(\tR\x04\x63ol2"`\n\x07StatCov\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ol1\x18\x02 \x01(\tR\x04\x63ol1\x12\x12\n\x04\x63ol2\x18\x03 \x01(\tR\x04\x63ol2"\x89\x01\n\x08StatCorr\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ol1\x18\x02 \x01(\tR\x04\x63ol1\x12\x12\n\x04\x63ol2\x18\x03 \x01(\tR\x04\x63ol2\x12\x1b\n\x06method\x18\x04 \x01(\tH\x00R\x06method\x88\x01\x01\x42\t\n\x07_method"\xa4\x01\n\x12StatApproxQuantile\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols\x12$\n\rprobabilities\x18\x03 \x03(\x01R\rprobabilities\x12%\n\x0erelative_error\x18\x04 \x01(\x01R\rrelativeError"}\n\rStatFreqItems\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols\x12\x1d\n\x07support\x18\x03 \x01(\x01H\x00R\x07support\x88\x01\x01\x42\n\n\x08_support"\xb5\x02\n\x0cStatSampleBy\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12+\n\x03\x63ol\x18\x02 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x03\x63ol\x12\x42\n\tfractions\x18\x03 \x03(\x0b\x32$.spark.connect.StatSampleBy.FractionR\tfractions\x12\x17\n\x04seed\x18\x05 \x01(\x03H\x00R\x04seed\x88\x01\x01\x1a\x63\n\x08\x46raction\x12;\n\x07stratum\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x07stratum\x12\x1a\n\x08\x66raction\x18\x02 \x01(\x01R\x08\x66ractionB\x07\n\x05_seed"\x86\x01\n\x06NAFill\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols\x12\x39\n\x06values\x18\x03 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06values"\x86\x01\n\x06NADrop\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols\x12\'\n\rmin_non_nulls\x18\x03 \x01(\x05H\x00R\x0bminNonNulls\x88\x01\x01\x42\x10\n\x0e_min_non_nulls"\xa8\x02\n\tNAReplace\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols\x12H\n\x0creplacements\x18\x03 \x03(\x0b\x32$.spark.connect.NAReplace.ReplacementR\x0creplacements\x1a\x8d\x01\n\x0bReplacement\x12>\n\told_value\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x08oldValue\x12>\n\tnew_value\x18\x02 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x08newValue"X\n\x04ToDF\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12!\n\x0c\x63olumn_names\x18\x02 \x03(\tR\x0b\x63olumnNames"\xfe\x02\n\x12WithColumnsRenamed\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12i\n\x12rename_columns_map\x18\x02 \x03(\x0b\x32\x37.spark.connect.WithColumnsRenamed.RenameColumnsMapEntryB\x02\x18\x01R\x10renameColumnsMap\x12\x42\n\x07renames\x18\x03 \x03(\x0b\x32(.spark.connect.WithColumnsRenamed.RenameR\x07renames\x1a\x43\n\x15RenameColumnsMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x45\n\x06Rename\x12\x19\n\x08\x63ol_name\x18\x01 \x01(\tR\x07\x63olName\x12 \n\x0cnew_col_name\x18\x02 \x01(\tR\nnewColName"w\n\x0bWithColumns\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x39\n\x07\x61liases\x18\x02 \x03(\x0b\x32\x1f.spark.connect.Expression.AliasR\x07\x61liases"\x86\x01\n\rWithWatermark\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x1d\n\nevent_time\x18\x02 \x01(\tR\teventTime\x12\'\n\x0f\x64\x65lay_threshold\x18\x03 \x01(\tR\x0e\x64\x65layThreshold"\x84\x01\n\x04Hint\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x39\n\nparameters\x18\x03 \x03(\x0b\x32\x19.spark.connect.ExpressionR\nparameters"\xc7\x02\n\x07Unpivot\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12+\n\x03ids\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x03ids\x12:\n\x06values\x18\x03 \x01(\x0b\x32\x1d.spark.connect.Unpivot.ValuesH\x00R\x06values\x88\x01\x01\x12\x30\n\x14variable_column_name\x18\x04 \x01(\tR\x12variableColumnName\x12*\n\x11value_column_name\x18\x05 \x01(\tR\x0fvalueColumnName\x1a;\n\x06Values\x12\x31\n\x06values\x18\x01 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x06valuesB\t\n\x07_values"j\n\x08ToSchema\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12/\n\x06schema\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataTypeR\x06schema"\xcb\x01\n\x17RepartitionByExpression\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x42\n\x0fpartition_exprs\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x0epartitionExprs\x12*\n\x0enum_partitions\x18\x03 \x01(\x05H\x00R\rnumPartitions\x88\x01\x01\x42\x11\n\x0f_num_partitions"\xe8\x01\n\rMapPartitions\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x42\n\x04\x66unc\x18\x02 \x01(\x0b\x32..spark.connect.CommonInlineUserDefinedFunctionR\x04\x66unc\x12"\n\nis_barrier\x18\x03 \x01(\x08H\x00R\tisBarrier\x88\x01\x01\x12"\n\nprofile_id\x18\x04 \x01(\x05H\x01R\tprofileId\x88\x01\x01\x42\r\n\x0b_is_barrierB\r\n\x0b_profile_id"\xfb\x04\n\x08GroupMap\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12L\n\x14grouping_expressions\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x13groupingExpressions\x12\x42\n\x04\x66unc\x18\x03 \x01(\x0b\x32..spark.connect.CommonInlineUserDefinedFunctionR\x04\x66unc\x12J\n\x13sorting_expressions\x18\x04 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x12sortingExpressions\x12<\n\rinitial_input\x18\x05 \x01(\x0b\x32\x17.spark.connect.RelationR\x0cinitialInput\x12[\n\x1cinitial_grouping_expressions\x18\x06 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x1ainitialGroupingExpressions\x12;\n\x18is_map_groups_with_state\x18\x07 \x01(\x08H\x00R\x14isMapGroupsWithState\x88\x01\x01\x12$\n\x0boutput_mode\x18\x08 \x01(\tH\x01R\noutputMode\x88\x01\x01\x12&\n\x0ctimeout_conf\x18\t \x01(\tH\x02R\x0btimeoutConf\x88\x01\x01\x42\x1b\n\x19_is_map_groups_with_stateB\x0e\n\x0c_output_modeB\x0f\n\r_timeout_conf"\x8e\x04\n\nCoGroupMap\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12W\n\x1ainput_grouping_expressions\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x18inputGroupingExpressions\x12-\n\x05other\x18\x03 \x01(\x0b\x32\x17.spark.connect.RelationR\x05other\x12W\n\x1aother_grouping_expressions\x18\x04 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x18otherGroupingExpressions\x12\x42\n\x04\x66unc\x18\x05 \x01(\x0b\x32..spark.connect.CommonInlineUserDefinedFunctionR\x04\x66unc\x12U\n\x19input_sorting_expressions\x18\x06 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x17inputSortingExpressions\x12U\n\x19other_sorting_expressions\x18\x07 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x17otherSortingExpressions"\xe5\x02\n\x16\x41pplyInPandasWithState\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12L\n\x14grouping_expressions\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x13groupingExpressions\x12\x42\n\x04\x66unc\x18\x03 \x01(\x0b\x32..spark.connect.CommonInlineUserDefinedFunctionR\x04\x66unc\x12#\n\routput_schema\x18\x04 \x01(\tR\x0coutputSchema\x12!\n\x0cstate_schema\x18\x05 \x01(\tR\x0bstateSchema\x12\x1f\n\x0boutput_mode\x18\x06 \x01(\tR\noutputMode\x12!\n\x0ctimeout_conf\x18\x07 \x01(\tR\x0btimeoutConf"\xf4\x01\n$CommonInlineUserDefinedTableFunction\x12#\n\rfunction_name\x18\x01 \x01(\tR\x0c\x66unctionName\x12$\n\rdeterministic\x18\x02 \x01(\x08R\rdeterministic\x12\x37\n\targuments\x18\x03 \x03(\x0b\x32\x19.spark.connect.ExpressionR\targuments\x12<\n\x0bpython_udtf\x18\x04 \x01(\x0b\x32\x19.spark.connect.PythonUDTFH\x00R\npythonUdtfB\n\n\x08\x66unction"\xb1\x01\n\nPythonUDTF\x12=\n\x0breturn_type\x18\x01 \x01(\x0b\x32\x17.spark.connect.DataTypeH\x00R\nreturnType\x88\x01\x01\x12\x1b\n\teval_type\x18\x02 \x01(\x05R\x08\x65valType\x12\x18\n\x07\x63ommand\x18\x03 \x01(\x0cR\x07\x63ommand\x12\x1d\n\npython_ver\x18\x04 \x01(\tR\tpythonVerB\x0e\n\x0c_return_type"\x97\x01\n!CommonInlineUserDefinedDataSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12O\n\x12python_data_source\x18\x02 \x01(\x0b\x32\x1f.spark.connect.PythonDataSourceH\x00R\x10pythonDataSourceB\r\n\x0b\x64\x61ta_source"K\n\x10PythonDataSource\x12\x18\n\x07\x63ommand\x18\x01 \x01(\x0cR\x07\x63ommand\x12\x1d\n\npython_ver\x18\x02 \x01(\tR\tpythonVer"\x88\x01\n\x0e\x43ollectMetrics\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x33\n\x07metrics\x18\x03 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x07metrics"\x84\x03\n\x05Parse\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x38\n\x06\x66ormat\x18\x02 \x01(\x0e\x32 .spark.connect.Parse.ParseFormatR\x06\x66ormat\x12\x34\n\x06schema\x18\x03 \x01(\x0b\x32\x17.spark.connect.DataTypeH\x00R\x06schema\x88\x01\x01\x12;\n\x07options\x18\x04 \x03(\x0b\x32!.spark.connect.Parse.OptionsEntryR\x07options\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"X\n\x0bParseFormat\x12\x1c\n\x18PARSE_FORMAT_UNSPECIFIED\x10\x00\x12\x14\n\x10PARSE_FORMAT_CSV\x10\x01\x12\x15\n\x11PARSE_FORMAT_JSON\x10\x02\x42\t\n\x07_schema"\xdb\x03\n\x08\x41sOfJoin\x12+\n\x04left\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x04left\x12-\n\x05right\x18\x02 \x01(\x0b\x32\x17.spark.connect.RelationR\x05right\x12\x37\n\nleft_as_of\x18\x03 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x08leftAsOf\x12\x39\n\x0bright_as_of\x18\x04 \x01(\x0b\x32\x19.spark.connect.ExpressionR\trightAsOf\x12\x36\n\tjoin_expr\x18\x05 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x08joinExpr\x12#\n\rusing_columns\x18\x06 \x03(\tR\x0cusingColumns\x12\x1b\n\tjoin_type\x18\x07 \x01(\tR\x08joinType\x12\x37\n\ttolerance\x18\x08 \x01(\x0b\x32\x19.spark.connect.ExpressionR\ttolerance\x12.\n\x13\x61llow_exact_matches\x18\t \x01(\x08R\x11\x61llowExactMatches\x12\x1c\n\tdirection\x18\n \x01(\tR\tdirectionB6\n\x1eorg.apache.spark.connect.protoP\x01Z\x12internal/generatedb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "pyspark.sql.connect.proto.relations_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\n\036org.apache.spark.connect.protoP\001Z\022internal/generated"
    )
    _SQL_ARGSENTRY._options = None
    _SQL_ARGSENTRY._serialized_options = b"8\001"
    _SQL_NAMEDARGUMENTSENTRY._options = None
    _SQL_NAMEDARGUMENTSENTRY._serialized_options = b"8\001"
    _SQL.fields_by_name["args"]._options = None
    _SQL.fields_by_name["args"]._serialized_options = b"\030\001"
    _SQL.fields_by_name["pos_args"]._options = None
    _SQL.fields_by_name["pos_args"]._serialized_options = b"\030\001"
    _READ_NAMEDTABLE_OPTIONSENTRY._options = None
    _READ_NAMEDTABLE_OPTIONSENTRY._serialized_options = b"8\001"
    _READ_DATASOURCE_OPTIONSENTRY._options = None
    _READ_DATASOURCE_OPTIONSENTRY._serialized_options = b"8\001"
    _WITHCOLUMNSRENAMED_RENAMECOLUMNSMAPENTRY._options = None
    _WITHCOLUMNSRENAMED_RENAMECOLUMNSMAPENTRY._serialized_options = b"8\001"
    _WITHCOLUMNSRENAMED.fields_by_name["rename_columns_map"]._options = None
    _WITHCOLUMNSRENAMED.fields_by_name["rename_columns_map"]._serialized_options = b"\030\001"
    _PARSE_OPTIONSENTRY._options = None
    _PARSE_OPTIONSENTRY._serialized_options = b"8\001"
    _RELATION._serialized_start = 193
    _RELATION._serialized_end = 3626
    _UNKNOWN._serialized_start = 3628
    _UNKNOWN._serialized_end = 3637
    _RELATIONCOMMON._serialized_start = 3639
    _RELATIONCOMMON._serialized_end = 3730
    _SQL._serialized_start = 3733
    _SQL._serialized_end = 4211
    _SQL_ARGSENTRY._serialized_start = 4027
    _SQL_ARGSENTRY._serialized_end = 4117
    _SQL_NAMEDARGUMENTSENTRY._serialized_start = 4119
    _SQL_NAMEDARGUMENTSENTRY._serialized_end = 4211
    _WITHRELATIONS._serialized_start = 4213
    _WITHRELATIONS._serialized_end = 4330
    _READ._serialized_start = 4333
    _READ._serialized_end = 4996
    _READ_NAMEDTABLE._serialized_start = 4511
    _READ_NAMEDTABLE._serialized_end = 4703
    _READ_NAMEDTABLE_OPTIONSENTRY._serialized_start = 4645
    _READ_NAMEDTABLE_OPTIONSENTRY._serialized_end = 4703
    _READ_DATASOURCE._serialized_start = 4706
    _READ_DATASOURCE._serialized_end = 4983
    _READ_DATASOURCE_OPTIONSENTRY._serialized_start = 4645
    _READ_DATASOURCE_OPTIONSENTRY._serialized_end = 4703
    _PROJECT._serialized_start = 4998
    _PROJECT._serialized_end = 5115
    _FILTER._serialized_start = 5117
    _FILTER._serialized_end = 5229
    _JOIN._serialized_start = 5232
    _JOIN._serialized_end = 5893
    _JOIN_JOINDATATYPE._serialized_start = 5571
    _JOIN_JOINDATATYPE._serialized_end = 5663
    _JOIN_JOINTYPE._serialized_start = 5666
    _JOIN_JOINTYPE._serialized_end = 5874
    _SETOPERATION._serialized_start = 5896
    _SETOPERATION._serialized_end = 6375
    _SETOPERATION_SETOPTYPE._serialized_start = 6212
    _SETOPERATION_SETOPTYPE._serialized_end = 6326
    _LIMIT._serialized_start = 6377
    _LIMIT._serialized_end = 6453
    _OFFSET._serialized_start = 6455
    _OFFSET._serialized_end = 6534
    _TAIL._serialized_start = 6536
    _TAIL._serialized_end = 6611
    _AGGREGATE._serialized_start = 6614
    _AGGREGATE._serialized_end = 7380
    _AGGREGATE_PIVOT._serialized_start = 7029
    _AGGREGATE_PIVOT._serialized_end = 7140
    _AGGREGATE_GROUPINGSETS._serialized_start = 7142
    _AGGREGATE_GROUPINGSETS._serialized_end = 7218
    _AGGREGATE_GROUPTYPE._serialized_start = 7221
    _AGGREGATE_GROUPTYPE._serialized_end = 7380
    _SORT._serialized_start = 7383
    _SORT._serialized_end = 7543
    _DROP._serialized_start = 7546
    _DROP._serialized_end = 7687
    _DEDUPLICATE._serialized_start = 7690
    _DEDUPLICATE._serialized_end = 7930
    _LOCALRELATION._serialized_start = 7932
    _LOCALRELATION._serialized_end = 8021
    _CACHEDLOCALRELATION._serialized_start = 8023
    _CACHEDLOCALRELATION._serialized_end = 8095
    _CACHEDREMOTERELATION._serialized_start = 8097
    _CACHEDREMOTERELATION._serialized_end = 8152
    _SAMPLE._serialized_start = 8155
    _SAMPLE._serialized_end = 8428
    _RANGE._serialized_start = 8431
    _RANGE._serialized_end = 8576
    _SUBQUERYALIAS._serialized_start = 8578
    _SUBQUERYALIAS._serialized_end = 8692
    _REPARTITION._serialized_start = 8695
    _REPARTITION._serialized_end = 8837
    _SHOWSTRING._serialized_start = 8840
    _SHOWSTRING._serialized_end = 8982
    _HTMLSTRING._serialized_start = 8984
    _HTMLSTRING._serialized_end = 9098
    _STATSUMMARY._serialized_start = 9100
    _STATSUMMARY._serialized_end = 9192
    _STATDESCRIBE._serialized_start = 9194
    _STATDESCRIBE._serialized_end = 9275
    _STATCROSSTAB._serialized_start = 9277
    _STATCROSSTAB._serialized_end = 9378
    _STATCOV._serialized_start = 9380
    _STATCOV._serialized_end = 9476
    _STATCORR._serialized_start = 9479
    _STATCORR._serialized_end = 9616
    _STATAPPROXQUANTILE._serialized_start = 9619
    _STATAPPROXQUANTILE._serialized_end = 9783
    _STATFREQITEMS._serialized_start = 9785
    _STATFREQITEMS._serialized_end = 9910
    _STATSAMPLEBY._serialized_start = 9913
    _STATSAMPLEBY._serialized_end = 10222
    _STATSAMPLEBY_FRACTION._serialized_start = 10114
    _STATSAMPLEBY_FRACTION._serialized_end = 10213
    _NAFILL._serialized_start = 10225
    _NAFILL._serialized_end = 10359
    _NADROP._serialized_start = 10362
    _NADROP._serialized_end = 10496
    _NAREPLACE._serialized_start = 10499
    _NAREPLACE._serialized_end = 10795
    _NAREPLACE_REPLACEMENT._serialized_start = 10654
    _NAREPLACE_REPLACEMENT._serialized_end = 10795
    _TODF._serialized_start = 10797
    _TODF._serialized_end = 10885
    _WITHCOLUMNSRENAMED._serialized_start = 10888
    _WITHCOLUMNSRENAMED._serialized_end = 11270
    _WITHCOLUMNSRENAMED_RENAMECOLUMNSMAPENTRY._serialized_start = 11132
    _WITHCOLUMNSRENAMED_RENAMECOLUMNSMAPENTRY._serialized_end = 11199
    _WITHCOLUMNSRENAMED_RENAME._serialized_start = 11201
    _WITHCOLUMNSRENAMED_RENAME._serialized_end = 11270
    _WITHCOLUMNS._serialized_start = 11272
    _WITHCOLUMNS._serialized_end = 11391
    _WITHWATERMARK._serialized_start = 11394
    _WITHWATERMARK._serialized_end = 11528
    _HINT._serialized_start = 11531
    _HINT._serialized_end = 11663
    _UNPIVOT._serialized_start = 11666
    _UNPIVOT._serialized_end = 11993
    _UNPIVOT_VALUES._serialized_start = 11923
    _UNPIVOT_VALUES._serialized_end = 11982
    _TOSCHEMA._serialized_start = 11995
    _TOSCHEMA._serialized_end = 12101
    _REPARTITIONBYEXPRESSION._serialized_start = 12104
    _REPARTITIONBYEXPRESSION._serialized_end = 12307
    _MAPPARTITIONS._serialized_start = 12310
    _MAPPARTITIONS._serialized_end = 12542
    _GROUPMAP._serialized_start = 12545
    _GROUPMAP._serialized_end = 13180
    _COGROUPMAP._serialized_start = 13183
    _COGROUPMAP._serialized_end = 13709
    _APPLYINPANDASWITHSTATE._serialized_start = 13712
    _APPLYINPANDASWITHSTATE._serialized_end = 14069
    _COMMONINLINEUSERDEFINEDTABLEFUNCTION._serialized_start = 14072
    _COMMONINLINEUSERDEFINEDTABLEFUNCTION._serialized_end = 14316
    _PYTHONUDTF._serialized_start = 14319
    _PYTHONUDTF._serialized_end = 14496
    _COMMONINLINEUSERDEFINEDDATASOURCE._serialized_start = 14499
    _COMMONINLINEUSERDEFINEDDATASOURCE._serialized_end = 14650
    _PYTHONDATASOURCE._serialized_start = 14652
    _PYTHONDATASOURCE._serialized_end = 14727
    _COLLECTMETRICS._serialized_start = 14730
    _COLLECTMETRICS._serialized_end = 14866
    _PARSE._serialized_start = 14869
    _PARSE._serialized_end = 15257
    _PARSE_OPTIONSENTRY._serialized_start = 4645
    _PARSE_OPTIONSENTRY._serialized_end = 4703
    _PARSE_PARSEFORMAT._serialized_start = 15158
    _PARSE_PARSEFORMAT._serialized_end = 15246
    _ASOFJOIN._serialized_start = 15260
    _ASOFJOIN._serialized_end = 15735
# @@protoc_insertion_point(module_scope)
