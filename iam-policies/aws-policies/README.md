# aws-policies
A set of example aws config files for use with [awscli](https://aws.amazon.com/cli/).

Text that should be replaced are marked with ```[[YOUR-VARIABLE]]``` (e.g. ```[[YOUR-BUCKET-NAME]]```).

## S3

### Simple S3 bucket
- Replace my-cool-bucket with your desired bucket name
```
aws s3api create-bucket --bucket my-cool-bucket --region eu-west-1
```

### Add public read policy
- Replace my-cool-bucket with your desired bucket name
```
curl https://raw.githubusercontent.com/tomfa/aws-policies/master/s3-bucket-public-read.json > s3-template.json
sed 's/\[\[YOUR-BUCKET-NAME\]\]/my-cool-bucket/g' s3-template.json > s3.json
aws s3api put-bucket-policy --bucket my-cool-bucket --policy file://s3.json
```

### Add CloudFront cdn
- Replace my-cool-bucket with your desired bucket name
```
aws configure set preview.cloudfront true
curl https://raw.githubusercontent.com/tomfa/aws-policies/master/cloudfront-static-webfiles.json > cf-template.json
sed 's/\[\[YOUR-BUCKET-NAME\]\]/my-cool-bucket/g' cf-template.json > cf.json
aws cloudfront create-distribution --distribution-config file://cf.json
```

### Add user with write access to the bucket
- Replace my-cool-bucket with your desired bucket name
- Replace CoolBucketGuy with your desired user name for the bucket user
- Replace arn:aws:iam::938109129012:policy/cool-bucket-write with your bucket arn (show as output in step 4)
```
curl https://raw.githubusercontent.com/tomfa/aws-policies/master/iam-bucket-write.json > iam-template.json
sed 's/\[\[YOUR-BUCKET-NAME\]\]/my-cool-bucket/g' iam-template.json > iam.json
aws iam create-user --user-name CoolBucketGuy
aws iam create-policy --policy-name cool-bucket-write --policy-document file://iam.json
aws iam attach-user-policy --usr-name CoolBucketGuy --policy-arn arn:aws:iam::938109129012:policy/cool-bucket-write 
aws iam create-access-key --user-name CoolBucketGuy
```

