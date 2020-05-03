variable “workspace_to_environment_map” {
  type = “map”  default = {
    dev     = “dev”
    qa      = “qa”
    staging = “staging”
    prod    = “prod”
  }
}
variable “environment_to_size_map” {
  type = “map”  default = {
    dev     = “small”
    qa      = “medium”
    staging = “large”
    prod    = “xlarge”
  }
}
