terraform {
  backend "s3" {
    bucket         = "{{ cookiecutter.aws_bucket_for_tf_state }}"
    key            = "terraform.tfstate"
    region         = "{{ cookiecutter.aws_region }}"
    dynamodb_table = "{{ cookiecutter.aws_dynamodb_lock_table }}"
    encrypt        = true
  }
}
