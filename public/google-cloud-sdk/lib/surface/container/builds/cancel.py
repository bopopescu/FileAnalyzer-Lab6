# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Cancel build command."""

from googlecloudsdk.api_lib.cloudbuild import cloudbuild_util
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.container.builds import flags
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources


class Cancel(base.Command):
  """Cancel an ongoing build."""

  @staticmethod
  def Args(parser):
    parser.add_argument(
        'builds',
        completer=flags.BuildsCompleter,
        nargs='+',  # Accept multiple builds.
        help='IDs of builds to cancel')
    parser.display_info.AddFormat(None)

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Some value that we want to have printed later.
    """

    client = cloudbuild_util.GetClientInstance()
    messages = cloudbuild_util.GetMessagesModule()

    cancelled = []
    for build in args.builds:
      build_ref = resources.REGISTRY.Parse(
          build,
          params={'projectId': properties.VALUES.core.project.GetOrFail},
          collection='cloudbuild.projects.builds')
      cancelled_build = client.projects_builds.Cancel(
          messages.CloudbuildProjectsBuildsCancelRequest(
              projectId=build_ref.projectId,
              id=build_ref.id))
      log.status.write('Cancelled [{r}].\n'.format(r=str(build_ref)))
      cancelled.append(cancelled_build)
    return cancelled
