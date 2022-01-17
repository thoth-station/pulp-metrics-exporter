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


class PulpPythonPluginMetrics(MetricsBase):
    """Class to check Pulp specific metrics for the Pulp's Python plugin."""

    @classmethod
    @register_metric_job
    def get_python_packages_count(cls) -> None:
        """Get the total number of Python packages available."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(
            urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/content/python/packages?limit=1")
        )
        response.raise_for_status()
        metrics.pulp_python_packages_count.set(response.json()["count"])

    @classmethod
    @register_metric_job
    def get_python_distributions_count(cls) -> None:
        """Get the total number of Python distributions available."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(
            urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/distributions/python/pypi?limit=1")
        )
        response.raise_for_status()
        metrics.pulp_python_distributions_count.set(response.json()["count"])

    @classmethod
    @register_metric_job
    def get_python_publications_count(cls) -> None:
        """Get the total number of Python publications available."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(
            urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/publications/python/pypi?limit=1")
        )
        response.raise_for_status()
        metrics.pulp_python_publications_count.set(response.json()["count"])

    @classmethod
    @register_metric_job
    def get_python_remotes_count(cls) -> None:
        """Get the total number of Python remotes available."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/remotes/python/python?limit=1"))
        response.raise_for_status()
        metrics.pulp_python_remotes_count.set(response.json()["count"])

    @classmethod
    @register_metric_job
    def get_python_repositories_count(cls) -> None:
        """Get the total number of Python repositories available."""
        pulp_session = cls.get_pulp_session()
        response = pulp_session.get(
            urljoin(Configuration.PULP_BASE_URL, "/pulp/api/v3/repositories/python/python?limit=1")
        )
        response.raise_for_status()
        metrics.pulp_python_repositories_count.set(response.json()["count"])
