output "storage_access_key" {
  value = "${azurerm_storage_account.storage_account.primary_access_key}"
}

output "storage_id" {
  value = "${azurerm_storage_account.storage_account.id}"
}

