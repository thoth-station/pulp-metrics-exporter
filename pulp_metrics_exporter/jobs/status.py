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

"""Metrics related to Pulp's Python plugin."""

import logging
from urllib.parse import urljoin

import pulp_metrics_exporter.metrics as metrics

from .base import register_metric_job
from .base import MetricsBase
from ..configuration import Configuration

_LOGGER = logging.getLogger(__name__)


class PulpStatusMetrics(MetricsBase):
    """Class to check Pulp status."""

    @classmethod
    @register_metric_job
    def get_status_connection(cls) -> None:
        """Check connection to the status endpoint."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/status"))
        # 1 means alarm.
        metrics.pulp_status_connection.set(int(response.status_code != 200))

    @classmethod
    @register_metric_job
    def get_status_workers_count(cls) -> None:
        """Check the number of workers available."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/status"))
        response.raise_for_status()
        metrics.pulp_status_workers_count.set(len(response.json()["online_workers"]))

    @classmethod
    @register_metric_job
    def get_status_database_connection(cls) -> None:
        """Check the database connection."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/status"))
        # 1 means alarm.
        response.raise_for_status()
        metrics.pulp_status_database_connection.set(response.json()["database_connection"]["connected"] is False)

    @classmethod
    @register_metric_job
    def get_status_redis_connection(cls) -> None:
        """Check the Redis connection."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/status"))
        response.raise_for_status()
        # 1 means alarm.
        metrics.pulp_status_database_connection.set(response.json()["redis_connection"]["connected"] is False)
