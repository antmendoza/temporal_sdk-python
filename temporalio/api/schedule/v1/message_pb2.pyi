"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
The MIT License

Copyright (c) 2020 Temporal Technologies Inc.  All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import temporalio.api.common.v1.message_pb2
import temporalio.api.enums.v1.schedule_pb2
import temporalio.api.workflow.v1.message_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CalendarSpec(google.protobuf.message.Message):
    """CalendarSpec describes an event specification relative to the calendar,
    similar to a traditional cron specification. Each field can be one of:
      *: matches always
      x: matches when the field equals x
      x/y : matches when the field equals x+n*y where n is an integer
      x-z: matches when the field is between x and z inclusive
      w,x,y,...: matches when the field is one of the listed values
    Each x, y, z, ... is either a decimal integer, or a month or day of week name
    or abbreviation (in the appropriate fields).
    A second in time matches if all fields match.
    Note that the special case that some cron implementations have for treating
    day_of_month and day_of_week as "or" instead of "and" when both are set is
    not implemented.
    day_of_week can accept 0 or 7 as Sunday
    TODO: add relative-to-end-of-month
    TODO: add nth day-of-week in month
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECOND_FIELD_NUMBER: builtins.int
    MINUTE_FIELD_NUMBER: builtins.int
    HOUR_FIELD_NUMBER: builtins.int
    DAY_OF_MONTH_FIELD_NUMBER: builtins.int
    MONTH_FIELD_NUMBER: builtins.int
    YEAR_FIELD_NUMBER: builtins.int
    DAY_OF_WEEK_FIELD_NUMBER: builtins.int
    second: builtins.str
    """Expression to match seconds. Default: 0"""
    minute: builtins.str
    """Expression to match minutes. Default: 0"""
    hour: builtins.str
    """Expression to match hours. Default: 0"""
    day_of_month: builtins.str
    """Expression to match days of the month. Default: *
    (-- api-linter: core::0140::prepositions=disabled
        aip.dev/not-precedent: standard name of field --)
    """
    month: builtins.str
    """Expression to match months. Default: *"""
    year: builtins.str
    """Expression to match years. Default: *"""
    day_of_week: builtins.str
    """Expression to match days of the week. Default: *"""
    def __init__(
        self,
        *,
        second: builtins.str = ...,
        minute: builtins.str = ...,
        hour: builtins.str = ...,
        day_of_month: builtins.str = ...,
        month: builtins.str = ...,
        year: builtins.str = ...,
        day_of_week: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "day_of_month",
            b"day_of_month",
            "day_of_week",
            b"day_of_week",
            "hour",
            b"hour",
            "minute",
            b"minute",
            "month",
            b"month",
            "second",
            b"second",
            "year",
            b"year",
        ],
    ) -> None: ...

global___CalendarSpec = CalendarSpec

class IntervalSpec(google.protobuf.message.Message):
    """IntervalSpec matches times that can be expressed as:
    epoch + n * interval + phase
    where n is an integer.
    phase defaults to zero if missing. interval is required.
    Both interval and phase must be non-negative and are truncated to the nearest
    second before any calculations.
    For example, an interval of 1 hour with phase of zero would match every hour,
    on the hour. The same interval but a phase of 19 minutes would match every
    xx:19:00. An interval of 28 days with phase zero would match
    2022-02-17T00:00:00Z (among other times). The same interval with a phase of 3
    days, 5 hours, and 23 minutes would match 2022-02-20T05:23:00Z instead.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTERVAL_FIELD_NUMBER: builtins.int
    PHASE_FIELD_NUMBER: builtins.int
    @property
    def interval(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def phase(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        interval: google.protobuf.duration_pb2.Duration | None = ...,
        phase: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "interval", b"interval", "phase", b"phase"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "interval", b"interval", "phase", b"phase"
        ],
    ) -> None: ...

global___IntervalSpec = IntervalSpec

