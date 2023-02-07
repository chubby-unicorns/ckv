# S3 CloudFormation Examples

## Good: PII + KMS

```yaml
  PIIBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Delete
    Properties:
      BucketName: !Sub piibucket-${AWS::Region}-${AWS::AccountId}
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
              KMSMasterKeyID: arn:KMSMasterKeyID
            BucketKeyEnabled: true
      PublicAccessBlockConfiguration:
        BlockPublicAcls: TRUE
        BlockPublicPolicy: TRUE
        IgnorePublicAcls: TRUE
        RestrictPublicBuckets: TRUE
      Tags:
        - Key: PII
          Value: true
        - Key: Name
          Value: !Sub piibucket-${AWS::Region}-${AWS::AccountId}
```

---

## Good: Non-PII + KMS

```yaml
  NonPIIBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Delete
    Properties:
      BucketName: !Sub nonpiibucket-${AWS::Region}-${AWS::AccountId}
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
              KMSMasterKeyID: arn:KMSMasterKeyID
            BucketKeyEnabled: true
      PublicAccessBlockConfiguration:
        BlockPublicAcls: TRUE
        BlockPublicPolicy: TRUE
        IgnorePublicAcls: TRUE
        RestrictPublicBuckets: TRUE
      Tags:
        - Key: Name
          Value: !Sub nonpiibucket-${AWS::Region}-${AWS::AccountId}
```

---

## Good: Non-PII + AES256 (sse-s3)

```yaml
  NonPIIBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Delete
    Properties:
      BucketName: !Sub nonpiibucket-${AWS::Region}-${AWS::AccountId}
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: AES256
      PublicAccessBlockConfiguration:
        BlockPublicAcls: TRUE
        BlockPublicPolicy: TRUE
        IgnorePublicAcls: TRUE
        RestrictPublicBuckets: TRUE
      Tags:
        - Key: Name
          Value: !Sub nonpiibucket-${AWS::Region}-${AWS::AccountId}
```

---

## Bad: PII + KMS

```yaml
  PIIBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Delete
    Properties:
      BucketName: !Sub piibucket-${AWS::Region}-${AWS::AccountId}
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
      PublicAccessBlockConfiguration:
        BlockPublicAcls: TRUE
        BlockPublicPolicy: TRUE
        IgnorePublicAcls: TRUE
        RestrictPublicBuckets: TRUE
      Tags:
        - Key: PII
          Value: yes
        - Key: Name
          Value: !Sub piibucket-${AWS::Region}-${AWS::AccountId}
```

---

## Bad: Non-PII + KMS

```yaml
  NonPIIBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Delete
    Properties:
      BucketName: !Sub nonpiibucket-${AWS::Region}-${AWS::AccountId}
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
      PublicAccessBlockConfiguration:
        BlockPublicAcls: TRUE
        BlockPublicPolicy: TRUE
        IgnorePublicAcls: TRUE
        RestrictPublicBuckets: TRUE
      Tags:
        - Key: Name
          Value: !Sub nonpiibucket-${AWS::Region}-${AWS::AccountId}
```

---

## Bad: PII + AES256

```yaml
  PIIBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Delete
    Properties:
      BucketName: !Sub piibucket-${AWS::Region}-${AWS::AccountId}
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: AES256
      PublicAccessBlockConfiguration:
        BlockPublicAcls: TRUE
        BlockPublicPolicy: TRUE
        IgnorePublicAcls: TRUE
        RestrictPublicBuckets: TRUE
      Tags:
        - Key: PII
          Value: yes
        - Key: Name
          Value: !Sub piibucket-${AWS::Region}-${AWS::AccountId}
```

---
