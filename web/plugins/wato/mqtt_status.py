# WATO rule for MQTT status check

from cmk.gui.i18n import _
from cmk.gui.valuespec import Dictionary, Float, Tuple
from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    RulespecGroupCheckParametersApplications,
    rulespec_registry,
)


def _parameter_valuespec_mqtt_status():
    return Dictionary(
        elements=[
            (
                "metric_levels",
                Tuple(
                    title=_("Metric levels"),
                    elements=[
                        Float(title=_("Warning at"), default_value=80.0),
                        Float(title=_("Critical at"), default_value=90.0),
                    ],
                ),
            ),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name="mqtt_status",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_mqtt_status,
    )
)