class ScheduleSpec(google.protobuf.message.Message):
    """ScheduleSpec is a complete description of a set of absolute timestamps
    (possibly infinite) that an action should occur at. The meaning of a
    ScheduleSpec depends only on its contents and never changes, except that the
    definition of a time zone can change over time (most commonly, when daylight
    saving time policy changes for an area). To create a totally self-contained
    ScheduleSpec, use UTC or include timezone_data.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CALENDAR_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    EXCLUDE_CALENDAR_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    JITTER_FIELD_NUMBER: builtins.int
    TIMEZONE_NAME_FIELD_NUMBER: builtins.int
    TIMEZONE_DATA_FIELD_NUMBER: builtins.int
    @property
    def calendar(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___CalendarSpec
    ]:
        """Calendar-based specifications of times."""
    @property
    def interval(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___IntervalSpec
    ]:
        """Interval-based specifications of times."""
    @property
    def exclude_calendar(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___CalendarSpec
    ]:
        """Any timestamps matching any of the exclude_calendar specs will be
        skipped.
        """
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Any timestamps before start_time will be skipped. Together, start_time
        and end_time make an inclusive interval.
        """
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Any timestamps after end_time will be skipped."""
    @property
    def jitter(self) -> google.protobuf.duration_pb2.Duration:
        """All timestamps will be incremented by a random value from 0 to this
        amount of jitter. Default: 1 second
        """
    timezone_name: builtins.str
    """Time zone to interpret all CalendarSpecs in.

    If unset, defaults to UTC. We recommend using UTC for your application if
    at all possible, to avoid various surprising properties of time zones.

    Time zones may be provided by name, corresponding to names in the IANA
    time zone database (see https://www.iana.org/time-zones). The definition
    will be loaded by the Temporal server from the environment it runs in.

    If your application requires more control over the time zone definition
    used, it may pass in a complete definition in the form of a TZif file
    from the time zone database. If present, this will be used instead of
    loading anything from the environment. You are then responsible for
    updating timezone_data when the definition changes.

    Calendar spec matching is based on literal matching of the clock time
    with no special handling of DST: if you write a calendar spec that fires
    at 2:30am and specify a time zone that follows DST, that action will not
    be triggered on the day that has no 2:30am. Similarly, an action that
    fires at 1:30am will be triggered twice on the day that has two 1:30s.
    """
    timezone_data: builtins.bytes
    def __init__(
        self,
        *,
        calendar: collections.abc.Iterable[global___CalendarSpec] | None = ...,
        interval: collections.abc.Iterable[global___IntervalSpec] | None = ...,
        exclude_calendar: collections.abc.Iterable[global___CalendarSpec] | None = ...,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        end_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        jitter: google.protobuf.duration_pb2.Duration | None = ...,
        timezone_name: builtins.str = ...,
        timezone_data: builtins.bytes = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "end_time", b"end_time", "jitter", b"jitter", "start_time", b"start_time"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "calendar",
            b"calendar",
            "end_time",
            b"end_time",
            "exclude_calendar",
            b"exclude_calendar",
            "interval",
            b"interval",
            "jitter",
            b"jitter",
            "start_time",
            b"start_time",
            "timezone_data",
            b"timezone_data",
            "timezone_name",
            b"timezone_name",
        ],
    ) -> None: ...

global___ScheduleSpec = ScheduleSpec

class SchedulePolicies(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OVERLAP_POLICY_FIELD_NUMBER: builtins.int
    CATCHUP_WINDOW_FIELD_NUMBER: builtins.int
    PAUSE_ON_FAILURE_FIELD_NUMBER: builtins.int
    overlap_policy: temporalio.api.enums.v1.schedule_pb2.ScheduleOverlapPolicy.ValueType
    """Policy for overlaps.
    Note that this can be changed after a schedule has taken some actions, and we can't
    provide 100% sensible semantics for all changes. The most confusing case would be
    changes to/from ALLOW_ALL: with that policy multiple scheduled workflows can run
    concurrently, but for all other policies only one can run at a time. Changing
    between these two classes will leave all workflows with the other class alone.
    E.g., if changing from ALLOW_ALL to CANCEL_OTHER, and there are workflows running,
    those workflows will not be cancelled. If changing from ALLOW_ALL to SKIP with
    workflows running, the running workflows will not cause the next action to be
    skipped.
    """
    @property
    def catchup_window(self) -> google.protobuf.duration_pb2.Duration:
        """Policy for catchups:
        If the Temporal server misses an action due to one or more components
        being down, and comes back up, the action will be run if the scheduled
        time is within this window from the current time.
        This value defaults to 60 seconds, and can't be less than 10 seconds.
        """
    pause_on_failure: builtins.bool
    """If true, and a workflow run fails or times out, turn on "paused".
    This applies after retry policies: the full chain of retries must fail to
    trigger a pause here.
    """
    def __init__(
        self,
        *,
        overlap_policy: temporalio.api.enums.v1.schedule_pb2.ScheduleOverlapPolicy.ValueType = ...,
        catchup_window: google.protobuf.duration_pb2.Duration | None = ...,
        pause_on_failure: builtins.bool = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["catchup_window", b"catchup_window"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "catchup_window",
            b"catchup_window",
            "overlap_policy",
            b"overlap_policy",
            "pause_on_failure",
            b"pause_on_failure",
        ],
    ) -> None: ...

global___SchedulePolicies = SchedulePolicies

class ScheduleAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_WORKFLOW_FIELD_NUMBER: builtins.int
    @property
    def start_workflow(
        self,
    ) -> temporalio.api.workflow.v1.message_pb2.NewWorkflowExecutionInfo:
        """All fields of NewWorkflowExecutionInfo are valid except for:
        - workflow_id_reuse_policy
        - cron_schedule
        The workflow id of the started workflow may not match this exactly,
        it may have a timestamp appended for uniqueness.
        """
    def __init__(
        self,
        *,
        start_workflow: temporalio.api.workflow.v1.message_pb2.NewWorkflowExecutionInfo
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "action", b"action", "start_workflow", b"start_workflow"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "action", b"action", "start_workflow", b"start_workflow"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["action", b"action"]
    ) -> typing_extensions.Literal["start_workflow"] | None: ...

global___ScheduleAction = ScheduleAction

class ScheduleActionResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCHEDULE_TIME_FIELD_NUMBER: builtins.int
    ACTUAL_TIME_FIELD_NUMBER: builtins.int
    START_WORKFLOW_RESULT_FIELD_NUMBER: builtins.int
    @property
    def schedule_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time that the action was taken (according to the schedule, including jitter)."""
    @property
    def actual_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time that the action was taken (real time)."""
    @property
    def start_workflow_result(
        self,
    ) -> temporalio.api.common.v1.message_pb2.WorkflowExecution:
        """If action was start_workflow:"""
    def __init__(
        self,
        *,
        schedule_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        actual_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        start_workflow_result: temporalio.api.common.v1.message_pb2.WorkflowExecution
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "actual_time",
            b"actual_time",
            "schedule_time",
            b"schedule_time",
            "start_workflow_result",
            b"start_workflow_result",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "actual_time",
            b"actual_time",
            "schedule_time",
            b"schedule_time",
            "start_workflow_result",
            b"start_workflow_result",
        ],
    ) -> None: ...

global___ScheduleActionResult = ScheduleActionResult

class ScheduleState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTES_FIELD_NUMBER: builtins.int
    PAUSED_FIELD_NUMBER: builtins.int
    LIMITED_ACTIONS_FIELD_NUMBER: builtins.int
    REMAINING_ACTIONS_FIELD_NUMBER: builtins.int
    notes: builtins.str
    """Informative human-readable message with contextual notes, e.g. the reason
    a schedule is paused. The system may overwrite this message on certain
    conditions, e.g. when pause-on-failure happens.
    """
    paused: builtins.bool
    """If true, do not take any actions based on the schedule spec."""
    limited_actions: builtins.bool
    """If limited_actions is true, decrement remaining_actions after each action, and do
    not take any more scheduled actions if remaining_actions is zero. Actions may still
    be taken by explicit request. Skipped actions (due to overlap policy) do not count
    against remaining actions.
    """
    remaining_actions: builtins.int
    def __init__(
        self,
        *,
        notes: builtins.str = ...,
        paused: builtins.bool = ...,
        limited_actions: builtins.bool = ...,
        remaining_actions: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "limited_actions",
            b"limited_actions",
            "notes",
            b"notes",
            "paused",
            b"paused",
            "remaining_actions",
            b"remaining_actions",
        ],
    ) -> None: ...

global___ScheduleState = ScheduleState

class TriggerImmediatelyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OVERLAP_POLICY_FIELD_NUMBER: builtins.int
    overlap_policy: temporalio.api.enums.v1.schedule_pb2.ScheduleOverlapPolicy.ValueType
    """Override overlap policy for this one request."""
    def __init__(
        self,
        *,
        overlap_policy: temporalio.api.enums.v1.schedule_pb2.ScheduleOverlapPolicy.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["overlap_policy", b"overlap_policy"]
    ) -> None: ...

global___TriggerImmediatelyRequest = TriggerImmediatelyRequest

class BackfillRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    OVERLAP_POLICY_FIELD_NUMBER: builtins.int
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time range to evaluate schedule in."""
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    overlap_policy: temporalio.api.enums.v1.schedule_pb2.ScheduleOverlapPolicy.ValueType
    """Override overlap policy for this request."""
    def __init__(
        self,
        *,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        end_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        overlap_policy: temporalio.api.enums.v1.schedule_pb2.ScheduleOverlapPolicy.ValueType = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "end_time", b"end_time", "start_time", b"start_time"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "end_time",
            b"end_time",
            "overlap_policy",
            b"overlap_policy",
            "start_time",
            b"start_time",
        ],
    ) -> None: ...

