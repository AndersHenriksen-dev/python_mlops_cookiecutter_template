# Project variables (templated by Cookiecutter)
variable "project_name" {
  description = "Human-readable project name"
  type        = string
  default     = "{{ cookiecutter.project_name }}"
}

variable "project_name" {
  description = "Human-readable repo name"
  type        = string
  default     = "{{ cookiecutter.repo_name }}"
}

# Environment configuration
variable "environment" {
  description = "Deployment environment (e.g. dev, staging, prod)"
  type        = string
  default     = "dev"
}

# AWS settings
variable "aws_region" {
  description = "AWS region to deploy resources in"
  type        = string
  default     = "us-east-1"
}
