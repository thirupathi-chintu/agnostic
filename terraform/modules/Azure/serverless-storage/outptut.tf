output "database_id" {
  value = "${azurerm_cosmosdb_sql_database.database.id}"
}

output "read_endpoints" {
  value = "${azurerm_cosmosdb_account.cosmos_account.read_endpoints}"
}

output "write_endpoints" {
  value = "${azurerm_cosmosdb_account.cosmos_account.write_endpoints}"
}

output "primary_readonly_master_key" {
  value = "${azurerm_cosmosdb_account.cosmos_account.primary_readonly_master_key}"
}

output "secondary_readonly_master_key" {
  value = "${azurerm_cosmosdb_account.cosmos_account.secondary_readonly_master_key}"
}

output "primary_master_key" {
  value = "${azurerm_cosmosdb_account.cosmos_account.primary_master_key}"
}

output "secondary_master_key" {
  value = "${azurerm_cosmosdb_account.cosmos_account.secondary_master_key}"
}

output "connection_strings" {
  value = "${azurerm_cosmosdb_account.cosmos_account.connection_strings}"
}
