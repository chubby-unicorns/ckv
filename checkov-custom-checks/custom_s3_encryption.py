from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.cloudformation.checks.resource.base_resource_value_check import (
    BaseResourceCheck,
)

PII_TAG_KEY = "PII"


class BucketEncryption(BaseResourceCheck):
    def __init__(self):
        """
        S3 BUCKET ENCRYPTION (CloudFormation):
        We have 4 Requirements for S3 buckets:
            [1] All buckets must be encrypted, regardless of purpose
            [2] All buckets containing PII data must be encrypted using KMS
                (buckets to be idenifiable via tag, e.g. "PII")
            [3] If a bucket is configured to use KMS, it must have a
                KMSMasterKeyID specified and
            [4]   it must be configured with BucketKeyEnabled
        """
        name = "S3 Buckets: All S3 buckets must have encryption configured; PII buckets must use KMS and have KMSMasterKeyID and must have BucketKeyEnabled"
        id = "CKV_CUSTOM_AWS_CF_S3_ENCR"
        supported_resources = ["AWS::S3::Bucket"]
        categories = [
            CheckCategories.ENCRYPTION,
            CheckCategories.GENERAL_SECURITY,
        ]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
            guideline="https://docs.bridgecrew.io/docs/ckv2_custom_1",
        )

    def scan_resource_conf(self, conf):
        if "Properties" in conf.keys():
            Properties = conf["Properties"]

            # [1] CHECK IF BUCKET HAS ENCRYPTION CONFIGURED
            if "BucketEncryption" in Properties.keys():
                # [2] CHECK IF PII TAG IS CONFIGURED:
                is_pii = False
                if "Tags" in Properties.keys():
                    for tag in Properties["Tags"]:
                        if tag["Key"] == PII_TAG_KEY:
                            tag_value = str(tag["Value"]).lower()
                            if tag_value == "true" or tag_value == "yes":
                                is_pii = True
                BucketEncr = Properties["BucketEncryption"]
                if "ServerSideEncryptionConfiguration" in BucketEncr.keys():
                    SseConfig = BucketEncr["ServerSideEncryptionConfiguration"][0]
                    SseByDefault = SseConfig["ServerSideEncryptionByDefault"]
                    SSEAlgorithm = SseByDefault["SSEAlgorithm"]

                    # Check if kms is used
                    if SSEAlgorithm == "aws:kms":
                        is_kms = True
                    else:
                        is_kms = False

                    # [3] CHECK IF KMSMasterKeyID IS SPECIFIED:
                    try:
                        if SseByDefault["KMSMasterKeyID"]:
                            has_master_key = True
                    except KeyError:
                        has_master_key = False

                    # [4] CHECK IF BucketKeyEnabled IS TRUE:
                    try:
                        if SseConfig["BucketKeyEnabled"]:
                            has_bucket_key = True
                    except KeyError:
                        has_bucket_key = False

                    if is_pii and is_kms and has_master_key and has_bucket_key:
                        # If PII data it must use kms, have a key configured
                        # and that be a bucket key
                        CheckResult.PASSED
                    elif is_kms and has_master_key and has_bucket_key:
                        # It's OK to use KMS, as long as it has a master key
                        # configured and bucketkey enabled
                        CheckResult.PASSED
                    elif not is_pii and not is_kms:
                        # Fallback is SSES3 (AES256) - It's OK to use AES256,
                        # as long as it is not PII data
                        CheckResult.PASSED
                    else:
                        return CheckResult.FAILED
                    return CheckResult.PASSED
        return CheckResult.FAILED


check = BucketEncryption()
