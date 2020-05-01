resource "random_integer" "ri" {
  min = 10000
  max = 99999
}
resource "azurerm_cosmosdb_account" "cosmos_account" {
  name                = "cosmos-db-${random_integer.ri.result}"
  location            = "${var.resouce_group_location}"
  resource_group_name = "${var.resource_group_name}"
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  enable_automatic_failover = true

  consistency_policy {
    consistency_level       = "${var.consistency_level}"
  }

  geo_location {
    location          = "${var.failover_location}"
    failover_priority = 1
  }

  geo_location {
    prefix            = "cosmos-db-${random_integer.ri.result}-customid"
    location          = "${var.resouce_group_location}"
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_sql_database" "database" {
  name                = "${var.cosmos_db_name}"
  resource_group_name = "${var.resource_group_name}"
  account_name        = "${azurerm_cosmosdb_account.cosmos_account.name}"
}