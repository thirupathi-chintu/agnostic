resource "azurerm_container_registry" "container_registry" {
  name                     = "${var.registry_name}"
  resource_group_name      = "${var.resource_group_name}"
  location                 = "${var.resouce_group_location}"
  sku = "${var.sku_type}"
  admin_enabled = true
}