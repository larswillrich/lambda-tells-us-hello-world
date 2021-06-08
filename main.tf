module "api_gateway" {
  source              = "github.com/larswillrich/api-gateway-with-lambda-and-dynamodb.git//modules/apigateway"
  api_name            = "hello"
  api_gateway_name    = "helloworld_api"
}

module "api_gateway_get_method" {
  source              = "github.com/larswillrich/api-gateway-with-lambda-and-dynamodb.git//modules/apiMethod"
  http_method         = "GET"
  lambda_invoke_arn   = module.lambda_hello_world.lambda_invoke_arn
  function_name       = module.lambda_hello_world.function_name
}

module "basic_infrastructure" {
  source              = "github.com/larswillrich/api-gateway-with-lambda-and-dynamodb.git//modules/basicInfrastructure"
}

module "lambda_hello_world" {
  source              = "github.com/larswillrich/api-gateway-with-lambda-and-dynamodb.git//modules/lambda"
  function_name       = "helloworld"
}

module "api_gateway_deployment" {
  source              = "github.com/larswillrich/api-gateway-with-lambda-and-dynamodb.git//modules/deployAPIGateway"
  stage_name          = "prod"
}