global___BackfillRequest = BackfillRequest

class SchedulePatch(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRIGGER_IMMEDIATELY_FIELD_NUMBER: builtins.int
    BACKFILL_REQUEST_FIELD_NUMBER: builtins.int
    PAUSE_FIELD_NUMBER: builtins.int
    UNPAUSE_FIELD_NUMBER: builtins.int
    @property
    def trigger_immediately(self) -> global___TriggerImmediatelyRequest:
        """If set, trigger one action immediately."""
    @property
    def backfill_request(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___BackfillRequest
    ]:
        """If set, runs though the specified time period(s) and takes actions as if that time
        passed by right now, all at once. The overlap policy can be overridden for the
        scope of the backfill.
        """
    pause: builtins.str
    """If set, change the state to paused or unpaused (respectively) and set the
    notes field to the value of the string.
    """
    unpause: builtins.str
    def __init__(
        self,
        *,
        trigger_immediately: global___TriggerImmediatelyRequest | None = ...,
        backfill_request: collections.abc.Iterable[global___BackfillRequest]
        | None = ...,
        pause: builtins.str = ...,
        unpause: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "trigger_immediately", b"trigger_immediately"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "backfill_request",
            b"backfill_request",
            "pause",
            b"pause",
            "trigger_immediately",
            b"trigger_immediately",
            "unpause",
            b"unpause",
        ],
    ) -> None: ...

