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

"""Metrics related to Pulp's tasks."""

import logging
from urllib.parse import urljoin

import pulp_metrics_exporter.metrics as metrics

from .base import register_metric_job
from .base import MetricsBase
from ..configuration import Configuration

_LOGGER = logging.getLogger(__name__)


class PulpTaskMetrics(MetricsBase):
    """Class to check Pulp task related metrics."""

    @classmethod
    @register_metric_job
    def get_status_connection(cls) -> None:
        """Check connection to the status endpoint."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/tasks?limit=1"))
        response.raise_for_status()
        metrics.pulp_tasks_count.set(response.json()["count"])
