#!/usr/bin/python
# Copyright 2011 Google Inc. All Rights Reserved.
#
# AUTO-GENERATED BY parse-schema.py
#
# DO NOT EDIT!!
#
#pylint: disable-msg=C6202
#pylint: disable-msg=C6409
#pylint: disable-msg=C6310
# These should not actually be necessary (bugs in gpylint?):
#pylint: disable-msg=E1101
#pylint: disable-msg=W0231
#
"""Auto-generated from spec: urn:broadband-forum-org:tr-140-1-0."""

import core


class StorageService_v1_0(core.Exporter):
  """Represents StorageService_v1_0."""

  def __init__(self, **defaults):
    core.Exporter.__init__(self, defaults=defaults)
    self.Export(lists=['StorageService'])

  class StorageService(core.Exporter):
    """Represents StorageService_v1_0.StorageService.{i}."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['Enable',
                          'LogicalVolumeNumberOfEntries',
                          'PhysicalMediumNumberOfEntries',
                          'StorageArrayNumberOfEntries',
                          'UserAccountNumberOfEntries',
                          'UserGroupNumberOfEntries'],
                  objects=['Capabilities',
                           'FTPServer',
                           'HTTPSServer',
                           'HTTPServer',
                           'NetInfo',
                           'NetworkServer',
                           'SFTPServer'],
                  lists=['LogicalVolume',
                         'PhysicalMedium',
                         'StorageArray',
                         'UserAccount',
                         'UserGroup'])

    class Capabilities(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.Capabilities."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['FTPCapable',
                            'HTTPCapable',
                            'HTTPSCapable',
                            'HTTPWritable',
                            'SFTPCapable',
                            'SupportedFileSystemTypes',
                            'SupportedNetworkProtocols',
                            'SupportedRaidTypes',
                            'VolumeEncryptionCapable'])

    class FTPServer(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.FTPServer."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Enable',
                            'IdleTime',
                            'MaxNumUsers',
                            'PortNumber',
                            'Status'],
                    objects=['AnonymousUser'])

      class AnonymousUser(core.Exporter):
        """Represents StorageService_v1_0.StorageService.{i}.FTPServer.AnonymousUser."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['Enable',
                              'ReadOnlyAccess',
                              'StartingFolder'])

    class HTTPSServer(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.HTTPSServer."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['AuthenticationReq',
                            'Enable',
                            'HTTPWritingEnabled',
                            'IdleTime',
                            'MaxNumUsers',
                            'PortNumber',
                            'Status'])

    class HTTPServer(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.HTTPServer."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['AuthenticationReq',
                            'Enable',
                            'HTTPWritingEnabled',
                            'IdleTime',
                            'MaxNumUsers',
                            'PortNumber',
                            'Status'])

    class LogicalVolume(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.LogicalVolume.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Capacity',
                            'Enable',
                            'Encrypted',
                            'FileSystem',
                            'FolderNumberOfEntries',
                            'Name',
                            'PhysicalReference',
                            'Status',
                            'ThresholdLimit',
                            'ThresholdReached',
                            'UsedSpace'],
                    lists=['Folder'])

      class Folder(core.Exporter):
        """Represents StorageService_v1_0.StorageService.{i}.LogicalVolume.{i}.Folder.{i}."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['Enable',
                              'GroupAccessNumberOfEntries',
                              'Name',
                              'UserAccessNumberOfEntries',
                              'UserAccountAccess'],
                      objects=['Quota'],
                      lists=['GroupAccess',
                             'UserAccess'])

        class GroupAccess(core.Exporter):
          """Represents StorageService_v1_0.StorageService.{i}.LogicalVolume.{i}.Folder.{i}.GroupAccess.{i}."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['GroupReference',
                                'Permissions'])

        class Quota(core.Exporter):
          """Represents StorageService_v1_0.StorageService.{i}.LogicalVolume.{i}.Folder.{i}.Quota."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['Capacity',
                                'Enable',
                                'ThresholdLimit',
                                'ThresholdReached',
                                'UsedSpace'])

        class UserAccess(core.Exporter):
          """Represents StorageService_v1_0.StorageService.{i}.LogicalVolume.{i}.Folder.{i}.UserAccess.{i}."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['Permissions',
                                'UserReference'])

    class NetInfo(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.NetInfo."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['DomainName',
                            'HostName'])

    class NetworkServer(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.NetworkServer."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['AFPEnable',
                            'NFSEnable',
                            'NetworkProtocolAuthReq',
                            'SMBEnable'])

    class PhysicalMedium(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.PhysicalMedium.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Capacity',
                            'ConnectionType',
                            'FirmwareVersion',
                            'Health',
                            'HotSwappable',
                            'Model',
                            'Name',
                            'Removable',
                            'SMARTCapable',
                            'SerialNumber',
                            'Status',
                            'Uptime',
                            'Vendor'])

    class SFTPServer(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.SFTPServer."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Enable',
                            'IdleTime',
                            'MaxNumUsers',
                            'PortNumber',
                            'Status'])

    class StorageArray(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.StorageArray.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Enable',
                            'Name',
                            'PhysicalMediumReference',
                            'RaidType',
                            'Status',
                            'UsableCapacity'])

    class UserAccount(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.UserAccount.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['AllowFTPAccess',
                            'AllowHTTPAccess',
                            'Enable',
                            'Password',
                            'UserGroupParticipation',
                            'Username'])

    class UserGroup(core.Exporter):
      """Represents StorageService_v1_0.StorageService.{i}.UserGroup.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Enable',
                            'GroupName'])


if __name__ == '__main__':
  print core.DumpSchema(StorageService_v1_0)
