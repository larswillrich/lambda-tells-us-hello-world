terraform destroy --target=module.api_gateway_deployment -auto-approve
terraform destroy --target=module.api_gateway_get_metho -auto-approve
terraform destroy --target=module.lambda_read_event -auto-approve
terraform destroy --target=module.basic_infrastructure -auto-approve
terraform destroy --target=module.api_gateway -auto-approve
