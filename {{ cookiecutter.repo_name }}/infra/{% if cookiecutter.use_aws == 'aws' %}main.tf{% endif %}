resource "aws_s3_bucket" "tf_state" {
  bucket = "myproject-tf-state"
}

resource "aws_dynamodb_table" "tf_lock" {
  name         = "myproject-tf-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
