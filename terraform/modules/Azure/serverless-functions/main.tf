resource "azurerm_app_service_plan" "app_service_plan" {
  name                = "azure-functions-service-plan"
  location            = "${var.resouce_group_location}"
  resource_group_name = "${var.resource_group_name}"
  kind                =  "FunctionApp"

  sku {
    tier = "Dynamic"
    size = "Y1"
  }
}

resource "azurerm_function_app" "function_app" {
  name                      = "${var.function_app_name}"
  location                  = "${var.resouce_group_location}"
  resource_group_name       = "${var.resource_group_name}"
  app_service_plan_id       = "${azurerm_app_service_plan.app_service_plan.id}"
  storage_connection_string = "${var.storage_connection_string}"
  version = "~2"

  app_settings {
    HOST = "${var.host_name}"
    MASTER_KEY = "${var.master_key}"
    DATABASE_URI = "${var.database_uri}"
    COLLECTION_URI = "${var.collection_uri}"
    FUNCTIONS_WORKER_RUNTIME = "${var.runtime}"
    WEBSITE_RUN_FROM_PACKAGE = "${var.run_from_package}"
    APPINSIGHTS_INSTRUMENTATIONKEY = "${azurerm_application_insights.app_insights.instrumentation_key}"
  }

}

resource "azurerm_application_insights" "app_insights" {
  name                = "${var.function_app_name}-appinsights"
  location            = "${var.app_insights_location}"
  resource_group_name = "${var.resource_group_name}"
  application_type    = "java"
}