# Checkov Custom Checks

Build custom Checkov checks using Python. Used in cases where we might have specific custom or complex policies for certain resources, e.g.:
- *S3 buckets must be encrypted, but if tagged as PII data, must use KMS, and if KMS, must specify a KMS key and be configured to use a bucketKey*
  - Example: `./checkov-custom-checks/custom_s3_encryption.py`
- *S3 buckets must have a `<Enter Tag Key Here>` tag (e.g. 'Name`)*
  - Example: `./checkov-custom-checks/custom_tag_name.py`

## Prerequisites for using custom checks

- Ensure the folder with custom checks also contains `__init__.py`

- If checks in local directory:
  - To include custom checks, use the `--external-checks-dir <dir>` argument, e.g.:
    - `checkov -d . --external-checks-dir ./checkov-custom-checks`
  - To debug a specific check, use the `--check <CHECKNAME>` argument, e.g.:
    - `checkov -d . --external-checks-dir ./checkov-custom-checks --check CKV_AWS_DUMMY_123`