global___SchedulePatch = SchedulePatch

class ScheduleInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTION_COUNT_FIELD_NUMBER: builtins.int
    MISSED_CATCHUP_WINDOW_FIELD_NUMBER: builtins.int
    OVERLAP_SKIPPED_FIELD_NUMBER: builtins.int
    RUNNING_WORKFLOWS_FIELD_NUMBER: builtins.int
    RECENT_ACTIONS_FIELD_NUMBER: builtins.int
    FUTURE_ACTION_TIMES_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    INVALID_SCHEDULE_ERROR_FIELD_NUMBER: builtins.int
    action_count: builtins.int
    """Number of actions taken so far."""
    missed_catchup_window: builtins.int
    """Number of times a scheduled action was skipped due to missing the catchup window."""
    overlap_skipped: builtins.int
    """Number of skipped actions due to overlap."""
    @property
    def running_workflows(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        temporalio.api.common.v1.message_pb2.WorkflowExecution
    ]:
        """Currently-running workflows started by this schedule. (There might be
        more than one if the overlap policy allows overlaps.)
        Note that the run_ids in here are the original execution run ids as
        started by the schedule. If the workflows retried, did continue-as-new,
        or were reset, they might still be running but with a different run_id.
        """
    @property
    def recent_actions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ScheduleActionResult
    ]:
        """Most recent ten actual action times (including manual triggers)."""
    @property
    def future_action_times(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.timestamp_pb2.Timestamp
    ]:
        """Next ten scheduled action times."""
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamps of schedule creation and last update."""
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    invalid_schedule_error: builtins.str
    """Error for invalid schedule. If this is set, no actions will be taken."""
    def __init__(
        self,
        *,
        action_count: builtins.int = ...,
        missed_catchup_window: builtins.int = ...,
        overlap_skipped: builtins.int = ...,
        running_workflows: collections.abc.Iterable[
            temporalio.api.common.v1.message_pb2.WorkflowExecution
        ]
        | None = ...,
        recent_actions: collections.abc.Iterable[global___ScheduleActionResult]
        | None = ...,
        future_action_times: collections.abc.Iterable[
            google.protobuf.timestamp_pb2.Timestamp
        ]
        | None = ...,
        create_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        update_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        invalid_schedule_error: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "create_time", b"create_time", "update_time", b"update_time"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "action_count",
            b"action_count",
            "create_time",
            b"create_time",
            "future_action_times",
            b"future_action_times",
            "invalid_schedule_error",
            b"invalid_schedule_error",
            "missed_catchup_window",
            b"missed_catchup_window",
            "overlap_skipped",
            b"overlap_skipped",
            "recent_actions",
            b"recent_actions",
            "running_workflows",
            b"running_workflows",
            "update_time",
            b"update_time",
        ],
    ) -> None: ...

global___ScheduleInfo = ScheduleInfo

class Schedule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPEC_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    POLICIES_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    @property
    def spec(self) -> global___ScheduleSpec: ...
    @property
    def action(self) -> global___ScheduleAction: ...
    @property
    def policies(self) -> global___SchedulePolicies: ...
    @property
    def state(self) -> global___ScheduleState: ...
    def __init__(
        self,
        *,
        spec: global___ScheduleSpec | None = ...,
        action: global___ScheduleAction | None = ...,
        policies: global___SchedulePolicies | None = ...,
        state: global___ScheduleState | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "action",
            b"action",
            "policies",
            b"policies",
            "spec",
            b"spec",
            "state",
            b"state",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "action",
            b"action",
            "policies",
            b"policies",
            "spec",
            b"spec",
            "state",
            b"state",
        ],
    ) -> None: ...

global___Schedule = Schedule

class ScheduleListInfo(google.protobuf.message.Message):
    """ScheduleListInfo is an abbreviated set of values from Schedule and ScheduleInfo
    that's returned in ListSchedules.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPEC_FIELD_NUMBER: builtins.int
    WORKFLOW_TYPE_FIELD_NUMBER: builtins.int
    NOTES_FIELD_NUMBER: builtins.int
    PAUSED_FIELD_NUMBER: builtins.int
    RECENT_ACTIONS_FIELD_NUMBER: builtins.int
    FUTURE_ACTION_TIMES_FIELD_NUMBER: builtins.int
    @property
    def spec(self) -> global___ScheduleSpec:
        """From spec:
        Some fields are too large/unimportant for the purpose of listing, so we'll clear them
        from this copy of spec: exclude_calendar, jitter, timezone_data.
        """
    @property
    def workflow_type(self) -> temporalio.api.common.v1.message_pb2.WorkflowType:
        """From action:
        Action is a oneof field, but we need to encode this in JSON and oneof fields don't work
        well with JSON. If action is start_workflow, this is set:
        """
    notes: builtins.str
    """From state:"""
    paused: builtins.bool
    @property
    def recent_actions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ScheduleActionResult
    ]:
        """From info (maybe fewer entries):"""
    @property
    def future_action_times(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.timestamp_pb2.Timestamp
    ]: ...
    def __init__(
        self,
        *,
        spec: global___ScheduleSpec | None = ...,
        workflow_type: temporalio.api.common.v1.message_pb2.WorkflowType | None = ...,
        notes: builtins.str = ...,
        paused: builtins.bool = ...,
        recent_actions: collections.abc.Iterable[global___ScheduleActionResult]
        | None = ...,
        future_action_times: collections.abc.Iterable[
            google.protobuf.timestamp_pb2.Timestamp
        ]
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "spec", b"spec", "workflow_type", b"workflow_type"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "future_action_times",
            b"future_action_times",
            "notes",
            b"notes",
            "paused",
            b"paused",
            "recent_actions",
            b"recent_actions",
            "spec",
            b"spec",
            "workflow_type",
            b"workflow_type",
        ],
    ) -> None: ...

