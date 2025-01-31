"""These are the custom STIX properties and observation types used internally by OpenCTI.

"""
from enum import Enum

# 枚举常量

class StixCyberObservableTypes(Enum):
    AUTONOMOUS_SYSTEM = "x-System"
    DIRECTORY = "Directory"
    DOMAIN_NAME = "Domain-Name"
    EMAIL_ADDR = "Email-Addr"
    EMAIL_MESSAGE = "Email-Message"
    EMAIL_MIME_PART_TYPE = "Email-Mime-Part-Type"
    ARTIFACT = "Artifact"
    FILE = "File"
    X509_CERTIFICATE = "X509-Certificate"
    IPV4_ADDR = "IPv4-Addr"
    IPV6_ADDR = "IPv6-Addr"
    MAC_ADDR = "Mac-Addr"
    MUTEX = "Mutex"
    NETWORK_TRAFFIC = "Network-Traffic"
    PROCESS = "Process"
    SOFTWARE = "Software"
    URL = "Url"
    USER_ACCOUNT = "User-Account"
    WINDOWS_REGISTRY_KEY = "Windows-Registry-Key"
    WINDOWS_REGISTRY_VALUE_TYPE = "Windows-Registry-Value-Type"
    X509_V3_EXTENSIONS_TYPE_ = "X509-V3-Extensions-Type"
    X_OPENCTI_HOSTNAME = "X-OpenCTI-Hostname"
    X_OPENCTI_CRYPTOGRAPHIC_KEY = "X-OpenCTI-Cryptographic-Key"
    X_OPENCTI_CRYPTOCURRENCY_WALLET = "X-OpenCTI-Cryptocurrency-Wallet"
    X_OPENCTI_TEXT = "X-OpenCTI-Text"
    X_OPENCTI_USER_AGENT = "X-OpenCTI-User-Agent"
    X_OPENCTI_SIMPLE_OBSERVABLE = "X-OpenCTI-Simple-Observable"

    @classmethod
    def has_value(cls, value):
        lower_attr = list(map(lambda x: x.lower(), cls._value2member_map_))
        return value.lower() in lower_attr


# 行业，组织，个人
class IdentityTypes(Enum):
    SECTOR = "Sector"
    ORGANIZATION = "Organization"
    INDIVIDUAL = "Individual"

    @classmethod
    def has_value(cls, value):
        lower_attr = list(map(lambda x: x.lower(), cls._value2member_map_))
        return value.lower() in lower_attr

# 位置：城市、国家、地区、位置
class LocationTypes(Enum):
    CITY = "City"
    COUNTRY = "Country"
    REGION = "Region"
    POSITION = "Position"

    @classmethod
    def has_value(cls, value):
        lower_attr = list(map(lambda x: x.lower(), cls._value2member_map_))
        return value.lower() in lower_attr


# 容器：注释、观察数据、意见、报告
class ContainerTypes(Enum):
    NOTE = "Note"
    OBSERVED_DATA = "Observed-Data"
    OPINION = "Opinion"
    REPORT = "Report"

    @classmethod
    def has_value(cls, value):
        lower_attr = list(map(lambda x: x.lower(), cls._value2member_map_))
        return value.lower() in lower_attr
