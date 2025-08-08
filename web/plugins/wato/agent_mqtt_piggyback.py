# web/plugins/wato/agent_mqtt_piggyback.py

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    TextInput,
)
from cmk.gui.plugins.wato.agent_bakery import AgentRuleParameter

agent_mqtt_piggyback_parameters = Dictionary(
    elements=[
        ("mqtt_host", TextInput(
            title=_("MQTT Broker Host"),
            help=_("Hostname oder IP des MQTT-Brokers"),
        )),
        ("mqtt_port", TextInput(
            title=_("MQTT Broker Port"),
            default_value="1883",
        )),
        ("mqtt_topics", TextInput(
            title=_("MQTT Topics (Kommagetrennt)"),
            help=_("z.B. sensor/+/status, oder mehrere Topics durch Komma getrennt."),
        )),
    ]
)

register_rule(
    "agent_mqtt_piggyback",
    _("Agent MQTT Piggyback"),
    agent_mqtt_piggyback_parameters,
    group="agent_access",
)
