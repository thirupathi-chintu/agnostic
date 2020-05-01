variable "registry_name" {
  description = "Name of the azure container registry"
  type = "string"
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type = "string"
}

variable "resouce_group_location" {
  description = "Location of the resource group"
  type = "string"
}

variable "sku_type" {
  type = "string"
  default = "Basic"
}


