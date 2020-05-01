variable "resource_group_name" {
  type = "string"
}

variable "resouce_group_location" {
  type = "string"
}

variable "function_app_name" {
  type = "string"
}

variable "storage_connection_string" {
    type = "string"
}

variable "host_name" {
  type = "string"
}

variable "master_key" {
  type = "string"
}

variable "database_uri" {
  type = "string"
}

variable "collection_uri" {
  type = "string"
}

variable "runtime" {
  type = "string"
  default = "java"
}

variable "run_from_package" {
  default = true
}
variable "app_insights_location" {
  type = "string"
  default = "centralus"
}

