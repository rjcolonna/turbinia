# -*- coding: utf-8 -*-
# Copyright 2019 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Job to finalize a request."""

from turbinia.evidence import FinalReport
from turbinia.jobs import interface
from turbinia.jobs import manager
from turbinia.workers.finalize_request import FinalizeRequestTask


class FinalizeRequestJob(interface.TurbiniaJob):
  """Runs request finalization Tasks."""
  # An empty evidence input here means that this Job will never get
  # automatically created.  This is generated by the TaskManager implicitly when
  # all of the other Jobs in the request have completed.
  evidence_input = []
  evidence_output = [FinalReport]

  NAME = 'FinalizeRequestJob'

  def __init__(self):
    super(FinalizeRequestJob, self).__init__()
    self.is_finalize_job = True

  def create_tasks(self, evidence):
    """Create finalize Tasks.

    Args:
      evidence (list[Evidence]): Evidence to process

    Returns:
      list[FinalizeRequestTask]: A list of FinalizeRequestTasks.
    """
    return [FinalizeRequestTask() for _ in evidence]


manager.JobsManager.RegisterJob(FinalizeRequestJob)
