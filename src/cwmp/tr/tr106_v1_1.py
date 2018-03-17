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
"""Auto-generated from spec: urn:broadband-forum-org:tr-106-1-1."""

import core
from tr106_v1_0 import Device_v1_0


class Device_v1_1(Device_v1_0):
  """Represents Device_v1_1."""

  def __init__(self, **defaults):
    Device_v1_0.__init__(self, defaults=defaults)
    self.Export(objects=['Config',
                         'DeviceInfo',
                         'LAN',
                         'ManagementServer',
                         'Time',
                         'UserInterface'])

  class Config(Device_v1_0.Config):
    """Represents Device_v1_1.Config."""

    def __init__(self, **defaults):
      Device_v1_0.Config.__init__(self, defaults=defaults)
      self.Export(params=['ConfigFile',
                          'PersistentData'])

  class DeviceInfo(Device_v1_0.DeviceInfo):
    """Represents Device_v1_1.DeviceInfo."""

    def __init__(self, **defaults):
      Device_v1_0.DeviceInfo.__init__(self, defaults=defaults)
      self.Export(params=['AdditionalHardwareVersion',
                          'AdditionalSoftwareVersion',
                          'EnabledOptions',
                          'FirstUseDate'])

  class LAN(Device_v1_0.LAN):
    """Represents Device_v1_1.LAN."""

    def __init__(self, **defaults):
      Device_v1_0.LAN.__init__(self, defaults=defaults)
      self.Export(params=['AddressingType',
                          'DNSServers',
                          'DefaultGateway',
                          'IPAddress',
                          'SubnetMask'],
                  objects=['IPPingDiagnostics',
                           'TraceRouteDiagnostics'],
                  lists=['DHCPOption'])

    class DHCPOption(Device_v1_0.LAN.DHCPOption):
      """Represents Device_v1_1.LAN.DHCPOption.{i}."""

      def __init__(self, **defaults):
        Device_v1_0.LAN.DHCPOption.__init__(self, defaults=defaults)
        self.Export(params=['Value'])

    class IPPingDiagnostics(Device_v1_0.LAN.IPPingDiagnostics):
      """Represents Device_v1_1.LAN.IPPingDiagnostics."""

      def __init__(self, **defaults):
        Device_v1_0.LAN.IPPingDiagnostics.__init__(self, defaults=defaults)
        self.Export(params=['DSCP',
                            'DiagnosticsState'])

    class TraceRouteDiagnostics(Device_v1_0.LAN.TraceRouteDiagnostics):
      """Represents Device_v1_1.LAN.TraceRouteDiagnostics."""

      def __init__(self, **defaults):
        Device_v1_0.LAN.TraceRouteDiagnostics.__init__(self, defaults=defaults)
        self.Export(params=['DSCP',
                            'DiagnosticsState',
                            'NumberOfRouteHops',
                            'ResponseTime'])

  class ManagementServer(Device_v1_0.ManagementServer):
    """Represents Device_v1_1.ManagementServer."""

    def __init__(self, **defaults):
      Device_v1_0.ManagementServer.__init__(self, defaults=defaults)
      self.Export(params=['ConnectionRequestURL',
                          'DownloadProgressURL',
                          'KickURL',
                          'NATDetected',
                          'Password',
                          'PeriodicInformEnable',
                          'PeriodicInformTime',
                          'STUNEnable',
                          'STUNMaximumKeepAlivePeriod',
                          'STUNMinimumKeepAlivePeriod',
                          'STUNPassword',
                          'STUNServerAddress',
                          'STUNServerPort',
                          'STUNUsername',
                          'UDPConnectionRequestAddress',
                          'UDPConnectionRequestAddressNotificationLimit',
                          'URL',
                          'UpgradesManaged',
                          'Username'])

  class Time(Device_v1_0.Time):
    """Represents Device_v1_1.Time."""
    pass

  class UserInterface(Device_v1_0.UserInterface):
    """Represents Device_v1_1.UserInterface."""

    def __init__(self, **defaults):
      Device_v1_0.UserInterface.__init__(self, defaults=defaults)
      self.Export(params=['PasswordRequired',
                          'PasswordUserSelectable'])


if __name__ == '__main__':
  print core.DumpSchema(Device_v1_1)
