# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""PIDManager."""

from invenio_drafts_resources.services.pid_manager import PIDManager, \
    PIDManagerConfig

from .models import BibliographicRecord, BibliographicRecordDraft


class BibliographicPIDManagerConfig(PIDManagerConfig):
    """PID manager config."""

    draft_cls = BibliographicRecordDraft
    record_cls = BibliographicRecord


class BibliographicPIDManager(PIDManager):
    """PID manager."""

    default_config = BibliographicPIDManagerConfig
