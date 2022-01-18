#!/usr/bin/env python3
# pulp-metrics-exporter
# Copyright(C) 2022 Fridolin Pokorny
# Based on Thoth's metrics-exporter code.
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Configuration of Pulp's metrics-exporter."""

import logging
import os
from prometheus_api_client import PrometheusConnect

_LOGGER = logging.getLogger(__name__)


class Configuration:
    """Configuration of Pulp's metrics-exporter."""

    # Prometheus
    URL = os.environ["PROMETHEUS_HOST_URL"]
    PROMETHEUS_SERVICE_ACCOUNT_TOKEN = os.environ["PROMETHEUS_SERVICE_ACCOUNT_TOKEN"]
    HEADERS = {"Authorization": f"bearer {PROMETHEUS_SERVICE_ACCOUNT_TOKEN}"}
    PROM = PrometheusConnect(url=URL, disable_ssl=True, headers=HEADERS)

    # Pulp
    PULP_HOST = os.environ["PULP_HOST"]
    PULP_BASE_URL = f"https://{PULP_HOST}"  # Scheme is always HTTPS.
    PULP_USERNAME = os.environ["PULP_USERNAME"]
    PULP_PASSWORD = os.environ["PULP_PASSWORD"]