global___ScheduleListInfo = ScheduleListInfo

class ScheduleListEntry(google.protobuf.message.Message):
    """ScheduleListEntry is returned by ListSchedules."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCHEDULE_ID_FIELD_NUMBER: builtins.int
    MEMO_FIELD_NUMBER: builtins.int
    SEARCH_ATTRIBUTES_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    schedule_id: builtins.str
    @property
    def memo(self) -> temporalio.api.common.v1.message_pb2.Memo: ...
    @property
    def search_attributes(
        self,
    ) -> temporalio.api.common.v1.message_pb2.SearchAttributes: ...
    @property
    def info(self) -> global___ScheduleListInfo: ...
    def __init__(
        self,
        *,
        schedule_id: builtins.str = ...,
        memo: temporalio.api.common.v1.message_pb2.Memo | None = ...,
        search_attributes: temporalio.api.common.v1.message_pb2.SearchAttributes
        | None = ...,
        info: global___ScheduleListInfo | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "info", b"info", "memo", b"memo", "search_attributes", b"search_attributes"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "info",
            b"info",
            "memo",
            b"memo",
            "schedule_id",
            b"schedule_id",
            "search_attributes",
            b"search_attributes",
        ],
    ) -> None: ...

global___ScheduleListEntry = ScheduleListEntry
