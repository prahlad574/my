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
"""Auto-generated from spec: urn:broadband-forum-org:tr-181-2-1."""

import core
from tr181_v2_0 import Device_v2_0


class Device_v2_1(Device_v2_0):
  """Represents Device_v2_1."""

  def __init__(self, **defaults):
    Device_v2_0.__init__(self, defaults=defaults)
    self.Export(objects=['DeviceInfo',
                         'Firewall',
                         'ManagementServer',
                         'NSLookupDiagnostics',
                         'SoftwareModules'])

  class DeviceInfo(Device_v2_0.DeviceInfo):
    """Represents Device_v2_1.DeviceInfo."""

    def __init__(self, **defaults):
      Device_v2_0.DeviceInfo.__init__(self, defaults=defaults)
      self.Export(params=['ProcessorNumberOfEntries',
                          'VendorLogFileNumberOfEntries'],
                  objects=['TemperatureStatus'],
                  lists=['Processor',
                         'VendorLogFile'])

    class Processor(core.Exporter):
      """Represents Device_v2_1.DeviceInfo.Processor.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Architecture'])

    class TemperatureStatus(Device_v2_0.DeviceInfo.TemperatureStatus):
      """Represents Device_v2_1.DeviceInfo.TemperatureStatus."""

      def __init__(self, **defaults):
        Device_v2_0.DeviceInfo.TemperatureStatus.__init__(self, defaults=defaults)
        self.Export(lists=['TemperatureSensor'])

      class TemperatureSensor(Device_v2_0.DeviceInfo.TemperatureStatus.TemperatureSensor):
        """Represents Device_v2_1.DeviceInfo.TemperatureStatus.TemperatureSensor.{i}."""

        def __init__(self, **defaults):
          Device_v2_0.DeviceInfo.TemperatureStatus.TemperatureSensor.__init__(self, defaults=defaults)
          self.Export(params=['HighAlarmValue',
                              'LowAlarmValue',
                              'PollingInterval'])

    class VendorLogFile(core.Exporter):
      """Represents Device_v2_1.DeviceInfo.VendorLogFile.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Alias',
                            'MaximumSize',
                            'Name',
                            'Persistent'])

  class Firewall(Device_v2_0.Firewall):
    """Represents Device_v2_1.Firewall."""

    def __init__(self, **defaults):
      Device_v2_0.Firewall.__init__(self, defaults=defaults)
      self.Export(params=['Config'])

  class ManagementServer(Device_v2_0.ManagementServer):
    """Represents Device_v2_1.ManagementServer."""

    def __init__(self, **defaults):
      Device_v2_0.ManagementServer.__init__(self, defaults=defaults)
      self.Export(objects=['DUStateChangeComplPolicy'])

    class DUStateChangeComplPolicy(core.Exporter):
      """Represents Device_v2_1.ManagementServer.DUStateChangeComplPolicy."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Enable',
                            'FaultCodeFilter',
                            'OperationTypeFilter',
                            'ResultTypeFilter'])

  class NSLookupDiagnostics(Device_v2_0.NSLookupDiagnostics):
    """Represents Device_v2_1.NSLookupDiagnostics."""

    def __init__(self, **defaults):
      Device_v2_0.NSLookupDiagnostics.__init__(self, defaults=defaults)
      self.Export(lists=['Result'])

    class Result(Device_v2_0.NSLookupDiagnostics.Result):
      """Represents Device_v2_1.NSLookupDiagnostics.Result.{i}."""

      def __init__(self, **defaults):
        Device_v2_0.NSLookupDiagnostics.Result.__init__(self, defaults=defaults)
        self.Export(params=['Status'])

  class SoftwareModules(core.Exporter):
    """Represents Device_v2_1.SoftwareModules."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['DeploymentUnitNumberOfEntries',
                          'ExecEnvNumberOfEntries',
                          'ExecutionUnitNumberOfEntries'],
                  lists=['DeploymentUnit',
                         'ExecEnv',
                         'ExecutionUnit'])

    class DeploymentUnit(core.Exporter):
      """Represents Device_v2_1.SoftwareModules.DeploymentUnit.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Alias',
                            'DUID',
                            'Description',
                            'ExecutionEnvRef',
                            'ExecutionUnitList',
                            'Name',
                            'Resolved',
                            'Status',
                            'URL',
                            'UUID',
                            'Vendor',
                            'VendorConfigList',
                            'VendorLogList',
                            'Version'])

    class ExecEnv(core.Exporter):
      """Represents Device_v2_1.SoftwareModules.ExecEnv.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['ActiveExecutionUnits',
                            'Alias',
                            'AllocatedDiskSpace',
                            'AllocatedMemory',
                            'AvailableDiskSpace',
                            'AvailableMemory',
                            'CurrentRunLevel',
                            'Enable',
                            'InitialRunLevel',
                            'Name',
                            'ParentExecEnv',
                            'ProcessorRefList',
                            'RequestedRunLevel',
                            'Reset',
                            'Status',
                            'Type',
                            'Vendor',
                            'Version'])

    class ExecutionUnit(core.Exporter):
      """Represents Device_v2_1.SoftwareModules.ExecutionUnit.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Alias',
                            'AssociatedProcessList',
                            'AutoStart',
                            'Description',
                            'DiskSpaceInUse',
                            'EUID',
                            'ExecEnvLabel',
                            'ExecutionEnvRef',
                            'ExecutionFaultCode',
                            'ExecutionFaultMessage',
                            'MemoryInUse',
                            'Name',
                            'References',
                            'RequestedState',
                            'RunLevel',
                            'Status',
                            'SupportedDataModelList',
                            'Vendor',
                            'VendorConfigList',
                            'VendorLogList',
                            'Version'],
                    objects=['Extensions'])

      class Extensions(core.Exporter):
        """Represents Device_v2_1.SoftwareModules.ExecutionUnit.{i}.Extensions."""
        pass


if __name__ == '__main__':
  print core.DumpSchema(Device_v2_1)
