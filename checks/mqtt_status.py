#!/usr/bin/env python3
"""Checkmk check plugin for MQTT status."""

import json
from typing import Any, Mapping

from .agent_based_api.v1 import (
    Metric,
    Result,
    Service,
    State,
    register,
)


def parse_mqtt_status(string_table):
    """Parse JSON payload from <<<mqtt_status>>> section."""
    if not string_table:
        return {}
    line = " ".join(string_table[0])
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return {}


register.agent_section(
    name="mqtt_status",
    parse_function=parse_mqtt_status,
)


def discovery_mqtt_status(section: Mapping[str, Any]):
    if section:
        yield Service()


def check_mqtt_status(params: Mapping[str, Any], section: Mapping[str, Any]):
    status = str(section.get("status", "UNKNOWN"))
    metric_value = section.get("metric")

    state_map = {
        "OK": State.OK,
        "WARN": State.WARN,
        "CRIT": State.CRIT,
    }
    state = state_map.get(status.upper(), State.UNKNOWN)
    summary = f"Status {status}"

    if metric_value is not None:
        metric_val = float(metric_value)
        warn, crit = params.get("metric_levels", (None, None))
        yield Metric("metric", metric_val, levels=(warn, crit))
        summary += f", metric {metric_val}"
        if crit is not None and metric_val >= crit:
            state = State.CRIT
        elif warn is not None and metric_val >= warn and state is State.OK:
            state = State.WARN

    yield Result(state=state, summary=summary)


register.check_plugin(
    name="mqtt_status",
    service_name="MQTT Status",
    discovery_function=discovery_mqtt_status,
    check_function=check_mqtt_status,
    check_default_parameters={"metric_levels": (80.0, 90.0)},
    check_ruleset_name="mqtt_status",
)
