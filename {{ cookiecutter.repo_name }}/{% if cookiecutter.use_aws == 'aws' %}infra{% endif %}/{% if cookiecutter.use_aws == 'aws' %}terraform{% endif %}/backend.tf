terraform {
  backend "s3" {
    bucket         = "AWS_BUCKET_FOR_TF_STATE"
    key            = "terraform.tfstate"
    region         = "{{ cookiecutter.aws_region }}"
    dynamodb_table = "AWS_DYNAMODB_LOCK_TABLE"
    encrypt        = true
  }
}