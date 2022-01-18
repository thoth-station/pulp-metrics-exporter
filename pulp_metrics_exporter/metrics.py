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

"""All metrics exposed by Pulp's metrics exporter."""

from pulp_metrics_exporter import __service_version__
from prometheus_client import Gauge


# Info Metric
metrics_exporter_info = Gauge(
    "pulp_metrics_exporter_info",
    "Thoth Metrics Exporter information",
    ["version"],
)
metrics_exporter_info.labels(__service_version__).inc()

# Status metrics.

pulp_status_connection = Gauge("pulp_status_connection", "Check connection to Pulp", [])

pulp_status_workers_count = Gauge("pulp_status_workers_count", "Number of online workers", [])

pulp_status_database_connection = Gauge(
    "pulp_status_database_connection", "Check Pulp's connection to the database", []
)

pulp_status_redis_connection = Gauge("pulp_status_redis_connection", "Check Pulp's connection to Redis", [])

# Task metrics

pulp_tasks_count = Gauge("pulp_tasks_count", "Number of tasks running in Pulp", [])

# Python plugin metrics.

pulp_python_packages_count = Gauge(
    "pulp_python_packages_count", "Number of Python packages available on Pulp Python", []
)

pulp_python_distributions_count = Gauge(
    "pulp_python_distributions_count", "Number of Python distributions available on Pulp Python", []
)

pulp_python_publications_count = Gauge(
    "pulp_python_publications_count", "Number of Python publications available on Pulp Python", []
)

pulp_python_remotes_count = Gauge("pulp_python_remotes_count", "Number of Python remotes available on Pulp Python", [])

pulp_python_repositories_count = Gauge(
    "pulp_python_repositories_count", "Number of Python repositories available on Pulp Python", []
)
