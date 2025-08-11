# Checkmk MQTT Piggyback

Dieses Repository enthält ein Beispiel für eine Checkmk-Erweiterung, die Piggyback-Daten über MQTT verteilt.

## MKP bauen

1. Abhängigkeiten installieren und in das Projektverzeichnis wechseln.
2. Paket erstellen:
   ```bash
   cmk -v pack mkp
   ```
   Alternativ kann das `mkp`-Werkzeug genutzt werden:
   ```bash
   mkp package
   ```
   Nach dem Bauen befindet sich die Datei `cmk_mqtt_piggyback-<version>.mkp` im aktuellen Verzeichnis.

## Installation auf dem Checkmk-Server

1. Kopieren Sie das MKP auf den Zielserver.
2. Installieren Sie das Paket:
   ```bash
   cmk -v install mkp cmk_mqtt_piggyback-<version>.mkp
   ```
   oder
   ```bash
   mkp install cmk_mqtt_piggyback-<version>.mkp
   ```
3. Aktivieren Sie die Änderungen über die Weboberfläche.

## Installation auf dem Checkmk-Agenten

1. Nach der Installation enthält das Paket ein Agenten-Plugin unter `agents/plugins/cmk_mqtt_pighgyback.py`.
2. Kopieren Sie diese Datei auf den Zielhost nach `/usr/lib/check_mk_agent/plugins/` (Linux).
3. Machen Sie das Skript ausführbar:
   ```bash
   chmod +x /usr/lib/check_mk_agent/plugins/cmk_mqtt_pighgyback.py
   ```
4. Führen Sie einen Agenten-Update (`check_mk_agent`) aus, um die Piggyback-Daten zu prüfen.
