# Copyright 2018 Google Inc. All Rights Reserved.
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
"""Command for bigtable instances remove-iam-policy-binding."""

from googlecloudsdk.api_lib.bigtable import util
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.bigtable import arguments
from googlecloudsdk.command_lib.bigtable import iam
from googlecloudsdk.command_lib.iam import iam_util


@base.Hidden
class RemoveIamPolicyBinding(base.Command):
  """Remove an IAM policy binding from a Cloud Spanner instance."""

  @staticmethod
  def Args(parser):
    """Register flags for this command."""
    arguments.AddInstanceResourceArg(parser,
                                     'to remove the IAM policy binding from')
    iam_util.AddArgsForRemoveIamPolicyBinding(parser)

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      A IAM policy message.
    """
    instance_ref = util.GetInstanceRef(args.instance)
    return iam.RemoveInstanceIamPolicyBinding(instance_ref, args.member,
                                              args.role)
