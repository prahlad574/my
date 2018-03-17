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
"""Auto-generated from spec: urn:broadband-forum-org:tr-181-2-4."""

import core
from tr181_v2_3 import Device_v2_3


class Device_v2_4(Device_v2_3):
  """Represents Device_v2_4."""

  def __init__(self, **defaults):
    Device_v2_3.__init__(self, defaults=defaults)
    self.Export(objects=['Device',
                         'DeviceInfo',
                         'FAP',
                         'FaultMgmt',
                         'Security',
                         'SoftwareModules'])

  class Device(Device_v2_3.Device):
    """Represents Device_v2_4.Device."""

    def __init__(self, **defaults):
      Device_v2_3.Device.__init__(self, defaults=defaults)
      self.Export(params=['RootDataModelVersion'],
                  objects=['Bridging',
                           'DHCPv6',
                           'DSLite',
                           'Ethernet',
                           'Firewall',
                           'Ghn',
                           'NAT',
                           'Optical',
                           'WiFi'])

    class Bridging(Device_v2_3.Device.Bridging):
      """Represents Device_v2_4.Device.Bridging."""

      def __init__(self, **defaults):
        Device_v2_3.Device.Bridging.__init__(self, defaults=defaults)
        self.Export(lists=['Filter'])

      class Filter(Device_v2_3.Device.Bridging.Filter):
        """Represents Device_v2_4.Device.Bridging.Filter.{i}."""

        def __init__(self, **defaults):
          Device_v2_3.Device.Bridging.Filter.__init__(self, defaults=defaults)
          self.Export(params=['DestMACFromClientIDFilter',
                              'SourceMACFromClientIDFilter'])

    class DHCPv6(Device_v2_3.Device.DHCPv6):
      """Represents Device_v2_4.Device.DHCPv6."""

      def __init__(self, **defaults):
        Device_v2_3.Device.DHCPv6.__init__(self, defaults=defaults)
        self.Export(objects=['Server'])

      class Server(Device_v2_3.Device.DHCPv6.Server):
        """Represents Device_v2_4.Device.DHCPv6.Server."""

        def __init__(self, **defaults):
          Device_v2_3.Device.DHCPv6.Server.__init__(self, defaults=defaults)
          self.Export(lists=['Pool'])

        class Pool(Device_v2_3.Device.DHCPv6.Server.Pool):
          """Represents Device_v2_4.Device.DHCPv6.Server.Pool.{i}."""

          def __init__(self, **defaults):
            Device_v2_3.Device.DHCPv6.Server.Pool.__init__(self, defaults=defaults)
            self.Export(params=['DUID'])

    class DSLite(Device_v2_3.Device.DSLite):
      """Represents Device_v2_4.Device.DSLite."""

      def __init__(self, **defaults):
        Device_v2_3.Device.DSLite.__init__(self, defaults=defaults)
        self.Export(lists=['InterfaceSetting'])

      class InterfaceSetting(Device_v2_3.Device.DSLite.InterfaceSetting):
        """Represents Device_v2_4.Device.DSLite.InterfaceSetting.{i}."""

        def __init__(self, **defaults):
          Device_v2_3.Device.DSLite.InterfaceSetting.__init__(self, defaults=defaults)
          self.Export(params=['EndpointAddress',
                              'EndpointName'])

    class Ethernet(Device_v2_3.Device.Ethernet):
      """Represents Device_v2_4.Device.Ethernet."""

      def __init__(self, **defaults):
        Device_v2_3.Device.Ethernet.__init__(self, defaults=defaults)
        self.Export(params=['RMONStatsNumberOfEntries'],
                    lists=['RMONStats'])

      class RMONStats(core.Exporter):
        """Represents Device_v2_4.Device.Ethernet.RMONStats.{i}."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['Alias',
                              'AllQueues',
                              'BroadcastPackets',
                              'Bytes',
                              'CRCErroredPackets',
                              'DropEvents',
                              'Enable',
                              'Interface',
                              'MulticastPackets',
                              'Name',
                              'OversizePackets',
                              'Packets',
                              'Packets1024to1518Bytes',
                              'Packets128to255Bytes',
                              'Packets256to511Bytes',
                              'Packets512to1023Bytes',
                              'Packets64Bytes',
                              'Packets65to127Bytes',
                              'Queue',
                              'Status',
                              'UndersizePackets',
                              'VLANID'])

    class Firewall(Device_v2_3.Device.Firewall):
      """Represents Device_v2_4.Device.Firewall."""

      def __init__(self, **defaults):
        Device_v2_3.Device.Firewall.__init__(self, defaults=defaults)
        self.Export(lists=['Chain'])

      class Chain(Device_v2_3.Device.Firewall.Chain):
        """Represents Device_v2_4.Device.Firewall.Chain.{i}."""

        def __init__(self, **defaults):
          Device_v2_3.Device.Firewall.Chain.__init__(self, defaults=defaults)
          self.Export(lists=['Rule'])

        class Rule(Device_v2_3.Device.Firewall.Chain.Rule):
          """Represents Device_v2_4.Device.Firewall.Chain.{i}.Rule.{i}."""
          pass

    class Ghn(core.Exporter):
      """Represents Device_v2_4.Device.Ghn."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['InterfaceNumberOfEntries'],
                    lists=['Interface'])

      class Interface(core.Exporter):
        """Represents Device_v2_4.Device.Ghn.Interface.{i}."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['Alias',
                              'AssociatedDeviceNumberOfEntries',
                              'ConnectionType',
                              'DeviceId',
                              'DomainId',
                              'DomainName',
                              'DomainNameIdentifier',
                              'Enable',
                              'FirmwareVersion',
                              'LastChange',
                              'LowerLayers',
                              'MACAddress',
                              'MaxBitRate',
                              'Name',
                              'NodeTypeDMCapable',
                              'NodeTypeDMConfig',
                              'NodeTypeDMStatus',
                              'NodeTypeSCCapable',
                              'NodeTypeSCStatus',
                              'Status',
                              'TargetDomainNames',
                              'Upstream'],
                      objects=['Stats'],
                      lists=['AssociatedDevice'])

        class AssociatedDevice(core.Exporter):
          """Represents Device_v2_4.Device.Ghn.Interface.{i}.AssociatedDevice.{i}."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['Active',
                                'DeviceId',
                                'MACAddress',
                                'RxPhyRate',
                                'TxPhyRate'])

        class Stats(core.Exporter):
          """Represents Device_v2_4.Device.Ghn.Interface.{i}.Stats."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['BroadcastPacketsReceived',
                                'BroadcastPacketsSent',
                                'BytesReceived',
                                'BytesSent',
                                'DiscardPacketsReceived',
                                'DiscardPacketsSent',
                                'ErrorsReceived',
                                'ErrorsSent',
                                'MulticastPacketsReceived',
                                'MulticastPacketsSent',
                                'PacketsReceived',
                                'PacketsSent',
                                'UnicastPacketsReceived',
                                'UnicastPacketsSent',
                                'UnknownProtoPacketsReceived'])

    class NAT(Device_v2_3.Device.NAT):
      """Represents Device_v2_4.Device.NAT."""

      def __init__(self, **defaults):
        Device_v2_3.Device.NAT.__init__(self, defaults=defaults)
        self.Export(lists=['PortMapping'])

      class PortMapping(Device_v2_3.Device.NAT.PortMapping):
        """Represents Device_v2_4.Device.NAT.PortMapping.{i}."""
        pass

    class Optical(core.Exporter):
      """Represents Device_v2_4.Device.Optical."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['InterfaceNumberOfEntries'],
                    lists=['Interface'])

      class Interface(core.Exporter):
        """Represents Device_v2_4.Device.Optical.Interface.{i}."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['Alias',
                              'Enable',
                              'LastChange',
                              'LowerLayers',
                              'LowerOpticalThreshold',
                              'LowerTransmitPowerThreshold',
                              'Name',
                              'OpticalSignalLevel',
                              'Status',
                              'TransmitOpticalLevel',
                              'UpperOpticalThreshold',
                              'UpperTransmitPowerThreshold',
                              'Upstream'],
                      objects=['Stats'])

        class Stats(core.Exporter):
          """Represents Device_v2_4.Device.Optical.Interface.{i}.Stats."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['BytesReceived',
                                'BytesSent',
                                'DiscardPacketsReceived',
                                'DiscardPacketsSent',
                                'ErrorsReceived',
                                'ErrorsSent',
                                'PacketsReceived',
                                'PacketsSent'])

    class WiFi(Device_v2_3.Device.WiFi):
      """Represents Device_v2_4.Device.WiFi."""

      def __init__(self, **defaults):
        Device_v2_3.Device.WiFi.__init__(self, defaults=defaults)
        self.Export(lists=['AccessPoint'])

      class AccessPoint(Device_v2_3.Device.WiFi.AccessPoint):
        """Represents Device_v2_4.Device.WiFi.AccessPoint.{i}."""

        def __init__(self, **defaults):
          Device_v2_3.Device.WiFi.AccessPoint.__init__(self, defaults=defaults)
          self.Export(params=['IsolationEnable',
                              'MaxAssociatedDevices'],
                      objects=['Security'])

        class Security(Device_v2_3.Device.WiFi.AccessPoint.Security):
          """Represents Device_v2_4.Device.WiFi.AccessPoint.{i}.Security."""

          def __init__(self, **defaults):
            Device_v2_3.Device.WiFi.AccessPoint.Security.__init__(self, defaults=defaults)
            self.Export(params=['Reset'])

  class DeviceInfo(Device_v2_3.DeviceInfo):
    """Represents Device_v2_4.DeviceInfo."""

    def __init__(self, **defaults):
      Device_v2_3.DeviceInfo.__init__(self, defaults=defaults)
      self.Export(params=['LocationNumberOfEntries'],
                  lists=['Location'])

    class Location(core.Exporter):
      """Represents Device_v2_4.DeviceInfo.Location.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['AcquiredTime',
                            'DataObject',
                            'ExternalProtocol',
                            'ExternalSource',
                            'Source'])

  class FAP(core.Exporter):
    """Represents Device_v2_4.FAP."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(objects=['ApplicationPlatform',
                           'GPS',
                           'PerfMgmt'])

    class ApplicationPlatform(core.Exporter):
      """Represents Device_v2_4.FAP.ApplicationPlatform."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['CurrentNumberofApplications',
                            'Enable',
                            'MaxNumberOfApplications',
                            'Status',
                            'Version'],
                    objects=['Capabilities',
                             'Control',
                             'Monitoring'])

      class Capabilities(core.Exporter):
        """Represents Device_v2_4.FAP.ApplicationPlatform.Capabilities."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['AccessLevelsSupported',
                              'AuthenticationMethodsSupported',
                              'FemtoAwarenessAPISupport',
                              'MMSAPISupport',
                              'PresenceApplicationSupport',
                              'QueryMMSDeliveryStatusSupport',
                              'QuerySMSDeliveryStatusSupport',
                              'SMSAPISupport',
                              'SendMMSTargetAddressType',
                              'SendSMSTargetAddressType',
                              'SubscribeToNotificationsOfMMSSentToApplicationSupport',
                              'SubscribeToNotificationsOfSMSSentToApplicationSupport',
                              'TerminalLocationAPISupport'])

      class Control(core.Exporter):
        """Represents Device_v2_4.FAP.ApplicationPlatform.Control."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['AuthenticationMethod',
                              'TunnelInst'],
                      objects=['FemtoAwareness',
                               'MMS',
                               'SMS',
                               'TerminalLocation'])

        class FemtoAwareness(core.Exporter):
          """Represents Device_v2_4.FAP.ApplicationPlatform.Control.FemtoAwareness."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['APIEnable',
                                'FemtozoneID',
                                'MaxAPIUsersNumber',
                                'NotificationsUserIdentifierMSISDN',
                                'QueryFemtocellResponseTimezone',
                                'QueueEnable',
                                'Queueing ',
                                'SubscribeToNotificationsResponseCallbackData'])

        class MMS(core.Exporter):
          """Represents Device_v2_4.FAP.ApplicationPlatform.Control.MMS."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['APIEnable',
                                'EnableQueryMMSDeliveryStatus',
                                'EnableSubscribeToNotificationsOfMessageSentToApplication',
                                'MaxAPIUsersNumber',
                                'MinSendMMSTimeInterval',
                                'QueueEnable',
                                'Queueing '])

        class SMS(core.Exporter):
          """Represents Device_v2_4.FAP.ApplicationPlatform.Control.SMS."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['APIEnable',
                                'EnableQuerySMSDeliveryStatus',
                                'EnableSubscribeToNotificationsOfMessageSentToApplication',
                                'MaxAPIUsersNumber',
                                'MinSendSMSTimeInterval',
                                'QueueEnable',
                                'Queueing '])

        class TerminalLocation(core.Exporter):
          """Represents Device_v2_4.FAP.ApplicationPlatform.Control.TerminalLocation."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['APIEnable',
                                'MaxAPIUsersNumber',
                                'QueryMobileLocationResponseAddress',
                                'QueryMobileLocationResponseAltitude',
                                'QueryMobileLocationResponseLongitudeLatitude',
                                'QueryMobileLocationResponseTimestamp',
                                'QueueEnable',
                                'Queueing '])

      class Monitoring(core.Exporter):
        """Represents Device_v2_4.FAP.ApplicationPlatform.Monitoring."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['AuthenticationRequestsReceived',
                              'AuthenticationRequestsRejected',
                              'Enable',
                              'MonitoringInterval'],
                      objects=['FemtoAwareness',
                               'MMS',
                               'SMS',
                               'TerminalLocation'])

        class FemtoAwareness(core.Exporter):
          """Represents Device_v2_4.FAP.ApplicationPlatform.Monitoring.FemtoAwareness."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['APIAvailable',
                                'APIUsers',
                                'QueueDiscarded',
                                'QueueNum',
                                'QueueReceived',
                                'QueueState'])

        class MMS(core.Exporter):
          """Represents Device_v2_4.FAP.ApplicationPlatform.Monitoring.MMS."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['APIAvailable',
                                'APIUsers',
                                'QueueDiscarded',
                                'QueueNum',
                                'QueueReceived',
                                'QueueState'])

        class SMS(core.Exporter):
          """Represents Device_v2_4.FAP.ApplicationPlatform.Monitoring.SMS."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['APIAvailable',
                                'APIUsers',
                                'QueueDiscarded',
                                'QueueNum',
                                'QueueReceived',
                                'QueueState'])

        class TerminalLocation(core.Exporter):
          """Represents Device_v2_4.FAP.ApplicationPlatform.Monitoring.TerminalLocation."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['APIAvailable',
                                'APIUsers',
                                'QueueDiscarded',
                                'QueueNum',
                                'QueueReceived',
                                'QueueState'])

    class GPS(core.Exporter):
      """Represents Device_v2_4.FAP.GPS."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['ContinuousGPS',
                            'ErrorDetails',
                            'GPSReset',
                            'LastScanTime',
                            'LastSuccessfulScanTime',
                            'LockedLatitude',
                            'LockedLongitude',
                            'NumberOfSatellites',
                            'PeriodicInterval',
                            'PeriodicTime',
                            'ScanOnBoot',
                            'ScanPeriodically',
                            'ScanStatus',
                            'ScanTimeout'],
                    objects=['AGPSServerConfig',
                             'ContinuousGPSStatus'])

      class AGPSServerConfig(core.Exporter):
        """Represents Device_v2_4.FAP.GPS.AGPSServerConfig."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['Enable',
                              'Password',
                              'ReferenceLatitude',
                              'ReferenceLongitude',
                              'ServerInUse',
                              'ServerPort',
                              'ServerURL',
                              'Username'])

      class ContinuousGPSStatus(core.Exporter):
        """Represents Device_v2_4.FAP.GPS.ContinuousGPSStatus."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['CurrentFix',
                              'Elevation',
                              'FirstFixTimeout',
                              'GotFix',
                              'LastFixDuration',
                              'LastFixTime',
                              'Latitude',
                              'LocationType',
                              'LockTimeOutDuration',
                              'Longitude',
                              'ReceiverStatus',
                              'SatelliteTrackingInterval',
                              'SatellitesTracked',
                              'TimingGood'])

    class PerfMgmt(core.Exporter):
      """Represents Device_v2_4.FAP.PerfMgmt."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['ConfigNumberOfEntries'],
                    lists=['Config'])

      class Config(core.Exporter):
        """Represents Device_v2_4.FAP.PerfMgmt.Config.{i}."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['Alias',
                              'Enable',
                              'Password',
                              'PeriodicUploadInterval',
                              'PeriodicUploadTime',
                              'URL',
                              'Username'])

  class FaultMgmt(core.Exporter):
    """Represents Device_v2_4.FaultMgmt."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['CurrentAlarmNumberOfEntries',
                          'ExpeditedEventNumberOfEntries',
                          'HistoryEventNumberOfEntries',
                          'MaxCurrentAlarmEntries',
                          'QueuedEventNumberOfEntries',
                          'SupportedAlarmNumberOfEntries'],
                  lists=['CurrentAlarm',
                         'ExpeditedEvent',
                         'HistoryEvent',
                         'QueuedEvent',
                         'SupportedAlarm'])

    class CurrentAlarm(core.Exporter):
      """Represents Device_v2_4.FaultMgmt.CurrentAlarm.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['AdditionalInformation',
                            'AdditionalText',
                            'AlarmChangedTime',
                            'AlarmIdentifier',
                            'AlarmRaisedTime',
                            'EventType',
                            'ManagedObjectInstance',
                            'PerceivedSeverity',
                            'ProbableCause',
                            'SpecificProblem'])

    class ExpeditedEvent(core.Exporter):
      """Represents Device_v2_4.FaultMgmt.ExpeditedEvent.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['AdditionalInformation',
                            'AdditionalText',
                            'AlarmIdentifier',
                            'EventTime',
                            'EventType',
                            'ManagedObjectInstance',
                            'NotificationType',
                            'PerceivedSeverity',
                            'ProbableCause',
                            'SpecificProblem'])

    class HistoryEvent(core.Exporter):
      """Represents Device_v2_4.FaultMgmt.HistoryEvent.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['AdditionalInformation',
                            'AdditionalText',
                            'AlarmIdentifier',
                            'EventTime',
                            'EventType',
                            'ManagedObjectInstance',
                            'NotificationType',
                            'PerceivedSeverity',
                            'ProbableCause',
                            'SpecificProblem'])

    class QueuedEvent(core.Exporter):
      """Represents Device_v2_4.FaultMgmt.QueuedEvent.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['AdditionalInformation',
                            'AdditionalText',
                            'AlarmIdentifier',
                            'EventTime',
                            'EventType',
                            'ManagedObjectInstance',
                            'NotificationType',
                            'PerceivedSeverity',
                            'ProbableCause',
                            'SpecificProblem'])

    class SupportedAlarm(core.Exporter):
      """Represents Device_v2_4.FaultMgmt.SupportedAlarm.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['EventType',
                            'PerceivedSeverity',
                            'ProbableCause',
                            'ReportingMechanism',
                            'SpecificProblem'])

  class Security(core.Exporter):
    """Represents Device_v2_4.Security."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['CertificateNumberOfEntries'],
                  lists=['Certificate'])

    class Certificate(core.Exporter):
      """Represents Device_v2_4.Security.Certificate.{i}."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['Enable',
                            'Issuer',
                            'LastModif',
                            'NotAfter',
                            'NotBefore',
                            'SerialNumber',
                            'SignatureAlgorithm',
                            'Subject',
                            'SubjectAlt'])

  class SoftwareModules(Device_v2_3.SoftwareModules):
    """Represents Device_v2_4.SoftwareModules."""

    def __init__(self, **defaults):
      Device_v2_3.SoftwareModules.__init__(self, defaults=defaults)
      self.Export(lists=['ExecEnv'])

    class ExecEnv(Device_v2_3.SoftwareModules.ExecEnv):
      """Represents Device_v2_4.SoftwareModules.ExecEnv.{i}."""

      def __init__(self, **defaults):
        Device_v2_3.SoftwareModules.ExecEnv.__init__(self, defaults=defaults)
        self.Export(params=['InitialExecutionUnitRunLevel'])


if __name__ == '__main__':
  print core.DumpSchema(Device_v2_4)
