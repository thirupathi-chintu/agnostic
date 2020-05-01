variable "resource_group_name" {
  description = "Resouce group to which the storage account belongs to"
}

variable "location" {
  description = "Location of the storage account"
  default = "westus"
}

variable "storage_account_name" {
  description = "Storage account name"
  type ="string"
}

variable "storage_container_name" {
  description = "Storage container name"
  default = "vhds"
}

variable "account_tier" {
  description = "Storage account tier"
  default = "Standard"
}

variable "account_replication_type" {
  description = "Storage account replication type"
  default = "LRS"
}

variable "container_access_type" {
  description = "Storage container access type"
  default = "private"
}



