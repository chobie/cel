"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Simple end-to-end conformance tests."""

import builtins
import cel.expr.checked_pb2
import cel.expr.eval_pb2
import cel.expr.value_pb2
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SimpleTestFile(google.protobuf.message.Message):
    """The format of a simple test file, expected to be stored in text format.
    A file is the unit of granularity for selecting conformance tests,
    so tests of optional features should be segregated into separate files.

    Deprecated: Use cel.expr.conformance.test.Suite
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SECTION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Required.  The name of the file.  Should match the filename."""
    description: builtins.str
    """A description of the file."""
    @property
    def section(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SimpleTestSection]:
        """The contained sections."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        section: collections.abc.Iterable[global___SimpleTestSection] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "name", b"name", "section", b"section"]) -> None: ...

global___SimpleTestFile = SimpleTestFile

@typing.final
class SimpleTestSection(google.protobuf.message.Message):
    """A collection of related SimpleTests.

    The section is the unit of organization within a test file, and should
    guide where new tests are added.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TEST_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Required.  The name of the section."""
    description: builtins.str
    """A description of the section."""
    @property
    def test(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SimpleTest]:
        """The contained tests."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        test: collections.abc.Iterable[global___SimpleTest] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "name", b"name", "test", b"test"]) -> None: ...

global___SimpleTestSection = SimpleTestSection

