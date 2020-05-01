output "container_id" {
  value = "${azurerm_container_registry.container_registry.id}"
}

output "username" {
  value = "${azurerm_container_registry.container_registry.admin_username}"
}

output "password" {
  value = "${azurerm_container_registry.container_registry.admin_password}"
}

output "login_server" {
  value = "${azurerm_container_registry.container_registry.login_server}"
}
