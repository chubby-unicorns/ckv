from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.cloudformation.checks.resource.base_resource_value_check import (
    BaseResourceCheck,
)


class Tags(BaseResourceCheck):
    def __init__(self):
        name = "Check that all resources are tagged with the key - Name"
        id = "CKV_CUSTOM_AWS_TAG_NAME"
        supported_resources = ["AWS::S3::Bucket"]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
            guideline="https://docs.bridgecrew.io/docs/ckv2_custom_1",
        )

    def scan_resource_conf(self, conf):
        if "Properties" in conf.keys():
            if "Tags" in conf["Properties"].keys():
                for tag in conf["Properties"]["Tags"]:
                    if tag["Key"] == "Name":
                        return CheckResult.PASSED
        return CheckResult.FAILED


check = Tags()