@typing.final
class SimpleTest(google.protobuf.message.Message):
    """A test which should run the given CEL program through parsing,
    optionally through checking, then evaluation, with the results
    of the pipeline validated by the given result matcher.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class BindingsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> cel.expr.eval_pb2.ExprValue: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: cel.expr.eval_pb2.ExprValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPR_FIELD_NUMBER: builtins.int
    DISABLE_MACROS_FIELD_NUMBER: builtins.int
    DISABLE_CHECK_FIELD_NUMBER: builtins.int
    CHECK_ONLY_FIELD_NUMBER: builtins.int
    TYPE_ENV_FIELD_NUMBER: builtins.int
    CONTAINER_FIELD_NUMBER: builtins.int
    LOCALE_FIELD_NUMBER: builtins.int
    BINDINGS_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    TYPED_RESULT_FIELD_NUMBER: builtins.int
    EVAL_ERROR_FIELD_NUMBER: builtins.int
    ANY_EVAL_ERRORS_FIELD_NUMBER: builtins.int
    UNKNOWN_FIELD_NUMBER: builtins.int
    ANY_UNKNOWNS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Required.  The name of the test, which should be unique in the test file."""
    description: builtins.str
    """A description of the test."""
    expr: builtins.str
    """Required.  The text of the CEL expression."""
    disable_macros: builtins.bool
    """Disables all macro expansion in parsing."""
    disable_check: builtins.bool
    """Disables the check phase."""
    check_only: builtins.bool
    """Disables the evaluate phase."""
    container: builtins.str
    """The container for name resolution."""
    locale: builtins.str
    """The locale to use for the evaluation phase."""
    @property
    def type_env(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cel.expr.checked_pb2.Decl]:
        """The type environment to use for the check phase."""

    @property
    def bindings(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, cel.expr.eval_pb2.ExprValue]:
        """Variable bindings to use for the eval phase."""

    @property
    def value(self) -> cel.expr.value_pb2.Value:
        """A normal value, which must match the evaluation result exactly
        via value equality semantics.  This coincides with proto equality,
        except for:
        *   maps are order-agnostic.
        *   a floating point NaN should match any NaN.
        """

    @property
    def typed_result(self) -> global___TypedResult:
        """A result and deduced expression type."""

    @property
    def eval_error(self) -> cel.expr.eval_pb2.ErrorSet:
        """Matches error evaluation results."""

    @property
    def any_eval_errors(self) -> global___ErrorSetMatcher:
        """Matches one of several error results.
        (Using explicit message since oneof can't handle repeated.)
        """

    @property
    def unknown(self) -> cel.expr.eval_pb2.UnknownSet:
        """Matches unknown evaluation results."""

    @property
    def any_unknowns(self) -> global___UnknownSetMatcher:
        """Matches one of several unknown results.
        (Using explicit message since oneof can't handle repeated.)
        """

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        expr: builtins.str = ...,
        disable_macros: builtins.bool = ...,
        disable_check: builtins.bool = ...,
        check_only: builtins.bool = ...,
        type_env: collections.abc.Iterable[cel.expr.checked_pb2.Decl] | None = ...,
        container: builtins.str = ...,
        locale: builtins.str = ...,
        bindings: collections.abc.Mapping[builtins.str, cel.expr.eval_pb2.ExprValue] | None = ...,
        value: cel.expr.value_pb2.Value | None = ...,
        typed_result: global___TypedResult | None = ...,
        eval_error: cel.expr.eval_pb2.ErrorSet | None = ...,
        any_eval_errors: global___ErrorSetMatcher | None = ...,
        unknown: cel.expr.eval_pb2.UnknownSet | None = ...,
        any_unknowns: global___UnknownSetMatcher | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["any_eval_errors", b"any_eval_errors", "any_unknowns", b"any_unknowns", "eval_error", b"eval_error", "result_matcher", b"result_matcher", "typed_result", b"typed_result", "unknown", b"unknown", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["any_eval_errors", b"any_eval_errors", "any_unknowns", b"any_unknowns", "bindings", b"bindings", "check_only", b"check_only", "container", b"container", "description", b"description", "disable_check", b"disable_check", "disable_macros", b"disable_macros", "eval_error", b"eval_error", "expr", b"expr", "locale", b"locale", "name", b"name", "result_matcher", b"result_matcher", "type_env", b"type_env", "typed_result", b"typed_result", "unknown", b"unknown", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["result_matcher", b"result_matcher"]) -> typing.Literal["value", "typed_result", "eval_error", "any_eval_errors", "unknown", "any_unknowns"] | None: ...

global___SimpleTest = SimpleTest

@typing.final
class TypedResult(google.protobuf.message.Message):
    """Matches a result along with deduced expression type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    DEDUCED_TYPE_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> cel.expr.value_pb2.Value:
        """A normal value, which must match the evaluation result exactly
        via value equality semantics. This is ignored if the test is `check_only`.
        """

    @property
    def deduced_type(self) -> cel.expr.checked_pb2.Type:
        """The deduced type of the expression as reported by the checker."""

    def __init__(
        self,
        *,
        result: cel.expr.value_pb2.Value | None = ...,
        deduced_type: cel.expr.checked_pb2.Type | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["deduced_type", b"deduced_type", "result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["deduced_type", b"deduced_type", "result", b"result"]) -> None: ...

global___TypedResult = TypedResult

@typing.final
class ErrorSetMatcher(google.protobuf.message.Message):
    """Matches error results from Eval."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERRORS_FIELD_NUMBER: builtins.int
    @property
    def errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cel.expr.eval_pb2.ErrorSet]:
        """Success if we match any of these sets."""

    def __init__(
        self,
        *,
        errors: collections.abc.Iterable[cel.expr.eval_pb2.ErrorSet] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["errors", b"errors"]) -> None: ...

global___ErrorSetMatcher = ErrorSetMatcher

@typing.final
class UnknownSetMatcher(google.protobuf.message.Message):
    """Matches unknown results from Eval."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UNKNOWNS_FIELD_NUMBER: builtins.int
    @property
    def unknowns(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cel.expr.eval_pb2.UnknownSet]:
        """Success if we match any of these sets."""

    def __init__(
        self,
        *,
        unknowns: collections.abc.Iterable[cel.expr.eval_pb2.UnknownSet] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["unknowns", b"unknowns"]) -> None: ...

global___UnknownSetMatcher = UnknownSetMatcher
