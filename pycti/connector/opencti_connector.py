from enum import Enum

# 范围定义
# Scope definition
# EXTERNAL_IMPORT = None
# INTERNAL_IMPORT_FILE = Files mime types to support (application/json, ...)
# INTERNAL_ENRICHMENT = Entity types to support (Report, Hash, ...)
# INTERNAL_EXPORT_FILE = Files mime types to generate (application/pdf, ...)


# 连接者类型
class ConnectorType(Enum):
    EXTERNAL_IMPORT = "EXTERNAL_IMPORT"  # From remote sources to OpenCTI stix2
    INTERNAL_IMPORT_FILE = (
        "INTERNAL_IMPORT_FILE"  # From OpenCTI file system to OpenCTI stix2
    )
    INTERNAL_ENRICHMENT = "INTERNAL_ENRICHMENT"  # From OpenCTI stix2 to OpenCTI stix2
    INTERNAL_EXPORT_FILE = (
        "INTERNAL_EXPORT_FILE"  # From OpenCTI stix2 to OpenCTI file system
    )
    STREAM = "STREAM"  # Read the stream and do something


# 连接者
class OpenCTIConnector:
    """Main class for OpenCTI connector

    :param connector_id: id for the connector (valid uuid4) 连接者id
    :type connector_id: str
    :param connector_name: name for the connector 连接者名称
    :type connector_name: str
    :param connector_type: valid OpenCTI connector type (see `ConnectorType`) 类型
    :type connector_type: str
    :param scope: connector scope 域
    :type scope: str
    :raises ValueError: if the connector type is not valid 会抛出异常
    """

    def __init__(
        self,
        connector_id: str,
        connector_name: str,
        connector_type: str,
        scope: str,
        auto: bool,
    ):
        self.id = connector_id
        self.name = connector_name
        self.type = ConnectorType(connector_type)
        if self.type is None:
            raise ValueError("Invalid connector type: " + connector_type)
        self.scope = scope.split(",")
        self.auto = auto

    def to_input(self) -> dict:
        """connector input to use in API query

        :return: dict with connector data
        :rtype: dict
        """
        return {
            "input": {
                "id": self.id,
                "name": self.name,
                "type": self.type.name,
                "scope": self.scope,
                "auto": self.auto,
            }
        }
