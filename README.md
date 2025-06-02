# prebuild cel proto for python

Since generating the CEL protobuf definitions can take a bit of extra effort, I’ve decided to temporarily share the prebuilt versions in a repository.

## How to build

```
git clone https://github.com/google/cel-spec
git clone https://github.com/googleapis/googleapis

protoc -I=./cel-spec/proto -I=./googleapis/ \
       --python_out=./ \
      --mypy_out=./ \
       ./cel-spec/proto/cel/expr/syntax.proto \
       ./cel-spec/proto/cel/expr/checked.proto \
       ./cel-spec/proto/cel/expr/eval.proto \
       ./cel-spec/proto/cel/expr/value.proto \
       ./cel-spec/proto/cel/expr/explain.proto \
       ./cel-spec/proto/cel/expr/conformance/test/simple.proto \
       ./cel-spec/proto/cel/expr/conformance/test/suite.proto \
       ./cel-spec/proto/cel/expr/conformance/conformance_service.proto \
       ./cel-spec/proto/cel/expr/conformance/env_config.proto \
       ./cel-spec/proto/cel/expr/conformance/proto2/test_all_types.proto \
       ./cel-spec/proto/cel/expr/conformance/proto2/test_all_types_extensions.proto \
       ./cel-spec/proto/cel/expr/conformance/proto3/test_all_types.proto \
       ./googleapis/google/rpc/status.proto \
       ./googleapis/google/rpc/code.proto
```
